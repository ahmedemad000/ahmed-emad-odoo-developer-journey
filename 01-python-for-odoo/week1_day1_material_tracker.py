# 🏗️ CONSTRUCTION SITE MATERIAL TRACKER
# Goal: Master lists, dictionaries and basic loops – exactly what Odoo uses every day

# 1. Create a dictionary for each material type
steel_bars = {
    "diameter_mm": 16,
    "length_m": 12,
    "quantity": 450,
    "unit_price": 12500,  # EGP per ton
    "total_weight_ton": 4.5
}

cement_bags = {
    "brand": "Asyut Cement",
    "strength": "42.5 N",
    "quantity": 1200,
    "unit_price_per_bag": 135
}

sand = {
    "brand": "Alex Sand",
    "strength": "30.5 N",
    "quantity": 250,
    "unit_price_per_bag": 95
}

gravel = {
    "brand": "Suez Gravel",
    "strength": "10.5 N",
    "quantity": 5,
    "unit_price_per_bag": 35
}

# 2. Put all materials in one big site inventory (list of dictionaries)
site_inventory = [
    {"name": "Steel Φ16", "data": steel_bars},
    {"name": "Cement 42.5N", "data": cement_bags},
    # Add 3 more materials yourself below:
    {"name": "Steel RFT16", "data": sand},
    {"name": "Cement RFT20", "data": gravel},
]

# 3. Print a beautiful report
print("🏗️ DAILY MATERIAL REPORT")
print("=" * 40)
for item in site_inventory:
    data = item["data"]
    print(f"{item['name']}: {data['quantity']} units")