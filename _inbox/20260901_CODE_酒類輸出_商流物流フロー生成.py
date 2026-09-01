# -*- coding: utf-8 -*-
import html

SHU, GRY, AOI = "var(--shu)", "var(--gry)", "var(--aoi)"

# ---- geometry (viewBox 980 x 312) ----
GUT = 92
S_K1 = (120, 30, 170, 46)      # 蔵 upper
S_K2 = (120, 88, 170, 46)      # 蔵 lower
S_SNJ_HALF = (330, 30, 180, 46)
S_SNJ_FULL = (330, 30, 180, 104)
S_AG = (650, 30, 160, 104)
S_SFC = (850, 30, 110, 104)
B_KURA = (120, 222, 150, 46)
B_FW = (310, 222, 180, 46)
B_CUS = (540, 222, 170, 46)
B_SFC = (790, 222, 170, 46)

def esc(t): return html.escape(t, quote=False)

def box(b, title, subs, tone="plain"):
    x, y, w, h = b
    cx, cy = x + w/2, y + h/2
    if tone == "solid":
        fill, stroke, sw, tc, sc, dash = "var(--ink)", "var(--ink)", 1, "var(--paper)", "var(--paper-2)", ""
    elif tone == "faint":
        fill, stroke, sw, tc, sc, dash = "var(--surface)", "var(--rule)", 1, "var(--ink-3)", "var(--ink-3)", ' stroke-dasharray="4 3"'
    else:
        fill, stroke, sw, tc, sc, dash = "var(--surface)", "var(--rule-2)", 1.2, "var(--ink)", "var(--ink-2)", ""
    n = len(subs)
    ty = cy - (n * 14) / 2 + 5
    o = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="2" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{dash}/>',
         f'<text x="{cx}" y="{ty:.0f}" text-anchor="middle" class="nt" fill="{tc}">{esc(title)}</text>']
    for i, s in enumerate(subs):
        o.append(f'<text x="{cx}" y="{ty+16+i*14:.0f}" text-anchor="middle" class="ns" fill="{sc}">{esc(s)}</text>')
    return "\n      ".join(o)

def arrow(x1, x2, y, color, dash=False, faint=False, label=None, ly=None, cross=False):
    op = ' opacity="0.42"' if faint else ""
    da = ' stroke-dasharray="7 5"' if dash else ""
    mid = (x1 + x2) / 2
    o = [f'<line x1="{x1}" y1="{y}" x2="{x2-9}" y2="{y}" stroke="{color}" stroke-width="2"{da}{op}/>',
         f'<polygon points="{x2},{y} {x2-10},{y-4.5} {x2-10},{y+4.5}" fill="{color}"{op}/>']
    if cross:
        o.append(f'<g stroke="{color}" stroke-width="2.2"><line x1="{mid-6}" y1="{y-6}" x2="{mid+6}" y2="{y+6}"/>'
                 f'<line x1="{mid-6}" y1="{y+6}" x2="{mid+6}" y2="{y-6}"/></g>')
    if label:
        o.append(f'<text x="{mid}" y="{ly}" text-anchor="middle" class="al" fill="{color}"{op}>{esc(label)}</text>')
    return "\n      ".join(o)

