# PLAN.md — Category Circle Icons & Hero Banner Redesign Plan

## Reference Specification
- **PRD Source**: [`PRD.md`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/PRD.md)
- **Workflow Standard**: [`AGENTS.md`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/AGENTS.md)
- **Visual Audit Findings**: Screenshot `uploaded_media_1786545948641.png` identified flat line wireframe icons inside plain grey circles and a textureless dark-purple background `#1e1b4b` on the Hero Banner.

---

## Hyper-Granular Task Breakdown

### Chunk 1: Redesign Category Circle Badges in `sections/category-carousel.liquid`
- **Target File**: [`sections/category-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/category-carousel.liquid)
- **Scope**:
  - Replace plain grey circle backgrounds (`#f9fafb`) with pastel-tinted duotone gradients per category (Soft Blue, Soft Rose, Soft Amber, Soft Emerald, Soft Violet, Soft Indigo).
  - Upgrade SVG fallback icons to duotone styled strokes with vibrant accent fills (`stroke-width: 1.8`, `color: var(--category-accent)`).
  - Add elevated double-ring border (`outline: 2px solid var(--border-color)`), subtle drop shadow (`box-shadow: 0 4px 12px rgba(0,0,0,0.06)`), and 1.1x icon scale animation on hover.
- **Definition of Done (DoD)**: Category badges display rich duotone pastel avatars with scale animations, `shopify theme check` 0 errors.

### Chunk 2: Redesign Hero Carousel Banner in `sections/hero-carousel.liquid`
- **Target File**: [`sections/hero-carousel.liquid`](file:///home/fuckadmin/Projects/shop.zyekh.com-theme/sections/hero-carousel.liquid)
- **Scope**:
  - Eliminate dark purple `#1e1b4b` background gradient.
  - Implement Slate Glass Mesh Gradient (`linear-gradient(135deg, #090d16 0%, #1e293b 50%, #0f172a 100%)`) with radial spotlight lighting aura.
  - Upgrade "MARKETPLACE DEALS" badge to glassmorphic blur backdrop (`backdrop-filter: blur(12px)`), crisp 11px uppercase tracking, and green glowing dot.
  - Upgrade CTA button to pill shape (`border-radius: 999px`), crisp dark text on white button, and hover lift effect.
  - Upgrade slider navigation buttons to glassmorphic circular arrows.
- **Definition of Done (DoD)**: Hero banner displays slate glass gradient with radial aura, glass badge, pill CTA, `shopify theme check` 0 errors.

### Chunk 3: Quality Gate & Local Checkpoint
- **Scope**: Execute `shopify theme check` (0 error) & `git commit` to save progress in local repository.
- **Definition of Done (DoD)**: Theme check 0 error, local git commit created.
