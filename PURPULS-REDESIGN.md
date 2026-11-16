# Purpuls: conversion redesign (theme "Purpuls Jewels — Conversion redesign")

Built inside the real Purpuls store (purpuls.com) as an **unpublished** copy of the live
"Blessed Friday Sale (Nov 16–30)" theme. All products, collections, offers, apps, reviews and settings carry over.

## What the order data showed (last ~100 orders, Nov 15)
- Average order value ≈ Rs 1,700.
- About 40% of orders are a **single item** (mostly Rs 1,198).
- Your main offer, **Buy 2 Get 1 Free** (automatic, 141 published products in `buy-2-get-1-free`), only triggers at 3 items. Nothing in the old theme told a 1- or 2-item buyer how close they were.

## What changed
| Where | Change | Goal |
|---|---|---|
| Cart drawer | Buy 2 Get 1 progress: 3 dots (1 · 2 · FREE) plus "Add 1 more piece and it's FREE 🎁" and a link to eligible pieces. Toggle and collection picker in the cart drawer section settings. | Turn 1–2 item carts into 3 items |
| Product page | "Buy any 2, get the 3rd FREE" callout next to the price, shown only on eligible products | Plant the offer before add-to-cart |
| Product cards | "Buy 2 Get 1" chip on eligible products everywhere (collections, rails, search) | Fast decisions while browsing |

Unchanged: Blessed Friday announcement and deals, free delivery from Rs 3,499, gift-box add-ons, delivery estimate, sticky add to bag, reviews, WhatsApp.

Files: `snippets/tf-b2g1.liquid`, `snippets/tf-b2g1-style.liquid`, `sections/tf-cart-drawer.liquid`, `sections/tf-product.liquid`, `snippets/tf-card.liquid`.

## Publish checklist (after Blessed Friday, Nov 30)
1. Online Store → Themes → "Purpuls Jewels — Conversion redesign" → **Preview**. Add 1, 2 and then 3 eligible items and check that the cart message changes each time and that the free item applies at checkout.
2. If Blessed Friday has ended, change the header announcement (Theme editor → Header → Announcement).
3. Publish.
4. Delete the leftover theme "DELETE ME — duplicate copy (unused)" and the separate preview store "My Store", which is no longer needed.

## Metrics to watch (compare the 7 days before and after publishing)
- Share of single-item orders: target below 30% (now about 40%).
- Items per order: target 2.2+.
- AOV: target Rs 2,100+ (now about Rs 1,700).
