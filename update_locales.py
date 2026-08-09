import json
import os

with open('locales/en.default.json', 'r') as f:
    en = json.load(f)

en['products']['shipping'] = {
    "title": "Shipping Options",
    "origin": "Ships from:",
    "economy": "Economy",
    "standard": "Standard",
    "express": "Express",
    "days": "days",
    "free": "Free"
}

en['products']['inventory'] = {
    "hurry": "Hurry!",
    "only_left": "Only {{ count }} left in stock."
}

en['products']['social_proof'] = {
    "toast": "Someone in {{ location }} just bought this {{ time }}m ago"
}

with open('locales/en.default.json', 'w') as f:
    json.dump(en, f, indent=2)

with open('locales/id.json', 'r') as f:
    id_lang = json.load(f)

id_lang['products']['shipping'] = {
    "title": "Opsi Pengiriman",
    "origin": "Dikirim dari:",
    "economy": "Ekonomi",
    "standard": "Standar",
    "express": "Ekspres",
    "days": "hari",
    "free": "Gratis"
}

id_lang['products']['inventory'] = {
    "hurry": "Cepat!",
    "only_left": "Tersisa {{ count }} stok."
}

id_lang['products']['social_proof'] = {
    "toast": "Seseorang di {{ location }} baru saja membeli ini {{ time }}m lalu"
}

with open('locales/id.json', 'w') as f:
    json.dump(id_lang, f, indent=2, ensure_ascii=False)
