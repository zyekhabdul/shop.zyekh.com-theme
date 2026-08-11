# PLAN.md — Enterprise Bagisto 2.4.x / Velocity Replica Standardization Plan

## Reference Specification
- **PRD Source**: [`PRD.md`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/PRD.md) & [`01-Dokumen/PRD-shop.zyekh.com-theme.md`](file:///home/fuckadmin/Documents/Obsidian%20Vault/01-Dokumen/PRD-shop.zyekh.com-theme.md)
- **Workflow Standard**: [`AGENTS (1).md`](file:///home/fuckadmin/Downloads/AGENTS%20%281%29.md)

---

## Hyper-Granular Task Breakdown

### Chunk 1: Synchronize `templates/index.json` with PRD v5.1 Sequence
- **Target File**: [`templates/index.json`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/templates/index.json)
- **Scope**: Align root JSON `order` array to match PRD v5.1 exact sequence:
  1. `announcement` (`sections/announcement-bar.liquid`)
  2. `hero_carousel` (`sections/hero-carousel.liquid` with 2 slide blocks)
  3. `category_carousel` (`sections/category-carousel.liquid` with 6 circle category blocks)
  4. `flash_sale` (`sections/flash-sale-bar.liquid`)
  5. `bento_categories` (`sections/bento-grid-categories.liquid`)
  6. `featured_carousel` (`sections/featured-collection-carousel.liquid`)
  7. `services` (`sections/services-grid.liquid`)
- **Data Contract**: Valid JSON schema with default block settings.
- **Definition of Done (DoD)**: JSON parser passes without syntax errors, order matches L17-L23 of `PRD.md`.

### Chunk 2: Refactor `sections/hero-carousel.liquid` to Scoped ZYEKH Vanilla CSS
- **Target File**: [`sections/hero-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/hero-carousel.liquid)
- **Scope**:
  - Replace unparsed Tailwind classes with ZYEKH Engine Vanilla CSS in `{% stylesheet %}` block.
  - CSS selector specs: `.hero-carousel-wrapper` (min-height 380px), `.hero-slide-gradient` (`linear-gradient(135deg, #0f172a 0%, #1e1b4b 60%, #312e81 100%)`), `.hero-slide-heading` (clamp 1.8rem to 3.2rem), `.hero-slide-btn` (background `#ffffff`, color `#0f172a`).
  - JS slider navigation hook: `HeroPrev-{{ section.id }}` & `HeroNext-{{ section.id }}`.
- **Definition of Done (DoD)**: Zero Tailwind class remnants, `shopify theme check` L0 errors on file.

### Chunk 3: Refactor `sections/category-carousel.liquid` Flexbox Avatar Centering
- **Target File**: [`sections/category-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/category-carousel.liquid)
- **Scope**:
  - Add scoped `{% stylesheet %}` block for flexbox centering.
  - CSS specs: `.category-carousel-wrapper` (`display: flex; align-items: center; justify-content: center; gap: 0.75rem; max-width: var(--page-width); margin: 0 auto; padding: 1.5rem var(--page-margin)`).
  - Avatar circle specs: `.category-carousel__avatar` (`width: 80px; height: 80px; border-radius: 50%; background: var(--bg-surface); border: 2px solid var(--border-color)`).
- **Definition of Done (DoD)**: Flexbox layout verified, `shopify theme check` L0 errors on file.

### Chunk 4: Full Automated Theme Check & Verification Gate
- **Target Scope**: Entire theme directory (79 files)
- **Execution Command**: `shopify theme check`
- **Definition of Done (DoD)**: 0 ERRORS across all inspected files.

---

## Strategic Checkpoint & Safety Rails
- **Commit Strategy**: `git commit` created after completion of each chunk.
- **Stop Condition (Tahap 3B)**: Immediate total halt if any theme check error is encountered or sensitive files are touched.
