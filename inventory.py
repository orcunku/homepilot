import database

TOTAL_WORDS = ("total", "subtotal", "sum", "tax", "cash", "card", "change")


def clean_name(raw_name):
    name = raw_name.strip().lower()
    result = ""
    for char in name:
        if char.isalpha() or char == " ":
            result += char
        else:
            result += " "
    words = result.split()
    kept = [word for word in words if len(word) >= 3]
    return " ".join(kept)

def looks_like_total(name):
    lowered = name.lower()
    return any(word in lowered for word in TOTAL_WORDS)


def add_receipt_items(ocr_items):
    added = []
    for item in ocr_items:
        raw = item["name"]
        if looks_like_total(raw):
            continue
        name = clean_name(raw)
        if not name:
            continue
        database.add_item(name, 1)
        added.append(name)
    return added


if __name__ == "__main__":
    database.setup()

    ocr_items = [
        {"name": "MILK2L", "price": "1.49"},
        {"name": "BREAD", "price": "2.19"},
        {"name": "EGGS 12PK", "price": "305"},
        {"name": "BANANAS", "price": "0.89"},
        {"name": "COFFEE2506", "price": "6.49"},
        {"name": "TOTAL", "price": "1411"},
    ]

    added = add_receipt_items(ocr_items)
    print("Added from receipt:", added)

    print("\nEverything in inventory now:")
    for name, quantity in database.list_items():
        print(" -", name, ":", quantity)