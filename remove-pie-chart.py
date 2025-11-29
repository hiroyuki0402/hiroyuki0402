#!/usr/bin/env python3

svg_file = "profile-3d-contrib/profile-night-rainbow.svg"

with open(svg_file, 'r') as f:
    content = f.read()

# 開始位置を探す
start_marker = '<g transform="translate(40, 520)">'
start_pos = content.find(start_marker)

if start_pos != -1:
    pos = start_pos + len(start_marker)
    level = 1
    
    while level > 0 and pos < len(content):
        if content[pos:pos+3] == '<g ' or content[pos:pos+3] == '<g>':
            level += 1
            pos += 1
        elif content[pos:pos+4] == '</g>':
            level -= 1
            pos += 4
            if level == 0:
                end_pos = pos
                break
        else:
            pos += 1
    
    new_content = content[:start_pos] + content[end_pos:]
    
    with open(svg_file, 'w') as f:
        f.write(new_content)
    
    open_g = new_content.count('<g')
    close_g = new_content.count('</g>')
    print(f"<g>: {open_g}, </g>: {close_g}, 差分: {open_g - close_g}")
