import sqlite3
from datetime import datetime, timedelta

import database


def add_task(name, kind, interval_days):
    conn = sqlite3.connect(database.DB_FILE)
    conn.execute(
        "INSERT OR REPLACE INTO tasks (name, kind, interval_days, last_done) VALUES (?, ?, ?, ?)",
        (name, kind, interval_days, None),
    )
    conn.commit()
    conn.close()


def mark_done(name):
    today = datetime.now().strftime("%Y-%m-%d")
    conn = sqlite3.connect(database.DB_FILE)
    conn.execute("UPDATE tasks SET last_done = ? WHERE name = ?", (today, name))
    conn.commit()
    conn.close()


def get_due_tasks():
    conn = sqlite3.connect(database.DB_FILE)
    rows = conn.execute(
        "SELECT name, kind, interval_days, last_done FROM tasks"
    ).fetchall()
    conn.close()

    today = datetime.now()
    due = []
    for name, kind, interval_days, last_done in rows:
        if last_done is None:
            due.append((name, kind, "never done"))
            continue
        last_date = datetime.strptime(last_done, "%Y-%m-%d")
        due_date = last_date + timedelta(days=interval_days)
        if today >= due_date:
            days_over = (today - due_date).days
            due.append((name, kind, f"overdue by {days_over} days"))
    return due


if __name__ == "__main__":
    database.setup()

    add_task("vacuum living room", "chore", 7)
    add_task("clean bathroom", "chore", 7)
    add_task("replace HVAC filter", "maintenance", 90)

    print("Tasks due right now:")
    for name, kind, status in get_due_tasks():
        print(f" - [{kind}] {name} ({status})")