def figure(sc):
    p = []
    # lane labels
    p.append(f'<text x="{GUT}" y="76" text-anchor="end" class="lane">商流</text>'
             f'<text x="{GUT}" y="92" text-anchor="end" class="lane2">売買・請求</text>')
    p.append(f'<text x="{GUT}" y="241" text-anchor="end" class="lane">物流</text>'
             f'<text x="{GUT}" y="257" text-anchor="end" class="lane2">モノの流れ</text>')
    # tie: declaration count follows the commercial flow
    p.append('<line x1="625" y1="140" x2="625" y2="216" stroke="var(--ink-3)" stroke-width="1.2" stroke-dasharray="3 4"/>'
             '<polygon points="625,222 621,213 629,213" fill="var(--ink-3)"/>'
             '<text x="634" y="182" class="tie" fill="var(--ink-3)">申告の本数は商流で決まる</text>')
    # commercial lane
    snj = S_SNJ_FULL if sc["snj_full"] else S_SNJ_HALF
    p.append(box(S_K1, "大和川・天鏡", ["当社が販売"]))
    p.append(box(S_K2, "他社蔵 2〜3社", [sc["k2sub"]]))
    p.append(box(snj, "新日本海商事", sc["snj"], sc.get("snj_tone", "plain")))
    p.append(box(S_AG, "輸入代理店", ["theSFCグループ"]))
    p.append(box(S_SFC, "theSFC", ["シンガポール"]))
    if sc["snj_full"]:
        p.append(arrow(290, 330, 53, SHU, label="仕入", ly=20))
        p.append(arrow(290, 330, 111, SHU, label="仕入", ly=101))
        p.append(arrow(510, 650, 82, SHU, label=sc["shu_label"], ly=72))
    else:
        p.append(arrow(290, 330, 53, SHU, label="仕入", ly=20))
        p.append(arrow(510, 650, 53, SHU, label=sc["shu_label"], ly=20))
        p.append(arrow(290, 650, 111, GRY, label=sc["gry_label"], ly=101,
                       faint=sc.get("gry_faint", False), cross=sc.get("gry_cross", False)))
    p.append(arrow(810, 850, 82, GRY))
    # physical lane
    p.append(box(B_KURA, "各蔵", ["4〜5社"]))
    p.append(box(B_FW, "フォワーダー", sc["fw"], sc.get("fw_tone", "plain")))
    p.append(box(B_CUS, "輸出通関", sc["cus"], sc.get("cus_tone", "plain")))
    p.append(box(B_SFC, "シンガポール着", ["輸入代理店が引き取り"]))
    f = sc.get("but_faint", False)
    p.append(arrow(270, 310, 245, AOI, dash=True, faint=f, label="集荷", ly=290))
    p.append(arrow(490, 540, 245, AOI, dash=True, faint=f, label=sc["but_label"], ly=290))
    p.append(arrow(710, 790, 245, AOI, dash=True, faint=f, label="海上輸送", ly=290))
    return "\n      ".join(p)

SC = {
"a_asis": dict(snj_full=False, k2sub="当社は絡まない",
  snj=["輸出者（大和川・天鏡分）"], shu_label="当社が輸出者・1本",
  gry_label="輸出者が決まらない", gry_faint=True, gry_cross=True,
  fw=["未定", "束ねる業者が決まらない"], fw_tone="faint",
  cus=["申告 当社1本", "＋ 他社蔵は未定"], but_label="混載できていない", but_faint=True),
"a_tobe": dict(snj_full=True, k2sub="当社が買い取る",
  snj=["輸出者・売主", "4〜5蔵すべて"], snj_tone="solid", shu_label="1本にまとまる",
  fw=["当社指定", "1コンテナ"], cus=["申告 1本"], cus_tone="solid",
  but_label="混載 1コンテナ"),
"b_asis": dict(snj_full=False, k2sub="当社は絡まない",
  snj=["輸出者（大和川・天鏡分）"], shu_label="当社が輸出者・1本",
  gry_label="他社蔵は直・2〜3本",
  fw=["定温リーファー定期便", "1社のみ・高い"],
  cus=["申告 当社1本", "＋ 各蔵2〜3本"], but_label="混載はできる"),
"b_tobe": dict(snj_full=False, k2sub="当社は絡まない",
  snj=["輸出者（大和川・天鏡分）"], shu_label="当社が輸出者・1本",
  gry_label="他社蔵は直・2〜3本",
  fw=["相見積で選び直す", "1コンテナ"], fw_tone="solid",
  cus=["申告 当社1本", "＋ 各蔵2〜3本（変わらず）"], but_label="混載 1コンテナ"),
}

def fig(key, tag, title, caption, aria):
    return f'''<figure class="fig">
    <div class="fh"><span class="tag">{esc(tag)}</span><h3>{esc(title)}</h3></div>
    <div class="svgwrap"><svg viewBox="0 0 980 312" role="img" aria-label="{esc(aria)}">
      {figure(SC[key])}
    </svg></div>
    <figcaption>{caption}</figcaption>
  </figure>'''

