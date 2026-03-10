import datetime
import re

# 1. 現在の時刻を取得
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 2. README.mdを読み込む
try:
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    content = "\n"

# 3. 置換するルールを決める
# 「マーカーとその間にあるもの全て」を、新しいマーカーと日付に置き換える
start_marker = ""
end_marker = ""

# 正規表現でマーカー間を特定（.は改行を含む全ての文字にマッチさせる）
pattern = f"{start_marker}.*?{end_marker}"
replacement = f"{start_marker}\n最終更新日: {now}\n{end_marker}"

updated_content = re.sub(pattern, replacement, content, flags=re.DOTALL)

# 4. もしマーカーが見つからなかった場合（初回など）の保険
if start_marker not in updated_content:
    updated_content += f"\n\n{replacement}"

# 5. 上書き保存
with open("README.md", "w", encoding="utf-8") as f:
    f.write(updated_content)
