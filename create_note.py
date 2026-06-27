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

# 创建月份文件夹
os.makedirs(folder_path, exist_ok=True)

# 检查今日文件是否已存在
if os.path.exists(file_path):
    print(f"⚠️  今日记录已存在：{file_path}")
    print("如需修改，请手动编辑该文件。")
else:
    # 写入模板内容
    content = f"""# {date_str} {weekday} 记录

## 📌 今日事项
- 

## 📝 今日总结
- 

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
    subprocess.run(["git", "add", "."], check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", f"📝 添加 {date_str} 记录"], check=True, capture_output=True)
    subprocess.run(["git", "push"], check=True, capture_output=True)
    print("🎉 全部完成！")
except subprocess.CalledProcessError as e:
    print(f"❌ Git 操作失败：{e.stderr.decode() if e.stderr else '未知错误'}")