# 中华书院 (China Book School) 品牌设计规范

## 🎨 视觉识别系统

### 品牌色彩

```css
/* 主色调 */
primary-blue: #0066CC   /* 教育蓝 - 信任、专业 */
primary-dark: #004C99   /* 深蓝色 - 稳重 */
primary-light: #3388FF  /* 浅蓝色 - 活力 */

/* 辅助色 */
accent-gold: #FFD700    /* 金色 - 卓越、成就 */
accent-orange: #FF6B35  /* 橙色 - 热情、创新 */
accent-green: #2ECC71   /* 绿色 - 成长、希望 */

/* 中性色 */
text-dark: #2C3E50      /* 深灰蓝 - 正文文字 */
text-muted: #95A5A6     /* 浅灰 - 辅助文字 */
background-light: #F8F9FA /* 浅色背景 */
```

### 品牌字体

```css
/* 中文标题：Microsoft YaHei UI / STHeiti */
h1-h3: Microsoft YaHei UI, sans-serif

/* 中文正文：SimSun / PingFang SC */
body: SimSun, "PingFang SC", sans-serif

/* 英文/PPT: Arial / Helvetica Neue */
english: Arial, Helvetica, sans-serif
```

### Logo 使用规范

- **最小尺寸：** 1cm × 1cm (印刷) / 64×64px (数字)
- **安全距离：** logo 四周留白 = logo 高度 × 0.5
- **禁止事项：** 
  - ❌ 不要拉伸或变形
  - ❌ 不要添加阴影/渐变
  - ❌ 不要在复杂背景上使用

## 📐 文档格式规范

### DOCX 标准

```python
# A4 纸张 (210mm × 297mm)
页边距：上 2.5cm / 下 2.5cm / 左 3cm / 右 2.8cm

行距：1.5 倍或固定值 22pt

段落间距：段前 6pt / 段后 6pt
```

### PPT 标准

```python
# 16:9 比例 (1920×1080)
幻灯片尺寸：宽 13.33cm × 高 9.47cm
行高：最小 1.2cm（便于投影）

标题字号：36-44pt
正文字号：18-24pt
```

### PDF 标准

```python
# A4 或 Letter 尺寸
压缩质量：JPEG 85%, PNG LZW
文件大小：<10MB (网页分发) / <50MB (印刷)
```

## 🎯 内容规范

### 标题层级

```markdown
# H1 - 主标题 (24pt, primary-blue)
## —— 副标题 (18pt, text-muted)

---
# H2 - 章节标题 (18pt, primary-dark)
```

### 列表样式

- **项目符号：** 实心圆点 • 或方形 □
- **编号：** 中文数字（一、二、三）或阿拉伯数字 1. 2. 3.
- **缩进：** 每级右移 2cm

### CTA (Call-to-Action)

```python
# 行动呼吁模板
标题：立即行动！名额有限，先报先得！
副标题：⏰ 限时优惠中...

联系信息:
🔘 扫码咨询 [二维码占位符]
💬 微信添加顾问：[微信号]
📧 邮箱：partnerships@chinabookschool.ph
```

## 🌐 多语言支持

### 中文（简体）- 主要语言

使用场景：中国大陆市场、学校官方文件

### 英文 - 次要语言

使用场景：国际学校、海外宣传材料

**原则：** 
- 优先提供中英双语版本
- 确保翻译准确且符合品牌调性
- 避免直译导致的文化误解

## 📊 数据可视化规范

### 图表配色

```python
bar_colors = [
    "#0066CC",   # 主蓝色
    "#3388FF",   # 浅蓝色
    "#2ECC71",   # 绿色
    "#F39C12"    # 橙色
]

# 避免使用：红色警告色（除非必要）
# 避免超过 5 种颜色在同一图表中
```

### 数据标注

- **单位：** 统一使用中文单位（人、%、元）或国际标准符号
- **来源：** 在图表下方注明数据来源和日期
- **精度：** 百分比保留小数点后一位（如 85.3%）

## 📁 文件组织规范

```bash
outputs/
├── DOCX/
│   ├── [project]_[date].docx          # Word 文档
│   └── [project]_[date].pdf           # PDF 导出
├── PPT/
│   ├── [project]_[date].pptx          # PowerPoint
│   └── thumbnails/[name].png          # 缩略图
├── Images/
│   ├── generated_[timestamp]/         # ComfyUI 输出
│   ├── logo_*.png                     # Logo 资产（多版本）
│   └── icons/[category]/              # 图标集
└── Templates/
    ├── docx_master.dotx               # Word 主模板
    ├── ppt_master.potx                # PPT 主模板
```

## 🔧 技术实现

### Python 脚本示例

```python
from docx import Document
from pptx import Presentation
from pptx.dml.color import RGBColor

# 创建带品牌样式的 DOCX
def create_branded_docx():
    doc = Document()
    
    # 应用品牌样式
    style = doc.styles['Normal']
    font = style.element.rPr.rFonts.set(qn('w:eastAsia'), 'SimSun')
    
    return doc

# 创建带品牌样式的 PPT
def create_branded_ppt():
    prs = Presentation()
    
    # 定义幻灯片母版
    master = prs.slide_master
    
    for shape in master.shapes:
        if hasattr(shape, 'fill'):
            shape.fill.solid()
            shape.fore_color.rgb = RGBColor(0, 102, 204)  # primary-blue
            
    return prs
```

## 📝 审核清单

### 发布前检查

- [ ] Logo 位置正确且大小合适
- [ ] 所有颜色来自品牌调色板
- [ ] 字体符合规范（无非法外文字体）
- [ ] 图片清晰度高，无变形模糊
- [ ] 数据准确且有来源标注
- [ ] CTA 信息完整可联系
- [ ] 文件能在主流办公软件打开

### 版本管理

```bash
v1.0 - 初始版本
v2.0 - 第一次修订（根据反馈）
final - 批准发布版本
archive - 历史归档版本
```

---

*中华书院品牌规范 | 确保一致性和专业性*

© EducationStudio | All Rights Reserved
