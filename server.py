from mcp.server.fastmcp import FastMCP

import database
import tasks
import manuals

mcp = FastMCP("homepilot")

database.setup()
manuals.setup_manuals()


@mcp.tool()
def add_inventory_item(name: str, quantity: float = 1) -> str:
    """Add a grocery or household item to the inventory. Use when the user
    mentions buying, adding, or having an item."""
    database.add_item(name.lower(), quantity)
    return f"Added {quantity} of {name}."


@mcp.tool()
def show_inventory() -> str:
    """List everything currently in the household inventory."""
    items = database.list_items()
    if not items:
        return "Inventory is empty."
    return "\n".join(f"{name}: {quantity}" for name, quantity in items)


@mcp.tool()
def add_task(name: str, kind: str, interval_days: int) -> str:
    """Add a recurring chore or maintenance task. kind must be 'chore' or
    'maintenance'. interval_days is how often it repeats."""
    if kind not in ("chore", "maintenance"):
        return "kind must be 'chore' or 'maintenance'."
    tasks.add_task(name.lower(), kind, interval_days)
    return f"Added {kind}: {name}, every {interval_days} days."


@mcp.tool()
def show_due_tasks() -> str:
    """Show all chores and maintenance tasks that are currently due or overdue."""
    due = tasks.get_due_tasks()
    if not due:
        return "Nothing is due right now."
    return "\n".join(f"[{kind}] {name} ({status})" for name, kind, status in due)


@mcp.tool()
def complete_task(name: str) -> str:
    """Mark a chore or maintenance task as done, resetting its schedule."""
    tasks.mark_done(name.lower())
    return f"Marked '{name}' as done."


@mcp.tool()
def ask_manual(question: str) -> str:
    """Answer a question about home appliances by searching stored manuals."""
    results = manuals.search_manuals(question)
    if not results:
        return "Nothing relevant found in the manuals."
    return "\n".join(results)


if __name__ == "__main__":
    mcp.run()