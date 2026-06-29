#!/usr/bin/env python3
"""
从学校官网下载实景图（PPCHA 等）
用于宣传册中的真实场景展示
"""

import requests
from pathlib import Path


def download_school_images(school_url, output_dir="assets/official_images"):
    """从学校官网下载图片资源"""
    
    # 创建输出目录
    Path(output_dir).mkdir(exist_ok=True)
    
    print("=" * 60)
    print(f"下载 {school_url} 的官方实景图")
    print("=" * 60)
    
    # PPCHA 官网图片（从官网提取）
    school_images = [
        {
            "name": "ppcha_campus.jpg",
            "url": "http://www.ppcha.edu.ph/images/gallery/ppcha-campus-1.jpg"  # 示例 URL
        },
        {
            "name": "ppcha_library.jpg", 
            "url": "http://www.ppcha.edu.ph/images/gallery/library-interior.jpg"
        },
        {
            "name": "ppcha_students.jpg",
            "url": "http://www.ppcha.edu.ph/images/gallery/student-activities.jpg"
        }
    ]
    
    downloaded = []
    
    for img in school_images:
        try:
            print(f"\n下载：{img['name']}")
            
            # 检查文件是否已存在
            output_path = Path(output_dir) / img["name"]
            
            if not output_path.exists():
                # 下载图像（实际 URL 需从官网获取）
                response = requests.get(img["url"], timeout=10)
                
                if response.status_code == 200:
                    with open(output_path, "wb") as f:
                        f.write(response.content)
                    
                    print(f"   ✅ 已保存：{output_path}")
                    downloaded.append({
                        "name": img["name"],
                        "type": "official",
                        "source": school_url
                    })
                else:
                    print(f"   ⚠️  下载失败（HTTP {response.status_code}）")
            else:
                print(f"   ✅ 文件已存在：{output_path}")
                
        except Exception as e:
            print(f"   ❌ 下载出错：{e}")
    
    return downloaded


def generate_comfyui_images(output_dir="assets/comfyui_generated"):
    """使用 ComfyUI 生成其他图像（数据可视化、图标等）"""
    
    # 创建输出目录
    Path(output_grad).mkdir(exist_ok=True)
    
    print("\n" + "=" * 60)
    print("ComfyUI 图像生成")
    print("=" * 60)
    
    # 示例：生成数据可视化图表占位图
    comfyui_prompts = [
        {
            "theme": "录取率统计",
            "prompt": "Infographic bar chart showing admission rates, blue and gold color scheme, professional data visualization style, clean background"
        },
        {
            "theme": "升学路径图",
            "prompt": "Educational pathway diagram with arrows connecting schools, modern infographic style, educational theme"
        },
        {
            "theme": "学生活动照片",
            "prompt": "Students learning in classroom, diverse group collaborating on projects, bright and positive atmosphere, high quality photography"
        }
    ]
    
    return comfyui_prompts


def create_mixed_brochure():
    """创建混合配图版宣传册"""
    
    print("\n" + "=" * 60)
    print("创建混合配图版宣传册")
    print("=" * 60)
    
    # Step 1: 下载官网实景图（如果尚未下载）
    ppcha_images = download_school_images(
        "http://www.ppcha.edu.ph",
        output_dir="assets/official_images"
    )
    
    if not ppcha_images:
        print("\n⚠️  暂无 PPCHA 官网图片，使用占位符")
    
    # Step 2: ComfyUI 生成其他图像
    comfyui_prompts = generate_comfyui_images()
    
    if comfyui_prompts:
        print(f"\n🎨 待生成 {len(comfyui_prompts)} 张 ComfyUI 配图:")
        
        # TODO: 实际调用 comfyui_generate API
        
    # Step 3: Summary
    print("\n" + "=" * 60)
    print("混合配图策略说明")
    print("=" * 60)
    
    print("""
📸 **实景图（从官网下载）:**
   - PPCHA 校园照片（真实场景展示）
   - 学生活动照片（增强可信度）
   - 图书馆/教室环境图
  
🎨 **ComfyUI 生成图：**
   - 数据可视化图表（录取率等）
   - 图标与插图（装饰性元素）
   - 概念性场景图（如"理想校园生活"）

💡 **混合配图优势:**
   ✅ 真实感：官网实景图增强信任度
   ✅ 创意性：ComfyUI 生成图提供新鲜视觉体验
   ✅ 灵活性：可根据需要动态替换图像
""")


if __name__ == "__main__":
    create_mixed_brochure()
