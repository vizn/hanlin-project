#!/bin/bash
# EducationStudio 自动化工作流启动脚本

WORKSPACE="/root/.openclaw/workspace/EducationStudio"

echo "=========================================="
echo "EducationStudio 自动化工作流"
echo "=========================================="

# Step 1: 生成基础文档（DOCX/PPTX）
echo ""
echo "[Step 1] 生成 DOCX + PPTX..."
source "$WORKSPACE/venv/bin/activate" && cd "$WORKSPACE" && python scripts/gen_simple.py 2>&1 | tail -20

# Step 2: 转换 PDF
echo ""
echo "[Step 2] 生成 PDF..."
libreoffice --headless --convert-to pdf \
    "/root/.openclaw/workspace/中华书院_华侨生保录宣传册_校长版.md" \
    --outdir "$WORKSPACE/outputs/PDF" 2>&1 | tail -5

# Step 3: ComfyUI 图像配图（通过 MCP API）
echo ""
echo "[Step 3] ComfyUI 图像配图..."
echo "   🎨 使用 comfyui_generate 工具生成图像"
echo "   💡 提示词：Philippines Manila city skyline, education theme"

# 调用 ComfyUI（MCP API）
echo ""
echo "[Step 3] 生成封面图示例..."
comfyui__comfyui_generate \
    prompt="Philippines Manila city skyline, Chinese school entrance, education theme, professional photography style, high quality" \
    negative_prompt="blurry, low quality, distorted text, nsfw, watermark" \
    width=512 height=768 steps=25 2>&1 | tail -10

echo ""
echo "=========================================="
echo "✅ 自动化流程完成！"
echo "=========================================="
