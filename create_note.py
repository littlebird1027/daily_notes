import os
import subprocess
from datetime import datetime

# 切换到脚本所在目录（仓库根目录）
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# 获取当前日期
now = datetime.now()
date_str = now.strftime("%Y-%m-%d")
month_str = now.strftime("%Y-%m")
weekday = now.strftime("%A")

# 文件名和路径
file_name = f"{date_str}-{weekday}.md"
folder_path = os.path.join(".", month_str)
file_path = os.path.join(folder_path, file_name)

# 图片文件夹路径（和 .md 同名，放在同一层）
image_folder_name = f"{date_str}-{weekday}"
image_folder_path = os.path.join(folder_path, image_folder_name)

# 创建月份文件夹
os.makedirs(folder_path, exist_ok=True)

# 检查今日文件是否已存在
file_exists = os.path.exists(file_path)

if file_exists:
    print(f"⚠️  今日记录已存在：{file_path}")
    print("如需修改，请手动编辑该文件。")
else:
    # 创建图片文件夹
    os.makedirs(image_folder_path, exist_ok=True)
    print(f"📁 已创建图片文件夹：{image_folder_path}")

    # 写入模板内容（引用图片的写法示例）
    content = f"""# {date_str} {weekday} 记录

## 📌 今日事项
- 

## 📝 今日总结
- 

## 🖼️ 今日配图

<!-- 粘贴图片后会自动保存到 ./{image_folder_name}/ 下 -->
<!-- 例如：![描述](./{image_folder_name}/图片名.png) -->

## 💡 明日计划
- 

---
*创建时间：{now.strftime('%Y-%m-%d %H:%M:%S')}*
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ 已创建今日记录：{file_path}")

# 自动提交并推送
try:
    print("📤 正在推送到 GitHub...")
    result_add = subprocess.run(["git", "add", "."], check=True, capture_output=True, text=True)
    result_commit = subprocess.run(
        ["git", "commit", "-m", f"📝 添加 {date_str} 记录"],
        check=True,
        capture_output=True,
        text=True
    )
    result_push = subprocess.run(["git", "push"], check=True, capture_output=True, text=True)
    print("🎉 全部完成！")
except subprocess.CalledProcessError as e:
    print(f"❌ Git 操作失败：")
    if e.stderr:
        print(e.stderr)
    else:
        print(e.stdout)