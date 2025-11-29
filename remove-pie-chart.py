#!/usr/bin/env python3

svg_file = "profile-night-rainbow-original.svg"
output_file = "profile-3d-contrib/profile-night-rainbow.svg"

with open(svg_file, 'r') as f:
    content = f.read()

# 開始位置を探す
start_marker = '<g transform="translate(40, 520)">'
start_pos = content.find(start_marker)

if start_pos != -1:
    # 開始位置から、対応する閉じタグを探す
    # ネストレベルを数える
    pos = start_pos + len(start_marker)
    level = 1
    
    while level > 0 and pos < len(content):
        if content[pos:pos+3] == '<g ':
            level += 1
            pos += 3
        elif content[pos:pos+4] == '</g>':
            level -= 1
            if level == 0:
                # 終了位置を見つけた
                end_pos = pos + 4
                break
            pos += 4
        else:
            pos += 1
    
    # 削除
    new_content = content[:start_pos] + content[end_pos:]
    
    with open(output_file, 'w') as f:
        f.write(new_content)
    
    print(f"✅ 削除完了: {start_pos}から{end_pos}まで削除")
    print(f"   削除バイト数: {end_pos - start_pos}")
else:
    print("⚠️ 対象が見つかりませんでした")
