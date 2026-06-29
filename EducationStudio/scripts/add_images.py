#!/usr/bin/env python3
"""
添加图像配图功能 - 调用 ComfyUI API 生成宣传册配图
"""

import json
import subprocess
from pathlib import Path


def generate_image_prompt(description):
    """将中文描述转换为英文 SD 提示词"""
    
    translation_map = {
        "菲律宾": "Philippines",
        "马尼拉": "Manila",
        "中国": "China",
        "学校": "school campus",
        "教室": "classroom",
        "学生": "students",
        "学习": "studying",
        "教育": "education",
        "现代化": "modern",
        "专业": "professional",
        "温馨": "warm and inviting",
    }
    
    text = description.lower()
    
    # 替换已知词汇
    for cn, en in translation_map.items():
        text = text.replace(cn, en)
    
    # 添加通用风格描述
    if "地标" in description or "城市" in description:
        text += ", city skyline, architectural photography"
    elif "校园" in description:
        text += ", school building, educational facility"
    elif "学生" in description:
        text += ", diverse students, collaborative learning"
    
    # 添加质量描述
    return f"{text}, high quality, professional photography style, {512}x{768}"


def extract_image_placeholders(markdown_file):
    """从 Markdown 文件中提取所有图像占位符"""
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取所有 ![生成图片：描述] 标记
    import re
    pattern = r'!\[生成图片：([^]]*)\]'
    matches = re.findall(pattern, content)
    
    return [
        {
            "description": desc,
            "prompt": generate_image_prompt(desc),
        }
        for desc in matches
    ]


def call_comfyui_api(prompt):
    """调用 ComfyUI API 生成图像"""
    
    print(f"\n🎨 正在生成图像...")
    print(f"   Prompt: {prompt[:100]}...")
    
    # 使用 comfyui_generate 工具（实际 API）
    import requests
    
    try:
        url = "http://localhost:8188/prompts"
        
        payload = json.dumps({
            "prompt": prompt,
            "negative_prompt": "blurry, low quality, distorted text, nsfw",
            "width": 512,
            "height": 768,
            "steps": 25,
            "sampler_name": "euler"
        })
        
        headers = {
            'Content-Type': 'application/json'
        }
        
        response = requests.post(url, data=payload, headers=headers, timeout=120)
        
        if response.status_code == 200:
            result = response.json()
            
            # 提取生成的图像文件名
            image_info = {
                "filename": result.get("filename", "generated_image.png"),
                "status": "success"
            }
            
            return image_info
        
        else:
            print(f"\n❌ ComfyUI API 请求失败：{response.status_code}")
            print(f"   响应：{response.text[:200]}")
            return None
            
    except Exception as e:
        print(f"\n⚠️ 调用 ComfyUI API 时出错：{e}")
        return None


def add_images_to_project(markdown_file, output_dir="/root/.openclaw/workspace/EducationStudio/outputs/Images"):
    """为项目添加图像配图"""
    
    # 创建输出目录
    Path(output_dir).mkdir(exist_ok=True)
    
    base_name = Path(markdown_file).stem
    
    print("=" * 60)
    print(f"ComfyUI 图像生成 - {base_name}")
    print(f"源文件：{markdown_file}")
    print(f"输出目录：{output_dir}")
    print("=" * 60)
    
    # Step 1: 提取图像需求
    image_requirements = extract_image_placeholders(markdown_file)
    
    if not image_requirements:
        print("\n⚠️  未找到图像占位符")
        return None
    
    print(f"\n📊 发现 {len(image_requirements)} 个图像需求:")
    
    # Step 2: 为每个图像调用 ComfyUI API
    for i, img_data in enumerate(image_requirements, 1):
        print(f"\n--- 生成第 {i} 张图 ---")
        
        prompt = img_data["prompt"]
        
        # 调用 ComfyUI
        image_info = call_comfyui_api(prompt)
        
        if image_info and "filename" in image_info:
            # Step 3: 下载图像到本地（如果 API 支持）
            try:
                import requests
                
                url = f"http://localhost:8188/view?filename={image_info['filename']}"
                
                response = requests.get(url, timeout=10)
                
                if response.status_code == 200 and len(response.content) > 0:
                    # 保存图像
                    output_path = Path(output_dir) / f"{base_name}_img_{i:03d}.png"
                    
                    with open(output_path, "wb") as f:
                        f.write(response.content)
                    
                    print(f"\n✅ 图像已保存到：{output_path}")
                    size_mb = output_path.stat().st_size / (1024 * 1024)
                    print(f"   💾 文件大小：{size_mb:.2f} MB")
                    
                    # 更新原 Markdown 文件中的占位符（替换为实际图像路径）
                    original_desc = img_data["description"]
                    new_text = f"[![Image: {original_desc}]({output_path})]"
                    content = Path(markdown_file).read_text(encoding='utf-8')
                    
                    # 简单替换（保留原始占位符但添加图像链接）
                    placeholder_pattern = f'!\[生成图片：{original_desc}\]'
                    if placeholder_pattern in content:
                        new_content = content.replace(placeholder_pattern, f"![Image]({output_path})")
                        Path(markdown_file).write_text(new_content, encoding='utf-8')
                        
                        print(f"\n✅ 已更新源文件：{markdown_file}")
                    
                    return {
                        "status": "success",
                        "images": [str(output_path)]
                    }
            
            except Exception as e:
                print(f"\n⚠️ 下载图像时出错：{e}")
        
        else:
            # 如果没有生成成功，创建占位符
            output_path = Path(output_dir) / f"{base_name}_img_{i:03d}.placeholder.png"
            
            with open(output_path, "wb") as f:
                f.write(b"\x89PNG\r\n\x1a\n")  # PNG header
            
            print(f"\n⚠️ 图像生成失败，创建占位符：{output_path}")
    
    return None


def main():
    """主函数"""
    
    import sys
    
    if len(sys.argv) < 2:
        # 默认处理最新 Markdown 文件
        markdown_files = list(Path("/root/.openclaw/workspace/EducationStudio/outputs/Markdown").glob("*.md"))
        
        if not markdown_files:
            source_md = "/root/.openclaw/workspace/中华书院_华侨生保录宣传册_校长版.md"
        else:
            source_md = str(markdown_files[-1])
    else:
        source_md = sys.argv[1]
    
    add_images_to_project(source_md)


if __name__ == "__main__":
    main()
