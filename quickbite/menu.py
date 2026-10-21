MENU = [
    {"id": 1, "name": "Margherita Pizza", "price": 250.0, "veg": True},
    {"id": 2, "name": "Chicken Biryani", "price": 320.0, "veg": False},
    {"id": 3, "name": "Paneer Wrap", "price": 140.0, "veg": True},
]

def search(term):
    term = term.lower().strip()
    return [m for m in MENU if term in m["name"].lower()]
