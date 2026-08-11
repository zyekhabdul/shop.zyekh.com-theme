# PLAN.md — Homepage Marketplace Architecture Standardization & Refactor

## Reference Specs & Comparison
- **Architecture Spec**: [`HOMEPAGE_STRUCTURE.md`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/HOMEPAGE_STRUCTURE.md)
- **Comparison & Audit Analysis**: [`HOMEPAGE_STRUCTURE_COMPARISON.md`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/HOMEPAGE_STRUCTURE_COMPARISON.md)

---

## Hyper-Granular Task Chunks

### Chunk 1: Synchronize `templates/index.json` with Marketplace Standard
- **Target File**: [`templates/index.json`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/templates/index.json)
- **Action**: Update `order` and default blocks strictly per Bagisto/Amazon marketplace standard:
  1. `announcement` (`sections/announcement-bar.liquid`)
  2. `hero_carousel` (`sections/hero-carousel.liquid` with 2 slide blocks)
  3. `services` (`sections/services-grid.liquid`)
  4. `category_carousel` (`sections/category-carousel.liquid` with 6 category blocks)
  5. `flash_sale` (`sections/flash-sale-bar.liquid`)
  6. `bento_categories` (`sections/bento-grid-categories.liquid`)
  7. `featured_carousel` (`sections/featured-collection-carousel.liquid`)
- **DoD**: Valid JSON structure, verified section order matching `HOMEPAGE_STRUCTURE.md`.

### Chunk 2: Pure Vanilla CSS Refactor for `sections/hero-carousel.liquid`
- **Target File**: [`sections/hero-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/hero-carousel.liquid)
- **Action**: Replace unparsed Tailwind utility classes with scoped Vanilla CSS in `{% stylesheet %}` block:
  - Dark gradient background (`linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%)`).
  - Typography scaling (`var(--font-size-3xl)`), white CTA button, responsive slide padding, and nav buttons (`<` and `>`).
- **DoD**: Hero slider renders with rich styling and zero unstyled Tailwind text.

### Chunk 3: Flexbox Centering for `sections/category-carousel.liquid`
- **Target File**: [`sections/category-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/category-carousel.liquid)
- **Action**: Update CSS layout in `{% stylesheet %}`:
  - Flexbox centering: `display: flex; align-items: center; justify-content: center; gap: 1.5rem; width: 100%; max-width: var(--page-width); margin: 0 auto;`.
  - Avatar circle styling: `width: 80px; height: 80px; border-radius: 50%; background: var(--bg-surface); border: 2px solid var(--border-color);`.
- **DoD**: Category circle items are neatly centered and scrollable between `<` and `>` arrows.

### Chunk 4: Verification & Quality Gate
- **Command**: `shopify theme check`
- **DoD**: 0 ERRORS across all Liquid and JSON files.
