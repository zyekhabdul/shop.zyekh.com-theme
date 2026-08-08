import os
import sys
import json
import urllib.request
import urllib.error

def load_env():
    if os.path.exists('.env'):
        with open('.env') as f:
            for line in f:
                if '=' in line and not line.strip().startswith('#'):
                    key, val = line.strip().split('=', 1)
                    os.environ[key] = val

def verify_shopify_connection():
    load_env()
    # Mengambil konfigurasi dari environment variables
    # (Pastikan Anda sudah menset environment variables atau menaruhnya di file .env lalu me-load-nya)
    store_domain = os.environ.get("SHOPIFY_STORE_URL", "jdidjn-c3.myshopify.com")
    api_token = os.environ.get("SHOPIFY_ACCESS_TOKEN")

    if not api_token:
        print("ERROR: SHOPIFY_ACCESS_TOKEN belum diset di environment atau file .env")
        sys.exit(1)

    url = f"https://{store_domain}/admin/api/2024-01/themes.json"
    
    headers = {
        "X-Shopify-Access-Token": api_token,
        "Content-Type": "application/json"
    }

    req = urllib.request.Request(url, headers=headers)
    
    try:
        print(f"Mencoba koneksi ke {store_domain}...")
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                data = json.loads(response.read().decode())
                themes = data.get("themes", [])
                
                print("\n✅ KONEKSI BERHASIL! Token Valid.")
                print("-" * 40)
                print("Daftar Theme yang ada di toko Anda:")
                for theme in themes:
                    role = theme.get("role")
                    name = theme.get("name")
                    id = theme.get("id")
                    print(f"- [{role.upper()}] {name} (ID: {id})")
                print("-" * 40)
                print("\nAutomasi API siap digunakan (misal: untuk auto-deploy atau sync content).")
            else:
                print(f"Gagal: HTTP {response.status}")
    except urllib.error.HTTPError as e:
        print(f"❌ KONEKSI GAGAL. Error: HTTP {e.code}")
        print("Penyebab Umum:")
        print("1. Token salah/typo")
        print("2. Scope 'read_themes' belum dicentang di Custom App")
    except Exception as e:
        print(f"❌ ERROR: {e}")

if __name__ == "__main__":
    verify_shopify_connection()
