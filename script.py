import datetime

# 現在の時刻を取得
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# README.mdを読み込んで、特定のコメント行を書き換える
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# から の間を書き換える
start_marker = ""
end_marker = ""
new_content = f"{start_marker}\n最終更新日: {now}\n{end_marker}"

# 文字列を置換して保存
import re
pattern = f"{start_marker}.*?{end_marker}"
updated_readme = re.sub(pattern, new_content, content, flags=re.DOTALL)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_readme)
