#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
supplier_map.json を Shopify Admin API から全件再生成する（ヘッドレス用）

前提（環境変数）
  SHOPIFY_SHOP   例: eezo.myshopify.com
  SHOPIFY_TOKEN  Admin API アクセストークン（read_products 権限のカスタムアプリ）

使い方
  SHOPIFY_SHOP=eezo.myshopify.com SHOPIFY_TOKEN=shpat_xxx python build_supplier_map.py
  → supplier_map.json を出力

メモ
  - custom.supplier が null の商品はスキップ（未登録）
  - チャット（Shopifyコネクタ）経由でも同等のマップを生成できる。トークンを置きたくない場合はそちらを使う。
"""
import os, json, sys, urllib.request

SHOP = os.environ.get("SHOPIFY_SHOP")
TOKEN = os.environ.get("SHOPIFY_TOKEN")
API_VERSION = "2025-01"

QUERY = """
query Dump($cursor: String) {
  products(first: 100, after: $cursor) {
    pageInfo { hasNextPage endCursor }
    edges { node {
      title
      supplier: metafield(namespace: "custom", key: "supplier") { value }
      spn: metafield(namespace: "custom", key: "supplier_product_name") { value }
    } }
  }
}
"""


def call(cursor):
    url = f"https://{SHOP}/admin/api/{API_VERSION}/graphql.json"
    body = json.dumps({"query": QUERY, "variables": {"cursor": cursor}}).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": TOKEN,
    })
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode("utf-8"))


def main():
    if not SHOP or not TOKEN:
        sys.exit("環境変数 SHOPIFY_SHOP と SHOPIFY_TOKEN を設定してください。")
    out, cursor, pages = {}, None, 0
    while True:
        data = call(cursor)
        if "errors" in data:
            sys.exit(f"APIエラー: {data['errors']}")
        conn = data["data"]["products"]
        for e in conn["edges"]:
            n = e["node"]
            sup = (n.get("supplier") or {}).get("value") if n.get("supplier") else None
            if not sup:
                continue
            spn = (n.get("spn") or {}).get("value") if n.get("spn") else ""
            out[n["title"]] = {"supplier": sup, "supplier_product_name": spn or ""}
        pages += 1
        if not conn["pageInfo"]["hasNextPage"]:
            break
        cursor = conn["pageInfo"]["endCursor"]
    with open("supplier_map.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"supplier_map.json を出力（{len(out)}商品 / {pages}ページ走査）")


if __name__ == "__main__":
    main()
