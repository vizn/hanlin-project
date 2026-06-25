# ComfyUI 墙面渲染指南

## 🎯 快速开始

### 方式 A：手动调用（推荐）

```bash
# 1. 打开 ComfyUI 网页界面
http://192.168.199.112:8188

# 2. 加载工作流文件
File → Import → comfyui_workflow.json

# 3. 点击 Apply 应用工作流
# 4. 调整参数（玻璃透明度/Logo 亮度等）
# 5. 点击 Queue Prompt 开始渲染
```

### 方式 B：脚本自动调用

```bash
cd /root/.openclaw/workspace/wall-design && python3 comfyui_render_api.py
```

## 📦 工作流文件说明

| 文件名 | 作用 | 大小 |
|--------|------|------|
| `comfyui_workflow.json` | 墙面场景基础工作流 | ~2KB |
| `render_wall.sh` | 批量渲染脚本（bash） | ~1KB |
| `comfyui_render_api.py` | API 自动调用脚本 | ~4KB |

## 🎨 可调整参数

### 玻璃材质 (Glass Material)
- **透明度**: 60-70%
- **折射率**: 1.52（双层夹胶）
- **反射模糊度**: 45°

### Logo 发光字 (Acrylic Glow)
```json
{
  "emission_strength": 5.0,
  "color_rgb": [0.3, 0.6, 1.0],
  "temperature_k": 3200
}
```

### 灯光系统 (Lighting Setup)
- **环境光**: 强度 0.3，色温 4000K
- **Logo 背光 LED**: 强度 1.5，色温 3200K
- **房间环境光**: HDR 文件 `studio.hdr`

## 📊 预期输出质量

| 设置 | 渲染时间 | 图像质量 |
|------|---------|---------|
| 快速预览 (64 steps) | ~30s | ⭐⭐⭐ |
| 标准渲染 (128 steps) | ~1min | ⭐⭐⭐⭐ |
| 高质量 (256 steps) | ~2min | ⭐⭐⭐⭐⭐ |

## 🔗 ComfyUI 状态检查

```bash
# 查看系统资源使用率
curl http://192.168.199.112:8188/system/stats

# 查看渲染队列
curl http://192.168.199.112:8188/queue?dryrun=false
```

## 💡 Pro Tips

### 优化渲染速度
- **使用 GPU**: ComfyUI 自动检测 CUDA GPU
- **降低采样步数**: `--steps 30` 快速预览
- **批量处理**: 使用 `render_wall.sh` 脚本

### 增强真实感
- **添加 HDRI**: 环境贴图提升玻璃反射效果
- **多层材质**: 独立控制双层玻璃折射
- **添加室内反光物体**: 提高场景丰富度

## 📁 输出文件位置

```bash
/root/.openclaw/workspace/wall-design/comfyui_output/
├── wall_a_glass_render.png   # Logo 墙效果图
├── wall_b_white_case.png     # 案例墙效果图  
└── wall_c_white_philosophy.png  # 理念墙效果图
```

## 🔗 GitHub 仓库

完整方案已上传至：
https://github.com/vizn/hanlin-project.git/tree/main/wall-design

需要进一步帮助？请告诉我您的具体需求！
