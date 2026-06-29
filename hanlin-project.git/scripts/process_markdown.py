#!/usr/bin/env python3
"""
ComfyUI 工作流集成脚本 - 处理 Markdown 中的图像占位符并生成对应图片
"""

import re
import json
from pathlib import Path


def translate_chinese_to_english(description):
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
    
    # 简单翻译逻辑
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
    elif "教室" in description:
        text += ", modern classroom, natural lighting"
    
    # 添加通用质量描述
    return f"{text}, high quality, professional photography style, {512}x{768}"


def extract_image_prompts(markdown_file):
    """从 Markdown 文件中提取所有图像占位符"""
    
    with open(markdown_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 提取所有 ![生成图片：描述] 标记
    pattern = r'!\[生成图片：([^]]*)\]'
    matches = re.findall(pattern, content)
    
    return [
        {
            "description": desc,
            "prompt": translate_chinese_to_english(desc),
            "workflow": "Brochure",
            "width": 512,
            "height": 768
        }
        for desc in matches
    ]


def generate_image_map(input_file, output_dir):
    """生成图像映射文件"""
    
    input_path = Path(input_file)
    project_name = input_path.stem
    
    # 提取图像需求
    image_requirements = extract_image_prompts(input_file)
    
    if not image_requirements:
        print(f"⚠️  未找到图像占位符：{input_file}")
        return None
    
    # 生成输出路径
    output_path = Path(output_dir) / f"{project_name}_image_map.json"
    
    # 保存为 JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump({
            "images": image_requirements,
            "input_file": str(input_path),
            "output_dir": str(output_dir)
        }, f, ensure_ascii=False, indent=2)
    
    print(f"✅ 图像映射已生成：{output_path}")
    print(f"   📊 共发现 {len(image_requirements)} 个图像需求")
    
    # 显示示例
    if image_requirements:
        example = image_requirements[0]
        print(f"\n🔍 示例图像需求:")
        print(f"   描述：{example['description']}")
        print(f"   提示词：{example['prompt'][:100]}...")


def preview_workflow(input_file):
    """预览 ComfyUI 工作流配置"""
    
    input_path = Path(input_file)
    project_name = input_path.stem
    
    # 读取工作流 JSON
    workflow_path = f"/root/.openclaw/workspace/EducationStudio/workflows/Brochure/{project_name}_workflow.json"
    
    if not Path(workflow_path).exists():
        workflow_path = "/root/.openclaw/workspace/EducationStudio/workflows/Brochure/brochure_workflow.json"
    
    with open(workflow_path, 'r', encoding='utf-8') as f:
        workflow = json.load(f)
    
    print("\n📋 ComfyUI 工作流配置:")
    print(f"   🎨 Workflow 文件：{workflow_path}")
    print(f"   📐 图像尺寸：512x768")
    print(f"   ⚙️ 采样步骤：25")
    print(f"   🎲 CFG Scale: 7.0")
    
    return workflow


def main():
    import sys
    
    input_file = None
    if len(sys.argv) >= 2:
        input_file = sys.argv[1]
    else:
        # 默认处理最新 Markdown 文件
        markdown_files = list(Path("/root/.openclaw/workspace/EducationStudio/outputs/Markdown").glob("*.md"))
        
        if markdown_files:
            input_file = str(markdown_files[-1])
        else:
            print("❌ 未找到 Markdown 源文件")
            return
    
    if not input_file:
        print("❌ 输入文件为空")
        return
    
    project_name = Path(input_file).stem
    
    print("=" * 60)
    print(f"ComfyUI 图像生成集成脚本")
    print(f"输入文件：{input_file}")
    print(f"项目名称：{project_name}")
    print("=" * 60)
    
    # Step 1: 预览工作流配置
    workflow = preview_workflow(input_file)
    
    # Step 2: 生成图像映射文件
    output_dir = "/root/.openclaw/workspace/EducationStudio/outputs/Images"
    generate_image_map(input_file, output_dir)
    
    print("\n💡 提示:")
    print("   - 使用 comfyui_generate 工具时，需提供 prompt 和 workflow_json")
    print("   - 图像将保存在 outputs/Images/generated_*/ 目录下")


if __name__ == "__main__":
    main()
