class Cart:
    def __init__(self):
        self.items = []
    def add(self, item, qty=1):
        if qty < 1:
            raise ValueError("Quantity must be at least 1")
        self.items.append((item, qty))
    def total(self):
        return sum(i["price"] * q for i, q in self.items)
