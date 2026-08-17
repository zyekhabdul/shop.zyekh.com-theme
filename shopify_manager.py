#!/usr/bin/env python3
"""
Shopify Direct Integration & Automation Engine for Zyekh Ecosystem
Supports Theme Asset Injection, Live Product Sync & Inventory Automation
"""

import sys, os, json, urllib.request, urllib.error

CONFIG_FILE = "/home/fuckadmin/Projects/shop.zyekh.com-theme/.shopify_env"

def load_credentials():
    shop_domain = os.environ.get("SHOPIFY_SHOP_DOMAIN")
    access_token = os.environ.get("SHOPIFY_ADMIN_API_ACCESS_TOKEN") or os.environ.get("SHOPIFY_ACCESS_TOKEN")

    if not shop_domain or not access_token:
        # Check local .shopify_env file
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE) as f:
                for line in f:
                    if "=" in line:
                        k, v = line.strip().split("=", 1)
                        if k == "SHOPIFY_SHOP_DOMAIN": shop_domain = v.strip("\"'")
                        if k in ["SHOPIFY_ADMIN_API_ACCESS_TOKEN", "SHOPIFY_ADMIN_ACCESS_TOKEN", "SHOPIFY_ACCESS_TOKEN"]: access_token = v.strip("\"'")

        # Check MCP Config Extended
        mcp_file = "/home/fuckadmin/.gemini/config/mcp_config_extended.json"
        if os.path.exists(mcp_file):
            try:
                cfg = json.load(open(mcp_file))
                env = cfg.get("mcpServers", {}).get("shopify", {}).get("env", {})
                if not shop_domain: shop_domain = env.get("SHOPIFY_SHOP_DOMAIN")
                if not access_token: access_token = env.get("SHOPIFY_ADMIN_API_ACCESS_TOKEN")
            except:
                pass

    return shop_domain, access_token

def request_shopify(endpoint, method="GET", data=None):
    domain, token = load_credentials()
    if not domain or not token:
        print("[ERROR] Kredensial Shopify belum dikonfigurasi.")
        print("Silakan jalankan: python3 shopify_manager.py --setup <shop_domain> <access_token>")
        sys.exit(1)

    clean_domain = domain.replace("https://", "").replace("http://", "").strip("/")
    url = f"https://{clean_domain}/admin/api/2024-01/{endpoint.lstrip('/')}"
    headers = {
        "X-Shopify-Access-Token": token,
        "Content-Type": "application/json"
    }

    payload = json.dumps(data).encode("utf-8") if data else None
    req = urllib.request.Request(url, data=payload, headers=headers, method=method)
    
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        print(f"[HTTP ERROR {e.code}] {e.read().decode()}")
        sys.exit(1)
    except Exception as e:
        print(f"[NETWORK ERROR] {e}")
        sys.exit(1)

def setup(domain, token):
    with open(CONFIG_FILE, "w") as f:
        f.write(f"SHOPIFY_SHOP_DOMAIN={domain}\nSHOPIFY_ADMIN_API_ACCESS_TOKEN={token}\n")
    os.chmod(CONFIG_FILE, 0o600)
    print(f"✅ Kredensial Shopify untuk '{domain}' berhasil disimpan dengan aman (0600).")

def check_connection():
    res = request_shopify("shop.json")
    shop = res.get("shop", {})
    print(f"✅ BERHASIL TERHUBUNG KE SHOPIFY:")
    print(f"• Nama Toko: {shop.get('name')}")
    print(f"• Domain: {shop.get('myshopify_domain')} ({shop.get('domain')})")
    print(f"• Email: {shop.get('email')}")
    print(f"• Mata Uang: {shop.get('currency')}")

def list_themes():
    res = request_shopify("themes.json")
    themes = res.get("themes", [])
    print(f"📂 DAFTAR TEMA SHOPIFY ({len(themes)} ditemukan):")
    for t in themes:
        status = "🟢 [AKTIF/PUBLISHED]" if t.get("role") == "main" else f"⚪ [{t.get('role')}]"
        print(f"• ID: {t.get('id')} | {t.get('name')} {status}")
    return themes

def inject_ai_widget():
    themes = list_themes()
    main_theme = next((t for t in themes if t.get("role") == "main"), None)
    if not main_theme:
        print("❌ Tidak ditemukan tema utama yang aktif.")
        sys.exit(1)

    theme_id = main_theme["id"]
    print(f"\n🚀 Menyuntikkan Widget AI ke tema utama (ID: {theme_id})...")

    # 1. Upload snippet ai-chat-widget.liquid
    snippet_content = """{% comment %}
  Zyekh AI Chat Widget Integration
  Embeds the central omnichannel AI CS & Sales Assistant
{% endcomment %}
<script 
  src="https://chat.zyekh.com/chat-widget.js" 
  data-api="https://api.zyekh.com"
  data-persona="cs_store"
  data-title="Yakunziz Support"
  data-subtitle="Online • Instan Delivery CS"
  defer>
</script>"""

    req_snippet = {
        "asset": {
            "key": "snippets/ai-chat-widget.liquid",
            "value": snippet_content
        }
    }
    request_shopify(f"themes/{theme_id}/assets.json", method="PUT", data=req_snippet)
    print("✅ Snippet 'snippets/ai-chat-widget.liquid' berhasil diunggah!")

    # 2. Ambil layout/theme.liquid saat ini
    res_layout = request_shopify(f"themes/{theme_id}/assets.json?asset[key]=layout/theme.liquid")
    theme_liquid = res_layout.get("asset", {}).get("value", "")

    if "ai-chat-widget" not in theme_liquid and "{% render 'ai-chat-widget' %}" not in theme_liquid:
        if "</body>" in theme_liquid:
            updated_liquid = theme_liquid.replace("</body>", "  {% render 'ai-chat-widget' %}\n</body>")
        else:
            updated_liquid = theme_liquid + "\n{% render 'ai-chat-widget' %}\n"

        req_layout = {
            "asset": {
                "key": "layout/theme.liquid",
                "value": updated_liquid
            }
        }
        request_shopify(f"themes/{theme_id}/assets.json", method="PUT", data=req_layout)
        print("✅ Tag '{% render 'ai-chat-widget' %}' berhasil disematkan ke layout/theme.liquid!")
    else:
        print("ℹ️ Snippet sudah terdaftar di theme.liquid sebelumnya.")

    print("\n🎉 WIDGET AI CUSTOMER SERVICE RESMI AKTIF DI TOKO SHOPIFY ANDA!")

if __name__ == "__main__":
    if len(sys.argv) < 2 or "--help" in sys.argv:
        print("🛍️ Shopify Integration Tool for Zyekh Ecosystem")
        print("-------------------------------------------------")
        print("Perintah:")
        print("  --setup <domain> <token> : Konfigurasi domain dan token Shopify Admin API")
        print("  --check                  : Uji koneksi ke toko Shopify")
        print("  --themes                 : Tampilkan daftar tema toko")
        print("  --inject-widget          : Otomatis upload snippet & aktifkan widget di tema live")
        sys.exit(0)

    arg = sys.argv[1]
    if arg == "--setup" and len(sys.argv) >= 4:
        setup(sys.argv[2], sys.argv[3])
    elif arg == "--check":
        check_connection()
    elif arg == "--themes":
        list_themes()
    elif arg == "--inject-widget":
        inject_ai_widget()
