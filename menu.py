import database
import tasks
import manuals


def show_inventory():
    print("\n--- Your Inventory ---")
    items = database.list_items()
    if not items:
        print("(empty)")
    for name, quantity in items:
        print(f" - {name}: {quantity}")


def add_inventory_item():
    name = input("Item name: ").strip().lower()
    if not name:
        print("No name entered.")
        return
    amount_text = input("Quantity (press Enter for 1): ").strip()
    amount = float(amount_text) if amount_text else 1
    database.add_item(name, amount)
    print(f"Added {name}.")


def show_due_tasks():
    print("\n--- Tasks Due ---")
    due = tasks.get_due_tasks()
    if not due:
        print("Nothing due. Nice.")
    for name, kind, status in due:
        print(f" - [{kind}] {name} ({status})")


def add_new_task():
    name = input("Task name: ").strip().lower()
    if not name:
        print("No name entered.")
        return
    kind = input("Type 'chore' or 'maintenance': ").strip().lower()
    if kind not in ("chore", "maintenance"):
        print("Must be 'chore' or 'maintenance'.")
        return
    days_text = input("How often, in days: ").strip()
    if not days_text.isdigit():
        print("Please enter a number.")
        return
    tasks.add_task(name, kind, int(days_text))
    print(f"Added {kind}: {name}.")


def complete_task():
    name = input("Which task did you finish: ").strip().lower()
    tasks.mark_done(name)
    print(f"Marked '{name}' as done.")


def ask_manual():
    question = input("Ask about your appliances: ").strip()
    if not question:
        print("No question entered.")
        return
    results = manuals.search_manuals(question)
    print("\n--- Manual Answers ---")
    if not results:
        print("Nothing relevant found.")
    for text in results:
        print(" -", text)


def main():
    database.setup()
    manuals.setup_manuals()
    while True:
        print("\n===== HomePilot =====")
        print("1. Show inventory")
        print("2. Add inventory item")
        print("3. Show tasks due")
        print("4. Add a task")
        print("5. Mark a task done")
        print("6. Ask about appliances")
        print("7. Quit")

        choice = input("Choose 1-7: ").strip()

        if choice == "1":
            show_inventory()
        elif choice == "2":
            add_inventory_item()
        elif choice == "3":
            show_due_tasks()
        elif choice == "4":
            add_new_task()
        elif choice == "5":
            complete_task()
        elif choice == "6":
            ask_manual()
        elif choice == "7":
            print("Bye!")
            break
        else:
            print("Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()