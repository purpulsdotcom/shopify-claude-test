"""Generate the 3 Blessed Friday emails (email-safe HTML for Shopify Email's
"Custom Liquid" section). Run: python3 blessed-friday/build_emails.py"""
from pathlib import Path

OUT = Path(__file__).parent / "emails"
OUT.mkdir(exist_ok=True)

CDN = "https://cdn.shopify.com/s/files/1/0777/0688/7406/files/"
IMG = {
    "hero": CDN + "ChatGPT_Image_Jun_19_2026_01_29_17_AM.webp?v=1781815154&width=1200",
    "box": CDN + "pomelli_photoshoot_image_1_1_0511.webp?v=1778498235&width=600",
    "silver_purple": CDN + "ChatGPT_Image_Jun_19_2026_01_29_58_AM.webp?v=1781815154&width=600",
    "silver_pink": CDN + "pomelli_photoshoot_image_1_1_0625_4.webp?v=1782401708&width=600",
    "aqua": CDN + "Aquamarine_Vine_Bracelet_on_Ivory_Silk.webp?v=1792075032&width=600",
    "lifestyle": CDN + "pomelli_photoshoot_image_1_1_0509_1.webp?v=1778276953&width=600",
}
SITE = "https://www.purpuls.com"
DEAL = SITE + "/products/tulip-bracelet-bundle-deal-any-2-for-rs-1-899"
BOX = SITE + "/products/premium-gift-box"
COLLECTION = SITE + "/collections/tulip-collection"

# Palette: night plum + antique gold + ivory (Purpuls purple, luxe gifting)
INK, PLUM, GOLD, IVORY, CREAM, MUTED = "#1c1020", "#2a1530", "#c9a24a", "#fbf7f1", "#f3ece2", "#6b5d70"
SERIF = "'Cormorant Garamond', Georgia, 'Times New Roman', serif"
SANS = "'Helvetica Neue', Helvetica, Arial, sans-serif"


def link(url, content):
    sep = "&" if "?" in url else "?"
    return f"{url}{sep}utm_source=shopify_email&utm_medium=email&utm_campaign=blessed_friday_26&utm_content={content}"


def button(url, label, content, dark=False):
    bg, fg = (INK, IVORY) if dark else (GOLD, INK)
    return f"""<table role="presentation" cellpadding="0" cellspacing="0" border="0" align="center"><tr>
<td align="center" bgcolor="{bg}" style="border-radius:999px;">
<a href="{link(url, content)}" target="_blank" style="display:inline-block;padding:16px 38px;font-family:{SANS};font-size:15px;font-weight:700;letter-spacing:0.5px;color:{fg};text-decoration:none;border-radius:999px;">{label}</a>
</td></tr></table>"""


def eyebrow(text, color=GOLD):
    return f'<p style="margin:0 0 14px;font-family:{SANS};font-size:11px;letter-spacing:4px;text-transform:uppercase;color:{color};font-weight:700;">{text}</p>'


def receipt(tag):
    row = lambda l, r, bold=False: f"""<tr>
<td style="padding:10px 0;font-family:{SANS};font-size:14px;color:{INK};{'font-weight:700;' if bold else ''}border-bottom:1px dashed #d9cdbb;">{l}</td>
<td align="right" style="padding:10px 0;font-family:{SANS};font-size:14px;color:{INK};{'font-weight:700;' if bold else ''}border-bottom:1px dashed #d9cdbb;">{r}</td></tr>"""
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{IVORY};border:1px solid #e8dcc8;border-radius:16px;">
<tr><td style="padding:22px 26px 8px;">{eyebrow('Your Blessed Friday order')}
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
{row('2 × Tulip Bracelet <span style="color:%s;">(any colours)</span>' % MUTED, 'Rs 1,899')}
{row('Premium Gift Box', f'<span style="text-decoration:line-through;color:{MUTED};">Rs 299</span>&nbsp; <span style="color:#a2311f;font-weight:700;">Rs 100</span>')}
<tr><td style="padding:14px 0 6px;font-family:{SERIF};font-size:24px;color:{INK};font-weight:700;">Total</td>
<td align="right" style="padding:14px 0 6px;font-family:{SERIF};font-size:24px;color:{INK};font-weight:700;">Rs 1,999</td></tr>
</table>
<p style="margin:4px 0 18px;font-family:{SANS};font-size:12px;color:{MUTED};">No code needed &middot; the box drops to Rs 100 automatically at checkout &middot; Cash on Delivery</p>
</td></tr></table>"""


def steps():
    cell = lambda n, t, s: f"""<td width="33%" valign="top" align="center" style="padding:0 6px;">
