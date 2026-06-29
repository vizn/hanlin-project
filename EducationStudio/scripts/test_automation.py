#!/usr/bin/env python3
"""测试 CopyWriter + CreativeDirector 自动化流程"""

from pathlib import Path
import json

def test_copywriter():
    """CopyWriter 技能测试 - 生成优化后的文案"""
    
    # 读取源 Markdown
    source = "/root/.openclaw/workspace/中华书院_华侨生保录宣传册_校长版.md"
    
    with open(source, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # CopyWriter：添加图像提示词标记
    def add_image_markers(text):
        """为各章节添加![生成图片：描述] 标记"""
        
        text = text.replace(
            '### P1 封面',
            '### P1 封面\n![生成图片：菲律宾马尼拉地标 + 中国元素融合，教育主题，专业风格]'
        )
        
        return text
    
    # 保存优化后的文案
    output_file = "/root/.openclaw/workspace/EducationStudio/outputs/Markdown/华侨生项目_copy.md"
    optimized_content = add_image_markers(content)
    
    Path(output_file).write_text(optimized_content, encoding='utf-8')
    
    print("✅ CopyWriter 完成")
    print(f"   📄 优化文案：{output_file}")


def test_creativedirector():
    """CreativeDirector 技能测试 - 生成图像提示词"""
    
    # 从优化后的文案提取关键视觉需求
    source = "/root/.openclaw/workspace/EducationStudio/outputs/Markdown/华侨生项目_copy.md"
    
    with open(source, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 识别需要图像的章节并生成提示词
    image_requirements = []
    
    for line in content.split('\n'):
        if '### P' in line or '封面' in line or '为什么合作' in line:
            page_num = line.split('### ')[-1]
            
            # 为每个主要章节生成提示词
            prompts_map = {
                'P1': '菲律宾马尼拉城市地标，中华书院校门，教育主题',
                'P2': '教育行业挑战数据可视化，生源竞争图表',
                'P3': '国际课程与升学路径流程图',
                'P4': '菲律宾校园场景，中文教学环境',
            }
            
            if page_num in prompts_map:
                image_requirements.append({
                    "page": page_num,
                    "prompt": f"{prompts_map[page_num]}，专业教育风格，主色调蓝色",
                    "description": line.strip()[:30]
                })
    
    # 保存图像需求到 JSON
    output_file = "/root/.openclaw/workspace/EducationStudio/outputs/Markdown/华侨生项目_image_requirements.json"
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(image_requirements, f, ensure_ascii=False, indent=2)
    
    print("✅ CreativeDirector 完成")
    print(f"   🎨 图像需求：{output_file}")


def main():
    print("=" * 60)
    print("EducationStudio 自动化流程测试")
    print("=" * 60)
    print()
    
    test_copywriter()
    test_creativedirector()
    
    # 列出输出文件
    output_dir = "/root/.openclaw/workspace/EducationStudio/outputs/Markdown"
    print()
    print("📁 生成的文件：")
    for file in Path(output_dir).glob("*"):
        size = file.stat().st_size / 1024 if file.stat().st_size else 0
        print(f"   {file.name} ({size:.1f} KB)")


if __name__ == "__main__":
    main()
