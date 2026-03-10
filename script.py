import datetime

# 1. 現在の時刻を取得
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 2. README.mdを一行ずつ読み込む
try:
    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()
except FileNotFoundError:
    lines = ["\n", "\n"]

# 3. 新しい中身を作成する
new_lines = []
skip = False

for line in lines:
    # 開始マーカーを見つけたら、マーカーと新しい日付を追加し、中身のスキップを開始
    if "" in line:
        new_lines.append("\n")
        new_lines.append(f"最終更新日: {now}\n")
        skip = True
    # 終了マーカーを見つけたら、スキップを終了し、マーカーを追加
    elif "" in line:
        new_lines.append("\n")
        skip = False
    # マーカーの外側（普通の文章）だけを新しいリストにコピー
    elif not skip:
        new_lines.append(line)

# 4. 上書き保存
with open("README.md", "w", encoding="utf-8") as f:
    f.writelines(new_lines)