<div style="font-family:{SERIF};font-size:30px;color:{GOLD};line-height:1;">{n}</div>
<p style="margin:8px 0 4px;font-family:{SANS};font-size:13px;font-weight:700;color:{INK};">{t}</p>
<p style="margin:0;font-family:{SANS};font-size:12px;line-height:1.5;color:{MUTED};">{s}</p></td>"""
    return f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
{cell('1', 'Pick 2 colours', 'Any 2 from 10 shades, mix or match.')}
{cell('2', 'Add the Premium Box', f'<a href="{link(BOX, "steps_box")}" style="color:{INK};">Add it to your cart</a> with your pair.')}
{cell('3', 'Pay Rs 100 for it', 'Discount applies at checkout. COD available.')}
</tr></table>"""


def grid(items, prefix):
    cells = []
    for img, label, sub in items:
        cells.append(f"""<td width="50%" valign="top" style="padding:6px;">
<a href="{link(DEAL, prefix + '_' + label.lower().replace(' ', '_').replace('+', ''))}" target="_blank" style="text-decoration:none;">
<img src="{IMG[img]}" width="264" alt="{label} Tulip bracelet" style="display:block;width:100%;max-width:264px;height:auto;border-radius:14px;border:0;">
<p style="margin:10px 0 2px;font-family:{SANS};font-size:13px;font-weight:700;color:{INK};">{label}</p>
<p style="margin:0;font-family:{SANS};font-size:12px;color:{MUTED};">{sub}</p></a></td>""")
    rows = "".join(f"<tr>{cells[i]}{cells[i + 1]}</tr>" for i in range(0, len(cells), 2))
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">{rows}</table>'


def trust():
    items = ["15K+ happy customers", "Cash on Delivery", "14-day returns", "2-year colour warranty"]
    tds = "".join(f'<td align="center" style="padding:6px 4px;font-family:{SANS};font-size:11px;letter-spacing:0.5px;color:{CREAM};">&#10022;&nbsp;{t}</td>' for t in items)
    return f'<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>{tds}</tr></table>'


def shell(preheader, hero_block, body_blocks, footer_note):
    body = "".join(f'<tr><td style="padding:{pad};background:{bg};">{html}</td></tr>' for pad, bg, html in body_blocks)
    return f"""<!-- Purpuls · Blessed Friday 2026 · paste into Shopify Email > Custom Liquid section -->
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,600;1,500&display=swap" rel="stylesheet">
<div style="display:none;max-height:0;overflow:hidden;opacity:0;color:transparent;">{preheader}&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;&#8199;&#65279;&#847;</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background:{CREAM};">
<tr><td align="center" style="padding:0;">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0" style="width:100%;max-width:600px;background:{IVORY};">
<tr><td align="center" style="padding:16px 24px;background:{INK};">
<p style="margin:0;font-family:{SANS};font-size:11px;letter-spacing:5px;color:{GOLD};font-weight:700;">GEMZ BY PURPULS</p></td></tr>
{hero_block}
{body}
<tr><td align="center" style="padding:22px 24px;background:{INK};">{trust()}
<p style="margin:14px 0 0;font-family:{SANS};font-size:11px;line-height:1.6;color:#9d8fa3;">{footer_note}</p></td></tr>
</table></td></tr></table>"""


def hero(eyebrow_txt, h1, sub, cta, cta_key, countdown):
    return f"""<tr><td align="center" style="padding:44px 32px 0;background:{PLUM};">
{eyebrow(eyebrow_txt)}
<h1 style="margin:0 0 16px;font-family:{SERIF};font-size:40px;line-height:1.08;font-weight:600;color:{IVORY};">{h1}</h1>
<p style="margin:0 auto 26px;max-width:460px;font-family:{SANS};font-size:15px;line-height:1.6;color:#e4d9e8;">{sub}</p>
{button(DEAL, cta, cta_key)}
<p style="margin:14px 0 30px;font-family:{SANS};font-size:12px;letter-spacing:1px;color:{GOLD};">{countdown}</p>
<a href="{link(DEAL, cta_key + '_img')}" target="_blank"><img src="{IMG['hero']}" width="536" alt="Luminous gold-plated crystal Tulip bracelet in its gift box" style="display:block;width:100%;max-width:536px;height:auto;border-radius:18px 18px 0 0;border:0;"></a>
</td></tr>"""


ENDS = "Ends Monday 30 Nov &middot; 11:59 PM"
FOOT = "Offer: buy 2 Tulip bracelets from the Pair Deal and get the Premium Gift Box (Rs 299) for Rs 100. One box per order. Valid until 30 Nov 2026, 11:59 PM PKT, while stocks last."
GRID_ALL = [
    ("silver_purple", "Silver + Purple", "Cool-toned and elegant"),
    ("silver_pink", "Silver + Pink", "Soft, everyday sparkle"),
    ("hero", "The viral original", "The one from our videos"),
    ("lifestyle", "10 shades to mix", "Pink, Blue, Green, White &amp; more"),
]

