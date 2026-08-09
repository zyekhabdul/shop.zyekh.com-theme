#!/bin/bash
set -e
THEME_DIR="/home/fuckadmin/Projects/shop.zyekh.com-theme"
cd "$THEME_DIR"

# 1. snippets/b2b-tier-pricing.liquid
cat << 'LIQUID' > snippets/b2b-tier-pricing.liquid
{% if product.tags contains 'b2b-enabled' %}
<div class="b2b-tier-pricing">
  <h3>{{ 'products.b2b.wholesale_pricing' | t }}</h3>
  <table class="b2b-pricing-table">
    <thead>
      <tr>
        <th>{{ 'products.b2b.quantity' | t }}</th>
        <th>{{ 'products.b2b.price_per_unit' | t }}</th>
      </tr>
    </thead>
    <tbody>
      {% for tag in product.tags %}
        {% if tag contains 'tier-' %}
          {% assign qty = tag | split: '-' | index: 1 %}
          {% assign discount = tag | split: '-' | index: 2 | divided_by: 100.0 %}
          {% assign price = product.price | times: discount %}
          <tr>
            <td>{{ qty }}+</td>
            <td>{{ price | money }}</td>
          </tr>
        {% endif %}
      {% endfor %}
    </tbody>
  </table>
</div>
{% endif %}
LIQUID

# 2. snippets/ddp-tax-calculator.liquid
cat << 'LIQUID' > snippets/ddp-tax-calculator.liquid
<div class="ddp-tax-calculator" data-cart-total="{{ cart.total_price }}">
  <label for="country-selector">{{ 'cart.taxes.estimate_for' | t }}:</label>
  <select id="country-selector">
    <option value="US">United States (No DDP)</option>
    <option value="EU">European Union (VAT & Duties)</option>
    <option value="ID">Indonesia (Bea Cukai)</option>
  </select>
  <div class="ddp-result">
    <span>{{ 'cart.taxes.estimated_duties' | t }}: </span>
    <strong id="ddp-amount">{{ 0 | money }}</strong>
  </div>
</div>
LIQUID

# 3. snippets/consent-banner.liquid
cat << 'LIQUID' > snippets/consent-banner.liquid
<div id="consent-banner" class="consent-banner" style="display: none;">
  <div class="consent-content">
    <p>{{ 'general.privacy.consent_message' | t }}</p>
    <div class="consent-actions">
      <button id="accept-cookies" class="btn btn--primary">{{ 'general.privacy.accept' | t }}</button>
      <button id="decline-cookies" class="btn btn--secondary">{{ 'general.privacy.decline' | t }}</button>
    </div>
  </div>
</div>
<script>
  if (!localStorage.getItem('cookieConsent')) {
    document.getElementById('consent-banner').style.display = 'block';
  }
  document.getElementById('accept-cookies').addEventListener('click', function() {
    localStorage.setItem('cookieConsent', 'accepted');
    document.getElementById('consent-banner').style.display = 'none';
  });
  document.getElementById('decline-cookies').addEventListener('click', function() {
    localStorage.setItem('cookieConsent', 'declined');
    document.getElementById('consent-banner').style.display = 'none';
  });
</script>
LIQUID

