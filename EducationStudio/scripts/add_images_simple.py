#!/usr/bin/env python3
"""
添加图像配图功能 - 简化版（直接调用 comfyui_generate）
"""

import json
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
    }
    
    text = description.lower()
    
    for cn, en in translation_map.items():
        text = text.replace(cn, en)
    
    if "地标" in description or "城市" in description:
        text += ", city skyline, architectural photography"
    elif "校园" in description:
        text += ", school building, educational facility"
    
    return f"{text}, high quality, professional photography style, {512}x{768}"


def extract_image_placeholders(markdown_file):
    """从 Markdown 文件中提取所有图像占位符"""
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
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


def call_comfyui_api(prompt, output_dir):
    """调用 comfyui_generate 工具生成图像"""
    
    print(f"\n🎨 正在生成图像...")
    print(f"   Prompt: {prompt[:100]}...")
    
    try:
        # 使用 comfyui_generate 工具（MCP API）
        from comfyui__comfyui_generate import generate
        
        result = generate(
            prompt=prompt,
            negative_prompt="blurry, low quality, distorted text, nsfw",
            width=512,
            height=768,
            steps=25
        )
        
        if result and "filename" in result:
            print(f"\n✅ 图像生成成功：{result['filename']}")
            
            # 下载图像到本地
            try:
                image_data = comfyui__comfyui_get_image(
                    filename=result["filename"],
                    type="output"
                )
                
                if isinstance(image_data, dict) and "base64" in image_data:
                    import base64
                    
                    # 解码并保存为 PNG
                    output_path = Path(output_dir) / f"{result['filename']}"
                    
                    with open(output_path, "wb") as f:
                        f.write(base64.b64decode(image_data["base64"]))
                    
                    print(f"   💾 已保存到：{output_path}")
                    size_mb = output_path.stat().st_size / (1024 * 1024)
                    print(f"   💾 文件大小：{size_mb:.2f} MB")
                    
                    return {
                        "status": "success",
                        "image_path": str(output_path),
                        "filename": result["filename"]
                    }
                
            except Exception as e:
                print(f"\n⚠️ 下载图像时出错：{e}")
        
        else:
            # 如果没有生成成功，创建占位符
            output_path = Path(output_dir) / f"{result['filename']}.placeholder.png"
            
            with open(output_path, "wb") as f:
                f.write(b"\x89PNG\r\n\x1a\n")
            
            print(f"\n⚠️ 图像生成失败，创建占位符：{output_path}")
        
        return None
        
    except Exception as e:
        print(f"\n❌ comfyui_generate 调用失败：{e}")
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
        prompt = img_data["prompt"]
        
        # 调用 ComfyUI
        image_info = call_comfyui_api(prompt, output_dir)
    
    return None


def main():
    """主函数"""
    
    import sys
    
    if len(sys.argv) < 2:
        source_md = "/root/.openclaw/workspace/中华书院_华侨生保录宣传册_校长版.md"
    else:
        source_md = sys.argv[1]
    
    add_images_to_project(source_md)


if __name__ == "__main__":
    main()