EMAILS = {
    "email-1-launch.html": dict(
        pre="2 Tulip bracelets + the Premium Box everyone asks about. Box drops to Rs 100 till Monday.",
        hero=hero("Blessed Friday &middot; 27&ndash;30 Nov",
                  "The box everyone asks about.<br><em style=\"color:%s;\">Rs 100 this weekend.</em>" % GOLD,
                  "Pick any 2 Tulip bracelets and our Rs 299 Premium Gift Box is yours for Rs 100. It drops automatically at checkout, no code needed.",
                  "Claim my Rs 100 box &rarr;", "e1_hero", ENDS),
        body=[
            ("32px 32px 8px", IVORY, receipt("e1")),
            ("26px 24px 6px", IVORY, steps()),
            ("30px 26px 4px", IVORY, f'<p style="margin:0;text-align:center;font-family:{SERIF};font-size:28px;color:{INK};">Pick your pair</p>'),
            ("10px 26px 10px", IVORY, grid(GRID_ALL, "e1_grid")),
            ("10px 32px 40px", IVORY, button(DEAL, "Shop the Pair Deal", "e1_bottom", dark=True)
             + f'<p style="margin:16px 0 0;text-align:center;font-family:{SANS};font-size:13px;"><a href="{link(COLLECTION, "e1_collection")}" style="color:{MUTED};">Or browse the full Tulip Collection</a></p>'),
        ]),
    "email-2-colour-guide.html": dict(
        pre="Our most-gifted Tulip pairs, plus your Rs 100 box. 2 days left.",
        hero=hero("Blessed Friday &middot; 2 days left",
                  "Can&rsquo;t pick 2 colours?<br><em style=\"color:%s;\">Here&rsquo;s the cheat sheet.</em>" % GOLD,
                  "Ten shades, one pair. If you&rsquo;re stuck, start with one of our favourite combos below. The Premium Box is still just Rs 100.",
                  "Shop the pairs &rarr;", "e2_hero", ENDS),
        body=[
            ("34px 26px 4px", IVORY, f'<p style="margin:0 0 4px;text-align:center;font-family:{SERIF};font-size:28px;color:{INK};">Our favourite combos</p>'
             f'<p style="margin:0;text-align:center;font-family:{SANS};font-size:13px;color:{MUTED};">Tap any colour to start your pair</p>'),
            ("12px 26px 10px", IVORY, grid([
                ("silver_purple", "Silver + Purple", "Pair it with Silver + Pink"),
                ("silver_pink", "Silver + Pink", "Soft, everyday sparkle"),
                ("hero", "The viral original", "Pair it with Purple"),
                ("lifestyle", "One for you, one for her", "Same colour, matching wrists"),
            ], "e2_grid")),
            ("14px 32px 8px", IVORY, receipt("e2")),
            ("22px 32px 40px", IVORY, button(DEAL, "Build my pair", "e2_bottom", dark=True)),
        ]),
    "email-3-last-chance.html": dict(
        pre="Tonight at 11:59 PM the Premium Box goes back to Rs 299.",
        hero=hero("Last chance &middot; ends tonight",
                  "At midnight, your box<br><em style=\"color:%s;\">goes back to Rs 299.</em>" % GOLD,
                  "This is the last email about it. Pick 2 Tulip bracelets before 11:59 PM and the Premium Gift Box is Rs 100. After that, Blessed Friday is over.",
                  "Get it before midnight &rarr;", "e3_hero", "Ends tonight &middot; 30 Nov &middot; 11:59 PM PKT"),
        body=[
            ("32px 32px 8px", IVORY, receipt("e3")),
            ("22px 32px 10px", IVORY, f"""<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr>
<td width="44%" valign="middle" style="padding-right:16px;"><img src="{IMG['box']}" width="230" alt="Purpuls Premium Gift Box" style="display:block;width:100%;max-width:230px;height:auto;border-radius:14px;border:0;"></td>
<td valign="middle"><p style="margin:0 0 6px;font-family:{SERIF};font-size:24px;color:{INK};">Gift-ready, the moment it arrives.</p>
<p style="margin:0;font-family:{SANS};font-size:13px;line-height:1.6;color:{MUTED};">The Premium Box is the one from our videos. Tonight it&rsquo;s Rs 100 with any 2 Tulips. Tomorrow it&rsquo;s Rs 299.</p></td></tr></table>"""),
            ("26px 32px 40px", IVORY, button(DEAL, "Claim it now", "e3_bottom", dark=True)),
        ]),
}

for name, e in EMAILS.items():
    (OUT / name).write_text(shell(e["pre"], e["hero"], e["body"], FOOT), encoding="utf-8")
    print("wrote", OUT / name)
