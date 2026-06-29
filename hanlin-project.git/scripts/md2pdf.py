#!/usr/bin/env python3
"""
Markdown → PDF 转换脚本（支持 LibreOffice/Pandoc 备用方案）
"""

import subprocess
from pathlib import Path


def convert_md_to_pdf(md_file, output_dir="/root/.openclaw/workspace/EducationStudio/outputs/PDF"):
    """将 Markdown 转换为 PDF"""
    
    # 创建输出目录
    Path(output_dir).mkdir(exist_ok=True)
    
    base_name = Path(md_file).stem
    
    print("=" * 60)
    print(f"Markdown → PDF 转换")
    print(f"输入：{md_file}")
    print(f"输出：{output_dir}/{base_name}.pdf")
    print("=" * 60)
    
    # 方案 1: LibreOffice（推荐）
    try:
        result = subprocess.run([
            "libreoffice", "--headless", "--convert-to", "pdf",
            md_file, f"--outdir={output_dir}"
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            output_path = Path(output_dir) / f"{base_name}.pdf"
            print(f"\n✅ LibreOffice 转换成功")
            print(f"   📄 PDF 文件：{output_path}")
            
            if output_path.exists():
                size_mb = output_path.stat().st_size / (1024 * 1024)
                print(f"   💾 文件大小：{size_mb:.2f} MB")
                
                return True
        else:
            print(f"\n⚠️ LibreOffice 转换失败，尝试备用方案...")
    
    except FileNotFoundError:
        print("\n⚠️ LibreOffice 未安装，使用备用方案...")
    
    # 方案 2: Pandoc（如果可用）
    try:
        result = subprocess.run([
            "pandoc", md_file, "-o", f"{output_dir}/{base_name}.pdf",
            "--pdf-engine=xelatex"  # 支持中文的 LaTeX 引擎
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            print(f"\n✅ Pandoc 转换成功")
            output_path = Path(output_dir) / f"{base_name}.pdf"
            print(f"   📄 PDF 文件：{output_path}")
            
            return True
            
    except FileNotFoundError:
        print("\n⚠️ Pandoc 也未安装，使用备用方案...")
    
    # 方案 3: wkhtmltopdf（最后尝试）
    try:
        result = subprocess.run([
            "wkhtmltohtml", md_file, "-o", f"{output_dir}/{base_name}.html"
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0 and Path(f"{output_dir}/{base_name}.html").exists():
            # HTML→PDF（简单转换）
            subprocess.run([
                "wkhtmltohtml", f"{output_dir}/{base_name}.html",
                "-o", f"{output_dir}/{base_name}.pdf"
            ], capture_output=True, text=True)
            
            print(f"\n✅ wkhtmltopdf 转换成功")
            output_path = Path(output_dir) / f"{base_name}.pdf"
            print(f"   📄 PDF 文件：{output_path}")
            
            return True
            
    except FileNotFoundError:
        print("\n⚠️ wkhtmltohtml 也未安装...")
    
    # 如果所有方案都失败，创建空 PDF（占位符）
    empty_pdf = Path(output_dir) / f"{base_name}.pdf"
    if not empty_pdf.exists():
        # 使用 base64 编码空 PDF
        import base64
        pdf_content = b"%PDF-1.4\n" + b"\n%EOF"
        with open(empty_pdf, "wb") as f:
            f.write(pdf_content)
        
        print(f"\n⚠️ 所有转换方法都不可用，已创建空 PDF 占位符")
    
    return False


def main():
    """主函数"""
    
    # 默认处理源文件
    source_md = "/root/.openclaw/workspace/中华书院_华侨生保录宣传册_校长版.md"
    
    if not Path(source_md).exists():
        print(f"\n❌ 错误：找不到源文件")
        print(f"路径：{source_md}")
        return
    
    # 执行转换
    convert_md_to_pdf(source_md)


if __name__ == "__main__":
    main()
