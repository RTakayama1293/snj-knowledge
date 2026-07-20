#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
北海道地名マップ生成スクリプト
ベース画像に地名と位置マーカーを追加（透明背景対応）
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ベース画像パス
BASE_IMAGE = '/mnt/user-data/uploads/hokkaidomap.png'
OUTPUT_DIR = '/mnt/user-data/outputs'

# フォント設定（日本語対応）
FONT_SIZE_JP = 90
FONT_SIZE_EN = 70
STAR_SIZE = 50

# 座標補正パラメータ（札幌基準の相対スケーリング）
ANCHOR_X = 580   # 札幌のX座標（基準点）
ANCHOR_Y = 700   # 札幌のY座標（基準点）
ANCHOR_OFFSET_X = -5   # 札幌自体の微調整（若干西へ）
ANCHOR_OFFSET_Y = 5    # 札幌自体の微調整（若干北へ）
SCALE_X = 0.98   # 東西方向の縮小率（札幌からの距離に適用）
SCALE_Y = 0.99   # 南北方向の縮小率（札幌からの距離に適用）

# テスト用地名データ（x, y座標は画像サイズ1600x1200基準、修正版）
SAMPLE_LOCATIONS = [
    {"name": "札幌市", "romaji": "Sapporo", "x": 580, "y": 700},
    {"name": "函館市", "romaji": "Hakodate", "x": 450, "y": 1050},
    {"name": "旭川市", "romaji": "Asahikawa", "x": 800, "y": 380},
    {"name": "釧路市", "romaji": "Kushiro", "x": 1280, "y": 680},
    {"name": "稚内市", "romaji": "Wakkanai", "x": 800, "y": 60},
    {"name": "帯広市", "romaji": "Obihiro", "x": 1150, "y": 760},
    {"name": "小樽市", "romaji": "Otaru", "x": 500, "y": 650},
    {"name": "富良野市", "romaji": "Furano", "x": 880, "y": 560},
]

def draw_star(draw, x, y, size, color='red'):
    """星型マーカーを描画"""
    # 5角星の座標計算
    import math
    points = []
    for i in range(10):
        angle = math.pi * 2 * i / 10 - math.pi / 2
        r = size if i % 2 == 0 else size * 0.4
        points.append((
            x + r * math.cos(angle),
            y + r * math.sin(angle)
        ))
    draw.polygon(points, fill=color)

def correct_coordinates(x, y):
    """座標補正：札幌を基準点とした相対スケーリング

    札幌から離れるほど補正量が大きくなる仕組み
    """
    # 札幌からの相対位置を計算
    dx = x - ANCHOR_X
    dy = y - ANCHOR_Y

    # 相対位置にスケーリングを適用
    dx_scaled = dx * SCALE_X
    dy_scaled = dy * SCALE_Y

    # 札幌の補正後位置を基準に戻す
    x_corrected = int(ANCHOR_X + ANCHOR_OFFSET_X + dx_scaled)
    y_corrected = int(ANCHOR_Y + ANCHOR_OFFSET_Y + dy_scaled)

    return x_corrected, y_corrected

def create_location_map(location_data):
    """地名マップ画像を生成（透明背景対応）"""
    # ベース画像を読み込み
    img = Image.open(BASE_IMAGE).convert('RGBA')

    # 白い背景を透明にする
    datas = img.getdata()
    newData = []
    for item in datas:
        # 白っぽい色（RGB値が高い）を透明にする
        if item[0] > 240 and item[1] > 240 and item[2] > 240:
            newData.append((255, 255, 255, 0))  # 完全透明
        else:
            newData.append(item)

    img.putdata(newData)
    draw = ImageDraw.Draw(img)

    # フォント設定（システムフォントを使用）
    try:
        # 日本語フォント（高品質レンダリング）
        font_jp = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", FONT_SIZE_JP)
        font_en = ImageFont.truetype("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc", FONT_SIZE_EN)
    except:
        # フォントが見つからない場合
        try:
            font_jp = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", FONT_SIZE_JP)
            font_en = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", FONT_SIZE_EN)
        except:
            font_jp = ImageFont.load_default()
            font_en = ImageFont.load_default()

    x = location_data['x']
    y = location_data['y']

    # 座標補正を適用
    x, y = correct_coordinates(x, y)

    # 星マーカーを描画
    draw_star(draw, x, y, STAR_SIZE)

    # テキスト配置（星の下）
    text_y = y + STAR_SIZE + 20

    # 日本語地名（白文字、黒縁取り）
    bbox_jp = draw.textbbox((0, 0), location_data['name'], font=font_jp)
    text_width_jp = bbox_jp[2] - bbox_jp[0]
    text_x_jp = x - text_width_jp/2
    draw.text((text_x_jp, text_y), location_data['name'],
              fill='white', font=font_jp, stroke_width=4, stroke_fill='black')

    # ローマ字
    text_y += FONT_SIZE_JP + 10
    bbox_en = draw.textbbox((0, 0), location_data['romaji'], font=font_en)
    text_width_en = bbox_en[2] - bbox_en[0]
    text_x_en = x - text_width_en/2
    draw.text((text_x_en, text_y), location_data['romaji'],
              fill='white', font=font_en, stroke_width=3, stroke_fill='black')

    return img

def main():
    """メイン処理"""
    # 出力ディレクトリ作成
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"サンプル画像生成開始: {len(SAMPLE_LOCATIONS)}件")
    print("背景: 透明 / 高品質レンダリング")
    print(f"座標補正: 札幌基準スケーリング (X={SCALE_X}, Y={SCALE_Y})")

    for location in SAMPLE_LOCATIONS:
        try:
            # 画像生成
            img = create_location_map(location)

            # ファイル名作成（都市名のみ、拡張子なし）
            filename = f"hokkaido_map_{location['romaji'].lower()}.png"
            filepath = os.path.join(OUTPUT_DIR, filename)

            # 高品質PNG保存（透明度対応）
            img.save(filepath, 'PNG', optimize=False, compress_level=1)
            print(f"✓ 生成完了: {location['name']} ({location['romaji']})")

        except Exception as e:
            print(f"✗ エラー: {location['name']} - {str(e)}")
            import traceback
            traceback.print_exc()

    print(f"\n全{len(SAMPLE_LOCATIONS)}件の画像を生成しました")
    print(f"出力先: {OUTPUT_DIR}")
    print("背景: 透明（RGBA）")

if __name__ == "__main__":
    main()
