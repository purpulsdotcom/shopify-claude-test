# Purpuls · Blessed Friday 2026: Flow email sequence

## The offer (already live in the store)
Automatic discount **"Blessed Friday — Premium Box for Rs 100 with any 2 Tulips"**
- Buy 2 × **Tulip Bracelet — Pair Deal** (Rs 949.50 each = **Rs 1,899** for the pair)
- **Premium Gift Box** Rs 299 → **Rs 100** (Rs 199 off, one box per order)
- Runs until **30 Nov 2026, 11:59 PM PKT**. No code needed, but the customer has to **add the box to their cart themselves**.

Email hook: **2 Tulips + the Premium Box = Rs 1,999**, with the box crossed out from Rs 299 to Rs 100.

## Landing page: the Pair Deal product page
`https://www.purpuls.com/products/tulip-bracelet-bundle-deal-any-2-for-rs-1-899`

Why this page:
- It's the only page where the Blessed Friday offer actually applies, so one click takes the reader from email to offer.
- It covers the Tulip bracelet, which is your biggest line by stock and sits at the top of both the Viral Sale and Tulip collections.
- It's **unlisted**, so only email and ad traffic can see it, which makes the deal feel exclusive.
- Secondary link: `/collections/tulip-collection` for readers who want to browse.

**Check before sending:** the email tells people to add the Premium Box themselves. If the Pair Deal page has no "Add Premium Box" upsell, add one with a product add-on or bundle block, or link `/products/premium-gift-box` near the add-to-cart button. Otherwise people will miss the Rs 100 box.

## Flow architecture

```
[1] BF26 · Tag buyers          (Shopify Flow, turn on NOW)
    Order created
      └─ if any line item product.handle == "tulip-bracelet-bundle-deal-any-2-for-rs-1-899"
           └─ Add customer tags: bf26-bought

[2] BF26 · Email sequence      (Marketing > Automations, opens in the Flow editor)
    Customer joined segment "BF26 · Subscribers"
      ├─ Send marketing email: E1 Launch                     Fri 27 Nov, ~10 AM
      ├─ Wait 34 hours
      ├─ if customer tags does NOT contain "bf26-bought"
      │    └─ Send marketing email: E2 Colour guide          Sat 28 Nov, ~8 PM
      ├─ Wait 46 hours
      └─ if customer tags does NOT contain "bf26-bought"
           └─ Send marketing email: E3 Last chance           Mon 30 Nov, ~6 PM

[3] Kickoff (manual, Fri 27 Nov, 10 AM)
    Customers > segment "Email subscribers" > select all > Add tags: bf26
    → everyone joins "BF26 · Subscribers" → workflow [2] starts for each of them
```

Buyers stop getting emails as soon as they order, so nobody is chased after they've already bought.

## Build steps

### 1. Segment
Customers → Segments → Create segment → name **BF26 · Subscribers**
```
email_subscription_status = 'SUBSCRIBED' AND customer_tags CONTAINS 'bf26'
```

### 2. Workflow 1: tag buyers (Apps → Flow → Create workflow)
1. Trigger: **Order created**
2. Condition: **Order / Line items / Product / Handle** → *at least one of* → *is equal to* `tulip-bracelet-bundle-deal-any-2-for-rs-1-899`
3. Then: **Add customer tags** → `bf26-bought`
4. Name it **BF26 · Tag buyers** and turn it on **now**, so it also catches people who buy before the emails go out.

### 3. Workflow 2: email sequence (Marketing → Automations → Create automation → Create custom automation)
1. Trigger: **Customer joined segment** → *BF26 · Subscribers*
2. Action: **Send marketing email** → Edit email:
   - Subject and preview text: see the table below
   - Delete the default sections → **Add section → Custom Liquid** → paste the whole contents of `emails/email-1-launch.html`
   - Send yourself a test and check it on a phone (Gmail app) before saving.
3. **Wait** → 34 hours
4. **Condition** → Customer / Tags → *does not include* → `bf26-bought`
5. Then (true branch): **Send marketing email** → paste `emails/email-2-colour-guide.html`
6. **Wait** → 46 hours
7. **Condition** → Customer / Tags → *does not include* → `bf26-bought`
8. Then: **Send marketing email** → paste `emails/email-3-last-chance.html`
9. Name it **BF26 · Email sequence** and turn it on before the kickoff.

### 4. Kickoff (Fri 27 Nov, 10 AM PKT)
Customers → open segment **Email subscribers** → select all → **More actions → Add tags** → `bf26`.

The segment trigger can take a little while to pick up new members, so tag at about 9:30 AM if you want E1 out by 10.

### 5. Clean-up (1 Dec)
Turn off both workflows. Optionally bulk-remove the `bf26` tag so the same setup can be reused next year.

## Emails

| # | When | Subject | Preview text | Goes to |
|---|---|---|---|---|
| E1 | Fri 27 Nov, 10 AM | Your Blessed Friday gift costs Rs 100 🎀 | 2 Tulip bracelets + the Premium Box everyone asks about. Box drops to Rs 100 till Monday. | All subscribers |
| E2 | Sat 28 Nov, ~8 PM | Can't decide which 2 Tulips? 💜 | Our favourite Tulip pairs, plus your Rs 100 box. 2 days left. | Non-buyers |
| E3 | Mon 30 Nov, ~6 PM | ⏳ Your Rs 100 box expires at midnight | Tonight at 11:59 PM the Premium Box goes back to Rs 299. | Non-buyers |

Alternative subject lines to A/B test on E1:
- `Rs 299 → Rs 100. Blessed Friday is here.`
- `Pick 2 Tulips. We'll handle the gift box. 🎁`

Design: night plum and antique-gold hero with a serif headline (Cormorant Garamond, falling back to Georgia), an ivory "receipt" block that spells out the Rs 1,999 total, 3 steps, a 2×2 colour grid, and a trust bar (15K+ customers, COD, 14-day returns, 2-year colour warranty). Every link carries `utm_campaign=blessed_friday_26` with a `utm_content` per button, so you can see in Analytics which button sold.

To edit the copy, change `build_emails.py` and run `python3 build_emails.py`. That regenerates all 3 HTML files.

## Things to check before launch
1. **Compare-at price on the Pair Deal:** each variant has a compare-at of **Rs 3,299** against Rs 949.50, which shows as about 71% off per bracelet. That doesn't look like a real former price. The emails don't use it, but the product page shows it. Under Pakistan's consumer-protection rules a made-up "was" price is a risk, so set it to an honest figure (for example Rs 999, the single-bracelet price).
2. **The "Viral Sale — Up to 70% / 50% Off" collections** have no compare-at prices on their products, so the "% off" claims can't be backed up. Better not to promote them in Blessed Friday emails.
3. **Overlapping discounts:** "Buy 2 Get 1 Free" is also active. Test a cart with 2 Pair Deal bracelets + Premium Box and check the total really comes to Rs 1,999.
4. **Email volume and cost:** you have 10,000+ customers. Three emails could be 20–30k sends. The Basic plan includes a monthly allowance of free Shopify Email sends, and anything above it is billed per 1,000. Check Settings → Billing.
5. Product images are served as `.webp` from the Shopify CDN. They display in Gmail, Apple Mail and Outlook web, but older Outlook desktop shows the alt text instead.
