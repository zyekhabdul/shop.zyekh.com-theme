# Bagisto 2.4.x to Shopify Liquid 2.0 Structural Mapping (ZYEKH Engine)

This document provides a 1-to-1 mapping between Bagisto 2.4.x structural components and the target Shopify Liquid 2.0 schema, strictly adhering to the ZYEKH Design Engine principles (Zero-dependency Vanilla JS, CSS Variables, Light mode default, zero emoji, WCAG 2.1 AA accessibility).

## 1. Header Top / Header Bottom
- **Bagisto 2.4.x Component**: `header-top`, `header-bottom` (Search, Currency, Language, Account, Cart, Navigation).
- **Shopify Liquid 2.0**: `sections/header.liquid` or `sections/header-group.json`.
- **CSS Variables mapping**: `--header-bg`, `--header-color`, `--header-border`.
- **Structural Notes**: Implement a multi-tier header. `header-top.liquid` snippet for top bar (announcements, utility links), `header-main.liquid` for logo, search, and icons.

## 2. Mega Menu
- **Bagisto 2.4.x Component**: `mega-menu`
- **Shopify Liquid 2.0**: `blocks/mega-menu.liquid` inside `sections/header.liquid`.
- **CSS Variables mapping**: `--dropdown-bg`, `--dropdown-shadow`.
- **Structural Notes**: Vanilla JS for dropdown hover/click handling with ARIA attributes for accessibility.

## 3. Carousel (Hero Slider)
- **Bagisto 2.4.x Component**: `image-carousel`
- **Shopify Liquid 2.0**: `sections/hero-carousel.liquid`
- **CSS Variables mapping**: `--carousel-nav-bg`, `--carousel-nav-color`.
- **Structural Notes**: Pure CSS scroll-snap carousel or lightweight Vanilla JS intersection observer. No external libraries (e.g., Slick, Swiper).

## 4. Services Grid (Value Propositions)
- **Bagisto 2.4.x Component**: `services-component`
- **Shopify Liquid 2.0**: `sections/services-grid.liquid`
- **CSS Variables mapping**: `--icon-color`, `--service-card-bg`.
- **Structural Notes**: CSS Grid layout, responsive, accessible icons (SVG inline).

## 5. Product Card
- **Bagisto 2.4.x Component**: `product-card`
- **Shopify Liquid 2.0**: `snippets/product-card.liquid`
- **CSS Variables mapping**: `--card-bg`, `--card-radius`, `--card-shadow`.
- **Structural Notes**: Lazy loaded images, semantic HTML, quick add-to-cart via Vanilla JS fetch API.

## 6. Mini Cart
- **Bagisto 2.4.x Component**: `mini-cart`
- **Shopify Liquid 2.0**: `sections/cart-drawer.liquid` or `snippets/mini-cart.liquid`.
- **CSS Variables mapping**: `--drawer-width`, `--drawer-bg`.
- **Structural Notes**: Off-canvas drawer sliding in from the right, updated dynamically using Section Rendering API.

## 7. PDP Gallery / Buy Box
- **Bagisto 2.4.x Component**: `product-gallery`, `product-options`
- **Shopify Liquid 2.0**: `sections/main-product.liquid` (with media gallery and form blocks).
- **CSS Variables mapping**: `--gallery-thumbnail-border`.
- **Structural Notes**: CSS Grid for gallery. Vanilla JS for variant selection updating URL and price without full reload.

## 8. Faceted Filter Sidebar
- **Bagisto 2.4.x Component**: `layered-navigation`
- **Shopify Liquid 2.0**: `sections/main-collection-product-grid.liquid` (incorporating `snippets/facets.liquid`).
- **CSS Variables mapping**: `--filter-sidebar-width`, `--filter-item-active`.
- **Structural Notes**: Use Shopify's Storefront Filtering API. Vanilla JS to fetch and update DOM via Section Rendering API.

---

### Implementation Guidelines
1. **Zero-dependency**: No jQuery, no React, no Alpine.js. Just modern DOM APIs.
2. **CSS Variables**: Theme must be fully configurable via `settings_data.json` injecting into CSS custom properties.
3. **Accessibility**: All interactive elements must have `aria-expanded`, `aria-hidden`, and keyboard navigation support.
4. **Light Mode Default**: Base variables are light mode. Dark mode can be an optional extension via `@media (prefers-color-scheme: dark)`.
