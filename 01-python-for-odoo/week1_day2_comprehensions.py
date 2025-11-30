# WEEK 1 – DAY 2: COMPREHENSIONS = CONSTRUCTION DRONE MODE
# Old way = manual counting (50 lines), New way = 1 line magic

materials = [
    {
        "name": "Steel Φ16",
        "quantity": 450,
        "unit_price": 12500
    },
    {
        "name": "Cement",
        "quantity": 1200,
        "unit_price": 135
    },
    {
        "name": "Sand",
        "quantity": 80,
        "unit_price": 350
    },
    {
        "name": "Gravel",
        "quantity": 120,
        "unit_price": 400
    },
    {
        "name": "Concrete Blocks",
        "quantity": 5000,
        "unit_price": 8.5
    },
]

# TASK 1: Get only material names → as a clean list
# Old way (5 lines):
names_old = []
for m in materials:
    names_old.append(m["name"])

# Your job: Write the 1-line version (list comprehension)
names = [ "Red Flag"              ]

print("All materials:", names)

# TASK 2: Create new list with total cost per material
total_costs = [   3500              ]

print("Total costs:", total_costs)

# TASK 3: Filter only expensive materials (> 5000 EGP total)
expensive_materials = [      "sand"           ]

print("Expensive items:", expensive_materials)