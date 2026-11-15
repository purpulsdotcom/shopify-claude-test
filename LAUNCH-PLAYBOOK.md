# Purpuls Jewels: launch playbook

Brand direction: **modern everyday jewelry** for young women (18–30), gift buyers and premium-minded shoppers. Price band PKR 500–3,000. Market: Pakistan, PKR, Cash on Delivery first.

## What is already built in the preview store

| Area | Done |
|---|---|
| Products | 12 sample products with prices, compare-at prices, descriptions and SKUs. Replace the photos with your own. |
| Collections | Earrings, Necklaces, Rings, Bracelets, Complete the Set, Under PKR 1,000, Gifts for Her, Best Sellers, New In, Studs. All update automatically from product **tags**. |
| Navigation | New In · Shop (Earrings / Necklaces / Rings / Bracelets) · Sets & Bundles · Under PKR 1,000 · Gifts · Best Sellers |
| Theme | Homepage, product page and cart built for fast decisions and trust (see the design notes in the theme's `DESIGN.md`). |

### Tags that drive the collections
`earrings` `necklaces` `rings` `bracelets` `sets` `studs` `gift` `best-seller` `new` `add-on` (the add-on tag keeps the gift box out of the shopping collections).
Under PKR 1,000 is price-based and needs no tag.

## Step 1: Claim the store (5 min)
Open the save link Claude gave you and save the store to your Shopify account. Until then it is password-locked, and anyone with its address can edit it.

## Step 2: Create the offers (10 min)
Shopify admin → **Discounts → Create discount**. The theme already advertises these offers, so create **all of them before launch**.

| # | Type | Name / code | Settings | Combines with |
|---|---|---|---|---|
| 1 | Free shipping, Automatic | Free delivery over PKR 2,500 | Minimum purchase PKR 2,500, all countries | Product + order discounts |
| 2 | Amount off order, Automatic | Buy 2, save 10% | 10%, minimum quantity 2 | Shipping only |
| 3 | Amount off order, Automatic | Buy 3+, save 15% | 15%, minimum quantity 3 (Shopify applies whichever of #2 or #3 is better) | Shipping only |
| 4 | Buy X get Y, Automatic | Studs: buy 2, get 1 free | Buys 2 from the *Studs* collection, gets 1 from *Studs* free, max 3 uses per order | Shipping + order |
| 5 | Buy X get Y, Automatic | Free gift box over PKR 3,500 | Minimum purchase PKR 3,500, gets *Signature Gift Box* 100% off, 1 per order | All |
| 6 | Amount off order, Code | `WELCOME10` | 10%, once per customer. Give it out via the WhatsApp/Instagram sign-up. | Shipping |

**Why these numbers:** with pieces at PKR 590–2,790, a typical single-item cart is about PKR 1,200–1,500.
- The free-delivery goal at PKR 2,500 nudges shoppers to a second piece.
- The PKR 3,500 gift tier nudges them to a third.
- Buy 2/Buy 3 rewards items per order directly.

## Step 3: Payments and shipping (1–5 days, outside parties)
- **Cash on Delivery:** Settings → Payments → Manual payment methods → *Cash on Delivery*. Works the same day.
- **Cards / JazzCash / Easypaisa:** apply with a local gateway (e.g. Safepay or PayFast). Approval usually takes a few days.
- **Courier:** connect PostEx, Trax or Leopards (Shopify apps) for COD remittance and tracking.
- **Shipping rates:** flat PKR 200 nationwide. Free delivery comes from offer #1.
- **Policies:** Settings → Policies. Paste the refund and shipping text below.

**Refund policy:**
> 7-day easy exchange. Not in love? Message us on WhatsApp within 7 days of delivery and we'll exchange your piece. Items must be unworn and in original packaging. Earrings can only be exchanged if faulty, for hygiene reasons.

**Shipping policy:**
> Nationwide delivery across Pakistan in 2–5 working days. Cash on Delivery available everywhere. Free delivery on orders over PKR 2,500; flat PKR 200 below that.

## Step 4: Checkout speed (15 min)
Settings → Checkout:
- One-page checkout (default), **phone number required**, company name and address line 2 **hidden**, address autocomplete **on**.
- Turn on **Shop Pay** once cards are approved.
- Order notes **on**, labelled "Gift message (optional)".

## Step 5: Apps (keep it to 5 or fewer for speed)
| Need | App |
|---|---|
| Bundles | Shopify Bundles (free) |
| Search & filters | Shopify Search & Discovery (free); also use it for "Complete the look" recommendations |
| Reviews with photos | Judge.me (free plan) |
| WhatsApp chat + abandoned-cart recovery | a WhatsApp app (e.g. WhatsApp chat + cart recovery) |
| Courier | PostEx / Trax / Leopards |

## Step 6: Content you must supply
- Real product photos: one on white, one being worn, one close-up, plus a short video if you can. **Photos are the biggest single factor in conversion.**
- Logo (SVG/PNG), your WhatsApp number, Instagram handle.
- Exact materials (plated / silver / stainless), sizes, and stock counts.

## Launch day: the numbers to watch
| Metric | Target |
|---|---|
| Mobile conversion rate | 1.5–3% |
| Average order value (AOV) | above PKR 2,000, rising towards the PKR 2,500 free-shipping goal |
| Items per order | 2.0+ |
| Reached checkout → order | ≥ 50% |
| COD return / refusal rate | < 15%. Confirm every COD order by WhatsApp before dispatch. |

## Weeks 2–4: optimise
1. If most carts sit just below PKR 2,500, the goal is working. If they sit far below it, lower the goal to PKR 2,000.
2. Swap the Best Sellers tag onto whatever actually sells.
3. Test a prepaid incentive (e.g. PKR 100 off for card payments) to reduce COD refusals.
4. Retarget cart abandoners on Meta and TikTok with the "Buy 2, save 10%" message.
