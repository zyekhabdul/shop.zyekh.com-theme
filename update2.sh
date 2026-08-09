#!/bin/bash
set -e
THEME_DIR="/home/fuckadmin/Projects/shop.zyekh.com-theme"
cd "$THEME_DIR"

# 4. include in sections/product.liquid
if ! grep -q "render 'b2b-tier-pricing'" sections/product.liquid; then
  sed -i '/<div class="product-price">/a \  {% render '\''b2b-tier-pricing'\'' %}' sections/product.liquid
fi

# 5. include in snippets/cart-drawer.liquid
if ! grep -q "render 'ddp-tax-calculator'" snippets/cart-drawer.liquid; then
  sed -i '/<div class="cart-drawer__footer">/a \  {% render '\''ddp-tax-calculator'\'' %}' snippets/cart-drawer.liquid
fi

# 6. include in layout/theme.liquid
if ! grep -q "render 'consent-banner'" layout/theme.liquid; then
  sed -i '/<\/body>/i \  {% render '\''consent-banner'\'' %}' layout/theme.liquid
fi

# 7. Add faceted filters to sections/collection.liquid
if ! grep -q "faceted-filters" sections/collection.liquid; then
  sed -i '/<div class="collection-grid">/i \  {% render '\''faceted-filters'\'' %}' sections/collection.liquid
fi

# 8. Add faceted filters to sections/search.liquid
if ! grep -q "faceted-filters" sections/search.liquid; then
  sed -i '/<div class="search-results">/i \  {% render '\''faceted-filters'\'' %}' sections/search.liquid
fi
