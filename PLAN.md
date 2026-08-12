# PLAN.md — Category Carousel Refactor & Shopify Live Store Launch Plan

## Reference Specification
- **PRD Source**: [`PRD.md`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/PRD.md)
- **Workflow Standard**: [`AGENTS.md`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/AGENTS.md)
- **Visual Audit**: Screenshot defect fix (`category-carousel.liquid` whitespace & navigation arrows).

---

## Hyper-Granular Task Breakdown

### Chunk 1: Refactor `sections/category-carousel.liquid` Layout & Dynamic Overflow
- **Target File**: [`sections/category-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/category-carousel.liquid)
- **Scope**:
  - Implement Vanilla JS overflow detection: set `data-overflow="true/false"` on `.category-carousel-wrapper` based on `carousel.scrollWidth > carousel.clientWidth`.
  - Scoped CSS: Hide nav arrows (`display: none`) when `data-overflow="false"`. When `data-overflow="true"`, position nav buttons as overlay controls.
  - Add category-specific SVG icon fallbacks for default categories ("Electronics", "Fashion", "Home & Living", "Beauty", "Accessories", "Gadgets") when `block.settings.image` is blank.
- **Definition of Done (DoD)**: Nav arrows auto-hide when items fit without overflow, zero awkward whitespace gaps, category icons distinct, `shopify theme check` 0 errors.

### Chunk 2: Polishing Homepage Sections Grid Alignment
- **Target Files**:
  - [`sections/hero-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/hero-carousel.liquid)
  - [`sections/bento-grid-categories.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/bento-grid-categories.liquid)
  - [`sections/flash-sale-bar.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/flash-sale-bar.liquid)
  - [`sections/featured-collection-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/featured-collection-carousel.liquid)
- **Scope**: Verify consistent max-width (`var(--page-width)`), padding (`var(--page-margin)`), and seamless vertical rhythm across all homepage sections.
- **Definition of Done (DoD)**: Responsive grid alignment clean across 360px, 768px, 1280px breakpoints.

### Chunk 3: Quality Gate & Automated Theme Audit
- **Target Scope**: Entire theme directory (79 files)
- **Execution Command**: `shopify theme check`
- **Definition of Done (DoD)**: 0 ERRORS across all inspected files.

### Chunk 4: Git Local Commit & Shopify Live Push
- **Target Command**: `git commit` & `shopify theme push --store jdidjn-c3.myshopify.com`
- **Scope**: Save progress locally and publish theme to Shopify store `jdidjn-c3.myshopify.com` (Main Theme ID `152405803086`).
- **Definition of Done (DoD)**: Live storefront `shop.zyekh.com` updated with latest theme build.

---

## Strategic Checkpoint & Safety Rails
- **Commit Strategy**: `git commit` after Chunk 1 & Chunk 2.
- **Push Permission**: `git push` to remote GitHub remains restricted unless user explicitly says "push". `shopify theme push` to Shopify store executes upon approval.
- **Stop Condition (Tahap 3B)**: Immediate total halt if any theme check error occurs.
