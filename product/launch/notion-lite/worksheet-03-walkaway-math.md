# Worksheet 3 — Walkaway math / benefit-equivalency calculator

> **Notion paste + FORMULA fields**: this is the highest-value Notion deliverable in the bundle. Convert to a Notion database with formula fields that auto-calculate total comparable comp.
>
> **Database setup:**
> 1. Create a new Notion database (table view) called "Offer Comparison"
> 2. Add columns:
>    - Offer name (Title)
>    - Base salary (Number, currency)
>    - Annual bonus target (Number, currency)
>    - Bonus probability (Number, percent)
>    - Sign-on bonus (Number, currency)
>    - Equity grant value (Number, currency)
>    - Vest years (Number)
>    - Risk discount % (Number, percent — based on stage per Step 2 below)
>    - PTO days (Number)
>    - Retirement match (Number, currency)
>    - Health subsidy (Number, currency)
>    - Learning budget (Number, currency)
>    - Commute cost (Number, currency, negative)
>    - Relo cost net (Number, currency, negative)
>    - **Total first-year comp** (Formula): = Base + (Bonus_target * Bonus_probability) + Signon + (Equity_grant_value * (1 - Risk_discount) / Vest_years) + (PTO * Base / 250) + Retirement_match + Health_subsidy + Learning_budget - Commute_cost - Relo_cost_net
>    - **Walkaway delta** (Formula): = Total_first_year_comp - your_walkaway_floor
> 3. Add one row per offer you're evaluating
> 4. Sort by Total first-year comp descending — top row is your best offer on cash
>
> The reference content below explains each component.

---

## Worksheet 3 — Walkaway math / benefit-equivalency calculator

**Purpose**: convert a full offer package into a single comparable number so you can (a) compare offers apples-to-apples, (b) stress-test against your walkaway floor, (c) evaluate trade-offs between components.

**Step 1 — cash components (straightforward dollars)**:

```
Base salary (annual):                        $[        ]
Annual bonus target (% of base × probability):
    Target $ × typical-hit-rate of [80–100%] = $[        ]
Sign-on bonus (pro-rate over expected
    tenure if you plan to stay 2+ years, or
    count in full if short-tenure expected):  $[        ]

Cash subtotal:                                $[        ]
```

**Step 2 — equity (the illiquid and probabilistic component)**:

For RSUs at a public company:
```
RSU grant dollar value ÷ vest years:          $[        ] / year
```

For RSUs at a late-stage private:
```
(Grant value × discount for illiquidity) ÷ vest years = $[   ] / year
(Discount typically 20–40% depending on company runway)
```

For ISOs/NSOs at a startup:
```
(Grant value AT CURRENT 409A × discount for
 risk-adjusted probability of exit × years
 to likely liquidity) ÷ vest years = $[        ] / year

Discount ranges:
- Seed/Series A: discount 70–90% (most fail)
- Series B–C: discount 50–70%
- Series D+: discount 20–40%

(These are honest risk-adjusted estimates, not
 recruiter-pitch numbers.)
```

**Step 3 — benefits and time**:

```
PTO (annual days × daily base rate):          $[        ]
    (Base ÷ 250 = daily rate; × PTO days)

Retirement match (up to annual cap):          $[        ]

Health insurance premium subsidy (annual
    company contribution):                    $[        ]

Learning / development budget:                $[        ]

Parental / family leave (if planning use in
    next 2 years, calculate paid leave value): $[        ]

Other benefits (home office, gym, food,
    commuter, etc.) — annual value:          $[        ]

Benefits subtotal:                            $[        ]
```

**Step 4 — costs and subtractions**:

```
Commute cost (if in-office — annual):         −$[        ]
Relocation cost (if relocating — not
    reimbursed portion, prorated):            −$[        ]
Cost-of-living difference from current
    location (if moving):                     ±$[        ]
Income tax difference (if moving to new
    state — ballpark):                        ±$[        ]

Costs subtotal:                               $[        ]
```

**Step 5 — total comparable value**:

```
TOTAL FIRST-YEAR COMP =
  Cash subtotal
+ Equity subtotal (first-year vest)
+ Benefits subtotal
− Costs subtotal
= $[        ]
```

**Step 6 — compare to your walkaway**:

```
My walkaway total comp (what I said I would not go below): $[      ]

Offer total: $[      ]

Gap: $[ + / − ]

Decision rule:
- Offer > walkaway by 10%+: strong offer, accept or close with minor
  asks
- Offer 0–10% above walkaway: acceptable, consider accepting
- Offer at walkaway: accept if non-comp factors (role, team, mission)
  are strong; decline if they're neutral
- Offer below walkaway: counter firmly or walk; do not rationalize
  accepting below your stated floor
```

**Step 7 — comparing two offers** (if you have multiple):

Run Steps 1–5 for each offer side-by-side. Don't compare on base alone; compare on total comparable value.

Second comparison — non-comp factors (check all that apply):

```
Factor                         Offer A | Offer B
-----------------------------------------
Role interest / scope            [ / ]
Team / manager quality           [ / ]
Company trajectory / stage       [ / ]
Learning opportunity             [ / ]
Career path / advancement        [ / ]
Work-life balance                [ / ]
Flexibility (remote, schedule)   [ / ]
Risk / stability                 [ / ]
Brand / resume value             [ / ]
Geographic fit / life logistics  [ / ]
```

Weight each factor 1–5 based on YOUR priorities. Sum × weight for each offer. Total comparable comp + weighted non-comp score = your decision input.

**Rules**:
- **Do not treat equity at face value** — always apply risk-adjusted discount based on stage
- **Include PTO in the math** — companies offering "unlimited PTO" that nobody actually takes are different from companies offering 25 specific days
- **Re-run the math when something changes** — if they counter with more equity instead of base, the math changes
- **Trust the non-comp factors** — a 10% lower total at a better role with a better team usually wins long-term

---

**End of Module 5.** 10 prompts · 8 scripts · 3 worksheets. Flagship module complete.
