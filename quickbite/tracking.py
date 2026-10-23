STATUSES = ["PLACED", "PREPARING", "OUT_FOR_DELIVERY", "DELIVERED"]

def next_status(current):
    i = STATUSES.index(current)
    return STATUSES[min(i + 1, len(STATUSES) - 1)]