PAGE = f'''<title>日本酒混載輸出の商流と物流</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=BIZ+UDPGothic:wght@400;700&display=swap">
<style>
:root{{
  --paper:#FBFAF8; --paper-2:#EFEAE6; --surface:#FFFFFF;
  --ink:#232020; --ink-2:#6A625E; --ink-3:#9C948E;
  --rule:#E2DCD6; --rule-2:#CFC7C0;
  --shu:#B23A2E; --gry:#8E8681; --aoi:#2F5D73;
}}
@media (prefers-color-scheme: dark){{
  :root:not([data-theme="light"]){{
    --paper:#171513; --paper-2:#2A2521; --surface:#211D1A;
    --ink:#F0EAE4; --ink-2:#B3A9A1; --ink-3:#8A807A;
    --rule:#332C27; --rule-2:#463D37;
    --shu:#E88B79; --gry:#A79E97; --aoi:#8CBBD3;
  }}
}}
:root[data-theme="dark"]{{
  --paper:#171513; --paper-2:#2A2521; --surface:#211D1A;
  --ink:#F0EAE4; --ink-2:#B3A9A1; --ink-3:#8A807A;
  --rule:#332C27; --rule-2:#463D37;
  --shu:#E88B79; --gry:#A79E97; --aoi:#8CBBD3;
}}
*{{box-sizing:border-box}}
body{{background:var(--paper);color:var(--ink);
  font-family:"Meiryo UI","Meiryo","BIZ UDPGothic","Hiragino Kaku Gothic ProN",sans-serif;
  font-size:15px;line-height:1.75;-webkit-font-smoothing:antialiased}}
.wrap{{max-width:1120px;margin:0 auto;padding:38px 26px 72px;display:flex;flex-direction:column;gap:30px}}
h1{{font-family:"Meiryo","Meiryo UI","BIZ UDPGothic","Hiragino Kaku Gothic ProN",sans-serif;font-weight:700;
  font-size:clamp(25px,3.4vw,34px);line-height:1.25;margin:0 0 8px;text-wrap:balance}}
.sub{{margin:0;color:var(--ink-2);font-size:13.5px}}
.date{{font-size:12px;color:var(--ink-3);letter-spacing:.06em}}
.head{{display:flex;justify-content:space-between;align-items:flex-start;gap:20px;flex-wrap:wrap}}

.legend{{display:flex;flex-wrap:wrap;gap:10px 26px;padding:14px 18px;
  background:var(--surface);border:1px solid var(--rule);border-radius:3px}}
.li{{display:flex;align-items:center;gap:9px;font-size:12.5px;color:var(--ink-2)}}
.li b{{color:var(--ink);font-weight:700}}
.sw{{flex:none}}

section{{display:flex;flex-direction:column;gap:16px}}
.sh{{border-top:2px solid var(--ink);padding-top:12px}}
.sh h2{{font-family:"Meiryo","Meiryo UI","BIZ UDPGothic",sans-serif;font-weight:700;
  font-size:21px;margin:0 0 4px;letter-spacing:.01em}}
.sh p{{margin:0;color:var(--ink-2);font-size:13px}}

.fig{{margin:0;background:var(--surface);border:1px solid var(--rule);border-radius:3px;
  padding:16px 18px 14px;display:flex;flex-direction:column;gap:10px}}
.fh{{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}}
.tag{{font-size:11px;font-weight:700;letter-spacing:.06em;
  color:var(--ink-2);border:1px solid var(--rule-2);border-radius:2px;padding:2px 7px;white-space:nowrap}}
.fh h3{{font-family:"Meiryo","Meiryo UI","BIZ UDPGothic",sans-serif;font-weight:700;
  font-size:17px;margin:0;line-height:1.4}}
.svgwrap{{overflow-x:auto}}
svg{{display:block;width:100%;min-width:760px;height:auto}}
.nt{{font:700 13.5px "Meiryo","Meiryo UI","BIZ UDPGothic",sans-serif}}
.ns{{font:400 10.5px "Meiryo UI","Meiryo","BIZ UDPGothic",sans-serif}}
.al{{font:700 11.5px "Meiryo UI","Meiryo","BIZ UDPGothic",sans-serif}}
.lane{{font:700 12.5px "Meiryo","Meiryo UI","BIZ UDPGothic",sans-serif;fill:var(--ink)}}
.lane2{{font:400 10px "Meiryo UI","Meiryo","BIZ UDPGothic",sans-serif;fill:var(--ink-3)}}
.tie{{font:400 10.5px "Meiryo UI","Meiryo","BIZ UDPGothic",sans-serif}}
figcaption{{font-size:12.5px;color:var(--ink-2);border-top:1px solid var(--rule);padding-top:10px;margin:0}}
figcaption b{{color:var(--ink);font-weight:700}}
.close{{background:var(--paper-2);border-radius:3px;padding:16px 20px;font-size:13.5px;line-height:1.8}}
.close b{{font-weight:700}}
</style>

<div class="wrap">
  <header class="head">
    <div>
      <h1>日本酒混載輸出の商流と物流</h1>
      <p class="sub">シンガポール向け 4〜5蔵の混載輸出／theSFC案件　　前提：当社は大和川・天鏡をtheSFCへ販売する</p>
    </div>
    <span class="date">26-09-01</span>
  </header>

  <div class="legend">
    <span class="li"><svg class="sw" width="34" height="12" aria-hidden="true"><line x1="0" y1="6" x2="24" y2="6" stroke="var(--shu)" stroke-width="2"/><polygon points="34,6 24,1.5 24,10.5" fill="var(--shu)"/></svg><b>商流：当社が入る</b></span>
    <span class="li"><svg class="sw" width="34" height="12" aria-hidden="true"><line x1="0" y1="6" x2="24" y2="6" stroke="var(--gry)" stroke-width="2"/><polygon points="34,6 24,1.5 24,10.5" fill="var(--gry)"/></svg><b>商流：当社が入らない</b></span>
    <span class="li"><svg class="sw" width="34" height="12" aria-hidden="true"><line x1="0" y1="6" x2="24" y2="6" stroke="var(--aoi)" stroke-width="2" stroke-dasharray="6 4"/><polygon points="34,6 24,1.5 24,10.5" fill="var(--aoi)"/></svg><b>物流</b></span>
    <span class="li"><svg class="sw" width="24" height="14" aria-hidden="true"><rect x="1" y="1" width="22" height="12" fill="var(--surface)" stroke="var(--rule)" stroke-dasharray="4 3"/></svg>薄い枠と薄い矢印＝まだ決まっていない</span>
    <span class="li"><svg class="sw" width="24" height="14" aria-hidden="true"><rect x="1" y="1" width="22" height="12" fill="var(--ink)"/></svg>塗り＝その案で変わるところ</span>
  </div>

  <section>
    <div class="sh">
      <h2>読みA　shipper ＝ 荷主（輸出者）</h2>
      <p>先方が求めているのは「4〜5蔵を束ねて自ら売り、輸出者になる会社」という読み</p>
    </div>
    {fig("a_asis","AS-IS　現状","当社分は立つが、他社蔵が立たない",
      "大和川・天鏡は当社が売るので、商流も輸出者も決まっている。決まっていないのは<b>他社蔵2〜3社の分</b>で、各蔵が自ら輸出者を務めることになるが引き受け手がいない。商流が決まらないので、束ねるフォワーダーも決まらない。",
      "商流は当社経由の1本だけが成立し、他社蔵からの商流は輸出者が決まらず未成立。物流も未確定")}
    {fig("a_tobe","TO-BE　読みAへの答え","当社が4〜5蔵すべてを束ねる",
      "他社蔵の分も当社が仕入れて売る。<b>商流が1本になり、輸出申告も1本になる。</b>先方が求める「束ねる輸出者」を当社が務める形。当社は他社蔵の仕入口座と与信を持つことになる。",
      "全ての蔵が新日本海商事を経由し、商流1本・輸出申告1本にまとまる")}
  </section>

  <section>
    <div class="sh">
      <h2>読みB　shipper ＝ フォワーダー（物流手配者）</h2>
      <p>先方が求めているのは「4〜5蔵から集荷して混載し、輸出通関を代行する物流会社」という読み</p>
    </div>
    {fig("b_asis","AS-IS　現状","商流は立つが、運賃が高い",
      "大和川・天鏡は当社経由、他社蔵はtheSFCへ直。<b>商流はどちらも成立しうる。</b>詰まっているのは物流で、手が挙がるのが定温リーファー定期便を持つ1社だけ。その見積が高い。",
      "商流は当社経由と他社蔵直の2系統が成立。物流は高い1社しか選択肢がない")}
    {fig("b_tobe","TO-BE　読みBへの答え","物流だけ束ね直す",
      "商流はAS-ISのまま動かさず、相見積で選び直したフォワーダーが集荷・混載する。運賃は下がるが、<b>商流が分かれている以上、輸出申告は当社1本＋各蔵2〜3本のまま残る。</b>",
      "商流はAS-ISと同じまま、フォワーダーだけが入れ替わる。輸出申告の本数は変わらない")}
  </section>

  <p class="close"><b>2つの読みの違いは、当社が何を背負うか。</b>　読みAなら、当社が大和川・天鏡で既にやっていることを他社蔵まで広げる話になり、仕入口座と与信を新たに持つ。読みBなら当社が新たに背負うものはないが、蔵側の輸出者負担は残ったままになる。<b>どちらの読みかは「各蔵への商品代金を誰が払う想定か」を聞けば1問で確定する。</b></p>
</div>
'''

open("flow.html","w",encoding="utf-8").write(PAGE)
print("ok", len(PAGE))
