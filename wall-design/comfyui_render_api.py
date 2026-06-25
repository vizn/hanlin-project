#!/usr/bin/env python3
"""
ComfyUI API 墙面渲染脚本
通过 HTTP 接口调用 ComfyUI 生成效果图
"""

import requests
import json
from pathlib import Path
import time

# 配置
COMFY_URL = "http://192.168.199.112:8188"
OUTPUT_DIR = Path("/root/.openclaw/workspace/wall-design/comfyui_output")
OUTPUT_DIR.mkdir(exist_ok=True)

def check_comfy_status():
    """检查 ComfyUI 状态"""
    try:
        response = requests.get(f"{COMFY_URL}/system/stats", timeout=5)
        return response.status_code == 200
    except Exception as e:
        print(f"❌ 无法连接 ComfyUI：{e}")
        return False

def load_workflow():
    """加载墙面设计工作流"""
    workflow_path = Path("/root/.openclaw/workspace/wall-design/comfyui_workflow.json")
    
    if not workflow_path.exists():
        print("❌ 工作流文件不存在，正在创建基础工作流...")
        
        # 创建基础工作流 JSON
        base_workflow = {
            "last_node_id": 50,
            "version": 0.4,
            "nodes": [
                {"id": 1, "type": "CheckpointLoaderSimple", 
                 "inputs": {"ckpt_name": ["sd1.5"]}},
                {"id": 2, "type": "CLIPTextEncode",
                 "inputs": {"clip": [0], "text": [["翰林光年墙面设计场景"]]},
                 "outputs": [{"name": "CLIP", "index": 0, "type": "CLIP"}]},
                {"id": 3, "type": "EmptyLatentImage",
                 "inputs": {"width": [1920], "height": [1080], "batch_size": [1]}},
                # ... 其他节点（简化版）
            ],
            "links": []
        }
        
        with open(workflow_path, 'w') as f:
            json.dump(base_workflow, f)
    
    return workflow_path.read_text()

def submit_prompt():
    """提交渲染任务"""
    try:
        response = requests.post(
            f"{COMFY_URL}/prompt",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"prompt": {}}),  # 简化版
            timeout=10
        )
        
        if response.status_code == 200:
            result = response.json()
            print("✅ 渲染任务已提交")
            return True
        else:
            print(f"❌ API 错误：{response.text}")
            return False
            
    except Exception as e:
        print(f"❌ 请求失败：{e}")
        return False

def check_queue():
    """检查渲染队列"""
    try:
        response = requests.get(
            f"{COMFY_URL}/queue",
            params={"dryrun": "false"},
            timeout=5
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"📊 渲染队列：{data}")
            
            # 等待任务完成
            while data.get('queue_running', False):
                time.sleep(3)
                response = requests.get(f"{COMFY_URL}/queue", timeout=5)
                data = response.json()
        
        return True
    except Exception as e:
        print(f"❌ 检查队列失败：{e}")
        return False

def main():
    """主渲染流程"""
    
    print("=" * 60)
    print("🎨 ComfyUI 墙面效果图渲染")
    print("=" * 60)
    
    # 步骤 1: 检查连接
    if not check_comfy_status():
        print("\n⚠️  无法连接到 ComfyUI，请确认:")
        print("   1. ComfyUI 是否正在运行")
        print(f"   2. 地址是否正确：{COMFY_URL}")
        print("\n💡 如需手动操作:")
        print(f"   访问 {COMFY_URL}/")
        return
    
    # 步骤 2: 加载工作流
    workflow = load_workflow()
    
    # 步骤 3: 提交渲染任务
    if submit_prompt():
        time.sleep(2)
        
        # 步骤 4: 检查队列
        check_queue()
        
        print(f"\n✅ 渲染完成！输出目录：{OUTPUT_DIR}")
        
        # 列出生成文件
        output_files = list(OUTPUT_DIR.glob("*.png")) + list(OUTPUT_DIR.glob("*.jpg"))
        for f in output_files:
            size_mb = round(f.stat().st_size / 1024 / 1024, 2)
            print(f"   - {f.name} ({size_mb}MB)")
    else:
        print("\n❌ 渲染任务提交失败")

if __name__ == "__main__":
    main()
