#!/bin/bash
SVG_FILE="profile-3d-contrib/profile-night-rainbow.svg"

if [ -f "$SVG_FILE" ]; then
  echo "円グラフ削除中..."
  
  # transform="translate(40, 520)" を持つg要素全体を削除
  # これで円グラフと凡例の両方が消える
  perl -i -0pe 's/<g[^>]*transform="translate\(40,\s*520\)"[^>]*>.*?<\/g>//gs' "$SVG_FILE"
  
  echo "✅ 円グラフ削除完了"
else
  echo "⚠️ SVGファイルが見つかりません"
fi
