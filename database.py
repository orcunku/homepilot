import sqlite3

DB_FILE = "homepilot.db"


def setup():
    conn = sqlite3.connect(DB_FILE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            name TEXT PRIMARY KEY,
            quantity REAL
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            name TEXT PRIMARY KEY,
            kind TEXT,
            interval_days INTEGER,
            last_done TEXT
        )
    """)
    conn.commit()
    conn.close()


def add_item(name, quantity):
    conn = sqlite3.connect(DB_FILE)
    conn.execute(
        "INSERT OR REPLACE INTO inventory (name, quantity) VALUES (?, ?)",
        (name, quantity),
    )
    conn.commit()
    conn.close()


def list_items():
    conn = sqlite3.connect(DB_FILE)
    rows = conn.execute("SELECT name, quantity FROM inventory").fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    setup()
    add_item("milk", 2)
    add_item("bread", 1)
    add_item("eggs", 12)

    print("Everything in inventory:")
    for name, quantity in list_items():
        print(" -", name, ":", quantity)