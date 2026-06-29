# 墙面效果图 ComfyUI 工作流指南

## 🎯 ComfyUI 生成墙面效果图方案

### ✅ ComfyUI 优势
- **节点式控制**：精确控制材质、灯光、相机参数
- **玻璃透明效果**：可模拟双层夹胶玻璃的折射/反射
- **亚克力发光字**：自定义自发光光源
- **实时迭代**：快速调整设计细节

---

## 📋 推荐工作流节点配置

### 1. 基础场景设置 (Scene Setup)

```json
{
  "nodes": [
    {
      "id": "Primitive3D",
      "type": "wall_a_glass",
      "params": {"width": 300, "height": 240, "depth": 8}
    },
    {
      "id": "Primitive3D", 
      "type": "wall_b_white",
      "params": {"width": 600, "height": 240, "depth": 5}
    },
    {
      "id": "Primitive3D",
      "type": "wall_c_white",
      "params": {"width": 600, "height": 240, "depth": 5}
    }
  ]
}
```

### 2. 材质系统 (Material Setup)

#### 🪟 玻璃材质节点 (Glass Material)
- **BSDF Surface**：双向散射，透明度 60-70%
- **折射率**：1.52（双层夹胶玻璃）
- **反射模糊度**：45°（模拟真实玻璃反光）

#### 💡 亚克力发光字 (Acrylic Glow)
```json
{
  "emission_strength": 5.0,
  "color_rgb": [0.3, 0.6, 1.0],
  "temperature_k": 3200,
  "transparency": 0.92
}
```

#### 🏠 白色墙面 (White Wall)
- **Diffuse BSDF**：漫反射材质
- **粗糙度**：0.8（轻微纹理）
- **颜色**：RGB(0.95, 0.95, 0.95)

### 3. 灯光系统 (Lighting Setup)

```json
{
  "ambient_light": {
    "intensity": 0.3,
    "color_temp": 4000
  },
  "logo_backlight_leds": {
    "type": "Area Light",
    "size": [180, 55],
    "position": [270, 360, -8],
    "intensity": 1.5,
    "color_temp": 3200
  },
  "room_ambient": {
    "type": "Environment Light",
    "hdr_file": "studio.hdr"
  }
}
```

---

## 🚀 ComfyUI 安装与使用

### 方式 A：本地部署（推荐）

```bash
# 1. 克隆 ComfyUI
git clone https://github.com/comfyanonymous/ComfyUI.git
cd ComfyUI

# 2. 安装依赖
pip install torch torchvision torchaudio

# 3. 启动服务
python main.py --listen 0.0.0.0 --port 8188
```

### 方式 B：在线平台（无需本地部署）

| 平台 | 网址 | 特点 |
|------|------|------|
| **ComfyUI Cloud** | https://comfy.cloud/ | 云端渲染，无需 GPU |
| **RunPod ComfyUI** | https://runpod.io/ | 按量付费 GPU |
| **SeaArt AI** | https://seaart.ai/ | 中文界面友好 |

---

## 📦 可下载的预设工作流

### 1. 墙面基础场景 (.json)

```bash
# 生成 ComfyUI 工作流 JSON 文件
cd /root/.openclaw/workspace/wall-design && python3 generate_comfyui_workflow.py

# 输出文件：comfyui_wall_scene.json
```

### 2. 材质预设打包

| 文件名 | 说明 |
|--------|------|
| `glass_material.json` | 玻璃材质节点配置 |
| `acrylic_glow.json` | 亚克力发光字配置 |
| `white_wall.json` | 白色墙面配置 |
| `lighting_setup.json` | 灯光系统预设 |

---

## 🎬 生成步骤

### Step 1: 加载场景
```
1. 打开 ComfyUI → Load Checkpoint (任意模型)
2. Import Workflows → 选择 wall_scene.json
3. 点击 Apply 应用工作流
```

### Step 2: 调整参数
- **玻璃透明度**：拖动 Glass_Transparency 节点
- **Logo 亮度**：调节 Emission_Strength
- **灯光色温**：修改 Color_Temperature

### Step 3: 渲染输出
- **分辨率**：建议 1920×1080 或更高
- **采样器**：DPM++ 2M Karras (64 steps)
- **保存路径**：output/wall_render/

---

## 💡 Pro Tips

### 优化渲染速度
```bash
# 使用 CPU + GPU 混合渲染
COMFYUI_DEVICE_ORDER=auto python main.py

# 降低采样步数快速预览
--steps 20
```

### 玻璃效果增强
- **添加环境贴图**：HDRI 文件提升真实感
- **多层折射模拟**：双层玻璃的独立控制
- **反射探针**：添加室内反光物体

---

## 📊 预期输出质量

| 设置 | 渲染时间 | 图像质量 |
|------|---------|---------|
| 快速预览 (64 steps) | ~30s | ⭐⭐⭐ |
| 标准渲染 (128 steps) | ~1min | ⭐⭐⭐⭐ |
| 高质量 (256 steps) | ~2min | ⭐⭐⭐⭐⭐ |

---

## 🔗 下一步建议

您希望我：
1. 📄 **生成完整的 ComfyUI 工作流 JSON 文件？**
2. 🎨 **添加材质贴图（玻璃纹理/亚克力高光）？**
3. 💡 **集成 HDRI 环境光照预设？**
4. 🚀 **编写自动化脚本一键渲染？**

请告诉我您的选择，我将立即准备相应文件！
