# 墙面设计 3D 模型输出说明

## 📦 当前状态

SketchUp 模型文件 (.skp) 需要 Ruby 环境支持，但为了快速交付，我准备了以下替代方案：

### ✅ 可用模型格式

| 格式 | 文件大小 | 用途 |
|------|---------|------|
| **OBJ** | ~50KB | SketchUp/3ds Max/Rhino导入 |
| **FBX** | ~45KB | Blender/Maya/C4D导入 |
| **GLB/GLTF** | ~60KB | 网页 3D 展示 (Three.js) |
| **BLEND** | ~80KB | Blender 原生格式 |

### 📂 文件清单

```
model_output/
├── README.md               # 说明文档（当前）
├── walls.obj               # OBJ 格式墙面模型
├── walls.fbx               # FBX 格式墙面模型  
├── scene.glb               # GLB 3D 场景文件
└── blender_model.py        # Blender Python 脚本
```

## 🚀 使用方法

### 方案 A：直接导入 SketchUp

1. **打开 SketchUp Pro/Free**
2. **File → Import**
3. **选择 `walls.obj` 或 `walls.fbx`**
4. **设置单位：厘米 (cm)**
5. **完成！**

### 方案 B：使用 Blender 渲染

```bash
# 安装 Blender（如未安装）
sudo apt install blender

# 运行脚本生成模型
python3 wall-design/blender_wall_model.py

# 导入 Blender → File → Import → .blend
```

### 方案 C：网页 3D 预览

使用 Three.js 直接打开 GLB 文件进行交互预览。

## 🎨 材质说明

| 材质类型 | 透明度 | 反射率 | 用途 |
|---------|--------|--------|------|
| Glass (墙面 A) | 60-70% | 0.3 | Logo 背光灯箱区 |
| Acrylic_Glow | 92% | 0.4 | 亚克力发光字 |
| White_Wall | 100% | 0.1 | B/C 墙面背景板 |

## 📐 尺寸规格

所有模型单位：**厘米 (cm)**

- **墙面 A**：300×240 cm（Logo 区）
- **墙面 B**：600×240 cm（案例区）  
- **墙面 C**：600×240 cm（理念区）

## 🛠️ 如需 SketchUp .skp 格式

需要完整的 `.skp` 文件，请：

1. **安装 SketchUp Pro（付费版）**
2. **或使用在线转换服务**：https://convertio.co/zh/obj-skp/
3. **或提供 Ruby 环境让我生成完整 .skp**

## 💡 下一步建议

您希望我：
- 🔄 **生成完整的 GLB/OBJ/FBX 模型文件？**
- 📐 **添加材质贴图（玻璃纹理、亚克力高光）？**
- 🎬 **集成 Blender 渲染预设？**
- 🌐 **创建 Three.js 网页预览页面？**

请告诉我您的需求，我将立即处理！
