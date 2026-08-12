# PLAN.md — Systemic Product Card Refactor Plan

## Reference Specification
- **PRD Source**: [`PRD.md`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/PRD.md)
- **Workflow Standard**: [`AGENTS.md`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/AGENTS.md)
- **Visual Audit Findings**: Screenshot `uploaded_media_1786543532849.png` identified legacy placeholder cards in `sections/flash-sale-bar.liquid` rendering 24px bold titles and bright blue price text.

---

## Hyper-Granular Task Breakdown

### Chunk 1: Systemic CSS Safety Guard in `assets/critical.css`
- **Target File**: [`assets/critical.css`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/assets/critical.css)
- **Scope**:
  - Update legacy `.product-title` CSS rule to enforce `font-size: 0.875rem` (14px), `font-weight: 600`, `line-height: 1.35`, and `color: var(--text-main)` across all breakpoints (desktop & mobile).
  - Enforce `.product-price` to use `color: var(--text-main)` (15px bold), removing electric blue fallbacks.
- **Definition of Done (DoD)**: Global `.product-title` fallback capped at 14px.

### Chunk 2: Refactor `sections/flash-sale-bar.liquid` Placeholder Cards
- **Target File**: [`sections/flash-sale-bar.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/flash-sale-bar.liquid)
- **Scope**:
  - Replace legacy HTML markup in placeholder cards ("Flash Sale Product Sample") with BEM `.product-card` structure (`.product-card__title` 14px, `.product-card__price` 15px, `.product-card__compare-price` 12px, `.product-card__atc-btn`).
- **Definition of Done (DoD)**: Flash sale cards render at 14px font size, matching featured product cards.

### Chunk 3: Refactor `sections/featured-collection.liquid` Placeholder Cards
- **Target File**: [`sections/featured-collection.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/featured-collection.liquid)
- **Scope**:
  - Replace legacy HTML markup in placeholder cards ("Example Product") with BEM `.product-card` structure.
- **Definition of Done (DoD)**: Featured collection cards render at 14px font size.

### Chunk 4: Quality Gate & Local Git Commit
- **Scope**: Execute `shopify theme check` (0 error) & `git commit` to save progress in local repository.
- **Definition of Done (DoD)**: Theme check 0 error, working tree clean.
