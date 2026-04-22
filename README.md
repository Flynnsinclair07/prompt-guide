# snipprompts.com

Programmatic SEO affiliate site — 134 "best ChatGPT prompt for [X]" pages across career, business, marketing, finance, and lifestyle.

## Stack
- Static HTML hosted on GitHub Pages (custom domain, HTTPS enforced)
- No framework, no CMS
- Ezoic (pending), Amazon Associates, ConvertKit email capture
- GA4 + Search Console + Bing Webmaster verified

## Structure
```
/                              # homepage, categories, legal
/prompts/                      # 134 prompt pages
/pins/                         # Pinterest pin assets (1000x1500 PNGs)
/product/                      # paid-product outlines (see job-hunter-bundle-outline.md)
/tracking/                     # daily metrics template + log
```

## Daily tracking

**Google Sheet**: https://docs.google.com/spreadsheets/d/1EVB7aO54xTPfZBe9BO7FmU1d5E7wd3xvGaPFAy-t2ak/edit

Create the sheet at [sheets.new](https://sheets.new) with these exact column headers (copy from `tracking/daily-metrics-template.csv`):

```
Date | Product sales | Gumroad revenue | Email subs | Pinterest impressions | Pinterest saves | Pinterest outbound clicks | YouTube subs | YouTube views | Hours worked | Notes
```

One row per day. Fill in at end of day. The CSV template in `tracking/` has today's baseline row.

## Traffic-waiting-phase rules (until 100+ monthly organic visitors)

- **Search Console**: check at most 1×/day. Do not obsess.
- **Watch for**: first impressions → first query list → 100+ monthly visitors (this is the trigger to reapply to Impact.com + FlexOffers).
- **FlexOffers**: declined on first application. Reapply when traffic threshold hits.
- **Amazon Associates**: 180-day qualifying clock running. Tax interview pending on SSN.
- **Phase 2 content** (expanding beyond the 134 pages): paused until Search Console shows which pages actually get impressions. Don't write speculatively.
