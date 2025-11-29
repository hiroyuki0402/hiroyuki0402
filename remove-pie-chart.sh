#!/bin/bash
# profile-night-rainbow.svgから円グラフ部分を削除

SVG_FILE="profile-3d-contrib/profile-night-rainbow.svg"

if [ -f "$SVG_FILE" ]; then
  echo "円グラフを削除中..."
  
  # 円グラフ部分を削除(idやclass名で特定)
  # SVGの構造に応じて調整が必要
  sed -i '/<g id="language-graph"/,/<\/g>/d' "$SVG_FILE" || true
  sed -i '/<g class="pie-chart"/,/<\/g>/d' "$SVG_FILE" || true
  
  echo "✅ 円グラフ削除完了"
else
  echo "⚠️ SVGファイルが見つかりません"
fi
