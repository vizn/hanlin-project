#!/bin/bash
# 墙面效果图 ComfyUI 批量渲染脚本

COMFY_URL="http://192.168.199.112:8188"
OUTPUT_DIR="/root/.openclaw/workspace/wall-design/comfyui_output"
mkdir -p "$OUTPUT_DIR"

echo "🎨 开始墙面效果图渲染..."

# 定义工作流文件
WORKFLOW_FILE="comfyui_workflow.json"

# 渲染参数配置
declare -A RENDER_PARAMS=(
    ["wall_a_glass"]="--steps 64 --cfg_scale 7.5 --width 1920 --height 1080"
    ["wall_b_white"]="--steps 32 --cfg_scale 7 --width 1920 --height 1080"
    ["wall_c_white"]="--steps 32 --cfg_scale 7 --width 1920 --height 1080"
)

# 渲染每面墙
for wall in "glass" "white_case" "white_philosophy"; do
    echo ""
    echo "📐 正在渲染：墙面 ${wall}..."
    
    # 构建 ComfyUI API 请求
    curl -X POST "${COMFY_URL}/prompt" \
        -H "Content-Type: application/json" \
        -d @${WORKFLOW_FILE} \
        --data-urlencode "output_path=${OUTPUT_DIR}/${wall}_render.png" &
    
    wait
    
done

echo ""
echo "✅ 渲染完成！结果保存在 ${OUTPUT_DIR}"
ls -lh "$OUTPUT_DIR"/*.png 2>/dev/null || echo "输出文件生成中..."
