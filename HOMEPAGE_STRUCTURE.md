# HOMEPAGE_STRUCTURE.md — General E-Commerce Dropship Marketplace Architecture (Bagisto / Amazon / eBay Style)

## 1. Project Purpose & Positioning
- **Storefront Concept**: General E-Commerce Dropshipping Marketplace (Bagisto 2.4.x Velocity / Amazon / eBay Standard).
- **Scope**: Multi-category dropship catalogue (Electronics, Fashion, Home & Living, Beauty, Gadgets, Automotive).
- **Engine Standard**: ZYEKH Engine (Vanilla ES6+, CSS Variables, Anti-FOUC, zero third-party dependencies).

---

## 2. Canonical Homepage Section Hierarchy (`templates/index.json`)

```
[1] Top Announcement Bar (sections/announcement-bar.liquid)
    └── Purpose: Free shipping threshold, multi-currency notice, global shipping terms.

[2] Main Marketplace Header (sections/header.liquid)
    └── Purpose: Brand logo, category dropdown predictive search bar, compare/wishlist counters, account, cart drawer icon.

[3] Hero Carousel Banner (sections/hero-carousel.liquid)
    └── Purpose: High-impact Bagisto 2.4.x multi-slide banner featuring major category promotions & Deal of the Day.

[4] Marketplace Trust & Services Grid (sections/services-grid.liquid)
    └── Purpose: Reassurance badges immediately below hero (Free Worldwide Shipping, 30-Day Money Back Guarantee, Safe Escrow Checkout, 24/7 Support).

[5] Category Circle Carousel (sections/category-carousel.liquid)
    └── Purpose: Fast category jump circles (Electronics, Fashion, Home, Beauty, Accessories, Gadgets) with smooth scroll navigation.

[6] Flash Sale & Daily Deals Bar (sections/flash-sale-bar.liquid)
    └── Purpose: Real-time countdown timer (Hours:Minutes:Seconds) + high-margin deal cards.

[7] Bento Grid Category Discovery (sections/bento-grid-categories.liquid)
    └── Purpose: Amazon/eBay-style visual category showcase tiles.

[8] Featured Marketplace Products Grid (sections/featured-collection-carousel.liquid)
    └── Purpose: Marketplace product card grid with star ratings, compare prices, stock urgency, and instant add-to-cart.

[9] Footer Marketplace Group (sections/footer.liquid)
    └── Purpose: Category quick links, buyer protection, payment provider badges, store copyright.
```

---

## 3. Styling & Layout Standards
1. **Edge-to-Edge Bar Backgrounds**: Top Announcement Bar, Header, Hero Carousel, and Footer span 100% full viewport width (`width: 100%; w-full`), while inner content stays centered at `max-width: var(--page-width)` (1280px).
2. **Vanilla CSS Only**: Scoped section styles in `{% stylesheet %}` blocks using CSS Variables. Zero Tailwind bloat.
3. **Zero Emoji Constraint**: Pure SVG icons or clean Unicode text indicators (`->`, `|`, `*`).
4. **i18n Localization Contract**: Every UI text string uses Liquid translation filters `{{ 'key' | t | default: 'Fallback' }}`.
