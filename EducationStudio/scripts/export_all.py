#!/usr/bin/env python3
"""One-click export: generate DOCX, PDF, PPT from a Markdown file with brand styling."""

import sys, os, json

def ensure_dir(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)

def export_all(md_path, output_base=None, brand_path=None):
    md_path = os.path.abspath(md_path)
    if not os.path.exists(md_path):
        print(f"ERROR: Input not found: {md_path}")
        sys.exit(1)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    brand_path = brand_path or os.path.join(script_dir, "brand_template.json")

    if not output_base:
        name = os.path.splitext(os.path.basename(md_path))[0]
        output_dir = os.path.join(os.path.dirname(md_path), "..", "outputs")
        output_base = os.path.join(output_dir, name, name)

    output_base = output_base.replace(".md", "")

    sys.path.insert(0, script_dir)
    from md2docx import md_to_docx
    from md2ppt import md_to_ppt
    from md2pdf import md_to_pdf

    docx_path = output_base + ".docx"
    pdf_path = output_base + ".pdf"
    ppt_path = output_base + ".pptx"

    ensure_dir(docx_path)
    ensure_dir(pdf_path)
    ensure_dir(ppt_path)

    print(f"=== Exporting {md_path} ===")

    print(f"[1/3] Generating DOCX...")
    md_to_docx(md_path, docx_path, brand_path)

    print(f"[2/3] Generating PDF...")
    md_to_pdf(md_path, pdf_path, brand_path)

    print(f"[3/3] Generating PPT...")
    md_to_ppt(md_path, ppt_path, brand_path)

    print(f"\n=== All done ===")
    print(f"  DOCX: {docx_path}")
    print(f"  PDF:  {pdf_path}")
    print(f"  PPT:  {ppt_path}")

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        print("Usage: export_all.py <input.md> [output_base] [brand_template.json]")
        print("  output_base: output path without extension (e.g., outputs/中华书院/中华书院宣传册)")
        sys.exit(1)
    export_all(*args)
