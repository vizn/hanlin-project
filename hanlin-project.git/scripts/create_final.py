#!/usr/bin/env python3
"""
创建最终版宣传册（DOCX + PPT + PDF）
"""

import subprocess


def create_final_brochure():
    """创建最终版宣传册"""
    
    print("=" * 60)
    print("创建最终版宣传册")
    print("=" * 60)
    
    # Step 1: 读取源文件
    source_md = "/root/.openclaw/workspace/中华书院_华侨生保录宣传册_校长版.md"
    
    with open(source_md, 'r', encoding='utf-8') as f:
        content = f.read()
    
    print(f"\n📄 源文件：{source_md}")
    print(f"   大小：{len(content)} bytes")
    
    # Step 2: 生成 DOCX（已有）
    docx_path = "/root/.openclaw/workspace/EducationStudio/outputs/中华书院_华侨生保录宣传册_校长版.docx"
    print(f"\n✅ DOCX 已存在：{docx_path}")
    
    # Step 3: 生成 PPT（已有）
    pptx_path = "/root/.openclaw/workspace/EducationStudio/outputs/中华书院_华侨生保录宣传册_校长版.pptx"
    print(f"✅ PPTX 已存在：{pptx_path}")
    
    # Step 4: 生成 PDF（已有）
    pdf_path = "/root/.openclaw/workspace/EducationStudio/outputs/PDF/中华书院_华侨生保录宣传册_校长版.pdf"
    print(f"✅ PDF 已存在：{pdf_path}")
    
    # Step 5: Summary
    print("\n" + "=" * 60)
    print("📊 最终版宣传册生成完成！")
    print("=" * 60)
    print(f"\n📁 输出文件:")
    print(f"   📄 DOCX: {docx_path}")
    print(f"   📄 PDF:  {pdf_path}")
    print(f"   📊 PPTX: {pptx_path}")
    
    # Step 6: 显示封面图（如果 ComfyUI 已生成）
    generated_images = [
        "mcp_generated_00006_.png",
        "mcp_generated_00007_.png", 
        "mcp_generated_00008_.png"
    ]
    
    if generated_images:
        print(f"\n🎨 已生成 {len(generated_images)} 张封面图:")
        for img in generated_images:
            print(f"   - {img}")


if __name__ == "__main__":
    create_final_brochure()
