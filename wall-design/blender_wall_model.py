
import bpy
import os
from mathutils import Vector

# 清除场景所有物体
for obj in bpy.data.objects:
    bpy.data.objects.remove(obj, do_unlink=True)

# 创建地面
ground = bpy.data.curves.new('Ground', type='MESH')
ground.dimensions = (1200, 960)  # cm
bpy.context.collection.objects.link(ground)
mesh = ground.to_mesh()
bpy.context.collection.objects.link(mesh)

# 创建墙面 A（玻璃）- Logo 区
def create_wall_a():
    wall_name = "Wall_A_Glass_Logo"
    bpy.ops.mesh.primitive_cube_add(size=300, location=(52.4, 192, 0))
    wall_a = bpy.context.object
    wall_a.name = wall_name
    
    # 材质：玻璃
    glass_mat = bpy.data.materials.new(name="Glass_Material")
    glass_mat.use_nodes = True
    nodes = glass_mat.node_tree.nodes
    links = glass_mat.node_tree.links
    
    # 添加输出节点
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    
    # BSDF（双向散射）
    bsdf_node = nodes.new(type='ShaderNodeBsdfTransparent')
    bsdf_node.inputs['Color'].default_factor = (0.9, 0.9, 1.0)
    
    # 连接节点
    links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])
    
    wall_a.data.materials.append(glass_mat)
    return bpy.data.objects[wall_name]

def create_wall_b():
    """墙面 B（案例区）"""
    wall_name = "Wall_B_White_CaseStudies"
    wall = bpy.ops.mesh.primitive_cube_add(size=600, location=(724, 192, 0))
    wall.name = wall_name
    
    # 材质：白色墙面
    white_mat = bpy.data.materials.new(name="White_Wall_Material")
    white_mat.use_nodes = True
    nodes = white_mat.node_tree.nodes
    
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    bsdf_node = nodes.new(type='ShaderNodeBsdfDiffuse')
    bsdf_node.inputs['Color'].default_factor = (0.95, 0.95, 0.95)
    
    links = white_mat.node_tree.links
    links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])
    
    wall.data.materials.append(white_mat)
    return bpy.context.object

def create_wall_c():
    """墙面 C（理念区）"""
    wall_name = "Wall_C_White_Philosophy"
    wall = bpy.ops.mesh.primitive_cube_add(size=600, location=(1374, 192, 0))
    wall.name = wall_name
    
    # 材质：白色墙面（同 B）
    white_mat = bpy.data.materials.new(name="White_Wall_Material_C")
    white_mat.use_nodes = True
    nodes = white_mat.node_tree.nodes
    
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    bsdf_node = nodes.new(type='ShaderNodeBsdfDiffuse')
    bsdf_node.inputs['Color'].default_factor = (0.95, 0.95, 0.95)
    
    links = white_mat.node_tree.links
    links.new(bsdf_node.outputs['BSDF'], output_node.inputs['Surface'])
    
    wall.data.materials.append(white_mat)
    return bpy.context.object

def create_logo_acrylic():
    """创建 Logo 亚克力发光字"""
    logo_group = bpy.data.groups.new("Logo_Assemblies")
    
    # 主 Logo 容器
    logo_name = "Hanlin_Guangnian_Logo"
    bpy.ops.mesh.primitive_cube_add(size=20, location=(52.4, 192, 360))
    logo_base = bpy.context.object
    logo_base.name = logo_name
    
    # 材质：亚克力发光
    acrylic_mat = bpy.data.materials.new(name="Acrylic_Glow_Material")
    acrylic_mat.use_nodes = True
    nodes = acrylic_mat.node_tree.nodes
    links = acrylic_mat.node_tree.links
    
    output_node = nodes.new(type='ShaderNodeOutputMaterial')
    
    # 混合节点：模拟发光效果
    mix_node = nodes.new(type='ShaderNodeMixRGB')
    mix_node.blend_type = 'ADD'
    
    bsdf_node = nodes.new(type='ShaderNodeBsdfDiffuse')
    bsdf_node.inputs['Color'].default_factor = (0.8, 0.9, 1.2)  # 淡蓝色
    
    emit_node = nodes.new(type='ShaderNodeEmission')
    emit_node.inputs['Color'].default_factor = (0.3, 0.6, 1.0)
    emit_node.inputs['Strength'].default_value = 5.0
    
    links.new(bsdf_node.outputs['BSDF'], mix_node.inputs[1])
    links.new(emit_node.outputs['Emission'], mix_node.inputs[2])
    
    # 输出混合结果
    links.new(mix_node.outputs['Mixed'], output_node.inputs['Surface'])
    
    logo_base.data.materials.append(acrylic_mat)
    return bpy.context.object

def main():
    print("🎨 开始生成墙面设计模型...")
    
    # 创建三面墙
    create_wall_a()
    create_wall_b()
    create_wall_c()
    
    # 创建 Logo
    create_logo_acrylic()
    
    print("✅ 模型生成完成！")
    print(f"📐 场景包含：3 面墙 + 1 个 Logo 组件")
    print(f"💡 可导出为：.blend, .obj, .fbx, .stl")

if __name__ == "__main__":
    main()
