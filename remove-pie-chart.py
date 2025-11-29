#!/usr/bin/env python3
import re

svg_file = "profile-3d-contrib/profile-night-rainbow.svg"

with open(svg_file, 'r') as f:
    content = f.read()

start_marker = '<g transform="translate(40, 520)">'
start_pos = content.find(start_marker)

if start_pos != -1:
    i = start_pos + len(start_marker)
    depth = 1
    
    while i < len(content) and depth > 0:
        if content[i:i+2] == '<g':
            depth += 1
            i += 1
        elif content[i:i+4] == '</g>':
            depth -= 1
            i += 4
            if depth == 0:
                end_pos = i
                new_content = content[:start_pos] + content[end_pos:]
                
                with open(svg_file, 'w') as f:
                    f.write(new_content)
                
                open_g = len(re.findall(r'<g[\s>]', new_content))
                close_g = new_content.count('</g>')
                print(f"✅ 削除完了")
                print(f"   <g>: {open_g}, </g>: {close_g}, 差分: {open_g - close_g}")
                break
        else:
            i += 1
else:
    print("⚠️ 対象が見つかりませんでした")
