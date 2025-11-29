#!/usr/bin/env python3
import re

svg_file = "profile-3d-contrib/profile-night-rainbow.svg"

with open(svg_file, 'r') as f:
    content = f.read()

# translate(130, 130)"></g></g> を translate(130, 130)"></g> に修正
content = content.replace('translate(130, 130)"></g></g>', 'translate(130, 130)"></g>')

# 空の<g transform="translate(40, 520)">...</g>を削除
pattern = r'<g transform="translate\(40, 520\)">(?:<g[^>]*></g>)*</g>'
content = re.sub(pattern, '', content)

with open(svg_file, 'w') as f:
    f.write(content)

print("✅ 円グラフ削除完了")
