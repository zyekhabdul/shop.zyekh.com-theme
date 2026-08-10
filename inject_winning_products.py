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

def inject_draft_products():
    load_env()
    store_domain = os.environ.get("SHOPIFY_STORE_URL", "jdidjn-c3.myshopify.com")
    api_token = os.environ.get("SHOPIFY_ACCESS_TOKEN")

    if not api_token:
        print("ERROR: SHOPIFY_ACCESS_TOKEN not set.")
        sys.exit(1)

    url = f"https://{store_domain}/admin/api/2024-01/products.json"
    headers = {
        "X-Shopify-Access-Token": api_token,
        "Content-Type": "application/json"
    }

    products_data = [
        {
            "title": "Smart Red Light Therapy Neck & Face Lifting Massager",
            "body_html": "<p>Elevate your skincare routine with advanced 7-in-1 LED red light therapy and high-frequency sonic vibration. Designed to tighten skin, reduce wrinkles, and sculpt facial contours effortlessly at home.</p><ul><li>7 LED Light Therapy Modes (Red, Blue, Green)</li><li>45°C Thermal Neck & Face Massage</li><li>Ergonomic Dolphin Bionic Design</li><li>USB Rechargeable & Portable</li></ul>",
            "vendor": "Zyekh Beauty",
            "product_type": "Beauty Tech",
            "tags": "winning-product, beauty-tech, trending, skincare, 2026-winning",
            "status": "draft",
            "options": [
                {
                    "name": "Color",
                    "values": ["Pearl White", "Rose Gold", "Midnight Black"]
                }
            ],
            "variants": [
                {
                    "option1": "Pearl White",
                    "price": "499000.00",
                    "compare_at_price": "899000.00",
                    "sku": "ZYK-BTY-01-WHT"
                },
                {
                    "option1": "Rose Gold",
                    "price": "499000.00",
                    "compare_at_price": "899000.00",
                    "sku": "ZYK-BTY-01-RGD"
                },
                {
                    "option1": "Midnight Black",
                    "price": "499000.00",
                    "compare_at_price": "899000.00",
                    "sku": "ZYK-BTY-01-BLK"
                }
            ]
        },
        {
            "title": "Ergonomic Contour Memory Foam Sleep Pillow",
            "body_html": "<p>Say goodbye to morning neck pain and restless nights. Engineered with slow-rebound high-density memory foam and dual-height cervical contours to support natural spine alignment.</p><ul><li>Cervical Spine Support & Pressure Relief</li><li>Cooling Breathable 3D Mesh Outer Cover</li><li>Zero-Pressure Slow Rebound Memory Foam</li><li>Machine Washable Hypoallergenic Cover</li></ul>",
            "vendor": "Zyekh Wellness",
            "product_type": "Health & Sleep Wellness",
            "tags": "winning-product, sleep-wellness, home-essentials, trending, 2026-winning",
            "status": "draft",
            "options": [
                {
                    "name": "Size",
                    "values": ["Standard Ergonomic", "Premium XL Contour"]
                }
            ],
            "variants": [
                {
                    "option1": "Standard Ergonomic",
                    "price": "389000.00",
                    "compare_at_price": "699000.00",
                    "sku": "ZYK-SLP-02-STD"
                },
                {
                    "option1": "Premium XL Contour",
                    "price": "449000.00",
                    "compare_at_price": "799000.00",
                    "sku": "ZYK-SLP-02-PXL"
                }
            ]
        },
        {
            "title": "Interactive Smart Bouncing Pet Ball with Obstacle Avoidance",
            "body_html": "<p>Keep your dogs and cats active and mentally stimulated for hours. Smart self-rotating motion with built-in motion sensors automatically changes direction when hitting obstacles.</p><ul><li>Automatic 360-Degree Self-Rotating Motion</li><li>BPA-Free Food-Grade Silicone Shell</li><li>USB-C Fast Charging (8 Hours Playtime)</li><li>Dual Modes: Normal & Intelligent Auto-Play</li></ul>",
            "vendor": "Zyekh Pets",
            "product_type": "Pet Gadgets",
            "tags": "winning-product, pet-gadgets, viral, trending, 2026-winning",
            "status": "draft",
            "options": [
                {
                    "name": "Color",
                    "values": ["Electric Blue", "Vibrant Pink", "Avocado Green"]
                }
            ],
            "variants": [
                {
                    "option1": "Electric Blue",
                    "price": "249000.00",
                    "compare_at_price": "450000.00",
                    "sku": "ZYK-PET-03-BLU"
                },
                {
                    "option1": "Vibrant Pink",
                    "price": "249000.00",
                    "compare_at_price": "450000.00",
                    "sku": "ZYK-PET-03-PNK"
                },
                {
                    "option1": "Avocado Green",
                    "price": "249000.00",
                    "compare_at_price": "450000.00",
                    "sku": "ZYK-PET-03-GRN"
                }
            ]
        }
    ]

    print(f"Injecting {len(products_data)} DRAFT winning products into {store_domain}...\n")

    created_products = []
    for item in products_data:
        payload = json.dumps({"product": item}).encode('utf-8')
        req = urllib.request.Request(url, data=payload, headers=headers, method='POST')

        try:
            with urllib.request.urlopen(req) as resp:
                if resp.status in (200, 201):
                    res_body = json.loads(resp.read().decode())
                    p = res_body.get("product", {})
                    created_products.append(p)
                    print(f"✓ INJECTED: '{p.get('title')}'")
                    print(f"  - Product ID : {p.get('id')}")
                    print(f"  - Status     : {p.get('status').upper()}")
                    print(f"  - Variants   : {len(p.get('variants', []))} items")
                    print(f"  - Vendor     : {p.get('vendor')}\n")
                else:
                    print(f"✗ FAILED ({item['title']}): HTTP {resp.status}")
        except urllib.error.HTTPError as e:
            err_msg = e.read().decode()
            print(f"✗ HTTP ERROR ({item['title']}): {e.code} - {err_msg}")
        except Exception as e:
            print(f"✗ ERROR ({item['title']}): {e}")

    print("-" * 50)
    print(f"Total DRAFT products successfully injected: {len(created_products)}/{len(products_data)}")

if __name__ == "__main__":
    inject_draft_products()
