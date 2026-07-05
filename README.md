# HomePilot — Smart Home Task Manager# HomePilot — Smart Home Task Manager

An AI-powered home assistant that manages household inventory, chores, and maintenance. Built with free, open tools, it combines **OCR**, **RAG** (document search), and **tool-calling AI agents** connected over **MCP** (Model Context Protocol).

You can talk to it in plain English — *"add milk to my inventory"*, *"what chores are due?"*, *"how do I descale the coffee machine?"* — and an AI model routes each request to the right tool.

## What it does

- **Inventory tracking** — reads grocery receipts with OCR and stores items in a local database.
- **Chore & maintenance scheduling** — tracks recurring tasks and tells you what's due or overdue.
- **Manual search (RAG)** — answers questions about your appliances by searching stored manual text by relevance.
- **AI-driven** — all features are exposed as tools an AI assistant can call through natural language.

## How it works

You give a plain-English request. The AI client reads it, picks the right tool from those exposed by the MCP server, runs the underlying Python function, and replies in natural language.

## Tech stack

- **Python** — core language
- **SQLite** — local, persistent storage
- **Tesseract OCR** — reads text from receipt images
- **scikit-learn (TF-IDF)** — relevance-based document search for the RAG feature
- **MCP (Model Context Protocol)** — exposes the app's functions as tools an AI can call
- **Jan + Gemini (free tier)** — the AI "brain" that drives the tools

All tools used are free.

## Project structure

| File | Purpose |
|------|---------|
| `database.py` | SQLite storage for inventory and tasks |
| `inventory.py` | Turns OCR receipt text into clean stored items |
| `tasks.py` | Chores and maintenance scheduling logic |
| `manuals.py` | RAG document storage and relevance search |
| `menu.py` | Text-menu interface to run everything without AI |
| `server.py` | MCP server exposing all features as AI-callable tools |

## Running it

Requirements: Python 3.10+

An AI-powered home assistant that manages household inventory, chores, and maintenance. Built with free, open tools, it combines **OCR**, **RAG** (document search), and **tool-calling AI agents** connected over **MCP** (Model Context Protocol).

You can talk to it in plain English — *"add milk to my inventory"*, *"what chores are due?"*, *"how do I descale the coffee machine?"* — and an AI model routes each request to the right tool.

## What it does

- **Inventory tracking** — reads grocery receipts with OCR and stores items in a local database.
- **Chore & maintenance scheduling** — tracks recurring tasks and tells you what's due or overdue.
- **Manual search (RAG)** — answers questions about your appliances by searching stored manual text by relevance.
- **AI-driven** — all features are exposed as tools an AI assistant can call through natural language.

## How it works

You give a plain-English request. The AI client reads it, picks the right tool from those exposed by the MCP server, runs the underlying Python function, and replies in natural language.

## Tech stack

- **Python** — core language
- **SQLite** — local, persistent storage
- **Tesseract OCR** — reads text from receipt images
- **scikit-learn (TF-IDF)** — relevance-based document search for the RAG feature
- **MCP (Model Context Protocol)** — exposes the app's functions as tools an AI can call
- **Jan + Gemini (free tier)** — the AI "brain" that drives the tools

All tools used are free.

## Project structure

| File | Purpose |
|------|---------|
| `database.py` | SQLite storage for inventory and tasks |
| `inventory.py` | Turns OCR receipt text into clean stored items |
| `tasks.py` | Chores and maintenance scheduling logic |
| `manuals.py` | RAG document storage and relevance search |
| `menu.py` | Text-menu interface to run everything without AI |
| `server.py` | MCP server exposing all features as AI-callable tools |

## Running it

Requirements: Python 3.10+
pip install scikit-learn "numpy<2" "mcp[cli]" pytesseract Pillowpython menu.py       # text-menu version (no AI needed)
python manuals.py    # load sample manual text for search
python server.py     # MCP server, to connect an AI client

To use it with an AI assistant, connect `server.py` as an MCP server in a client such as [Jan](https://jan.ai), using a tool-calling model (e.g. a free Gemini Flash model).

## Notes

- `numpy<2` is pinned intentionally — newer numpy builds require CPU instruction sets not present on all machines, which can cause silent import crashes across dependent libraries. Pinning to the 1.x line avoids this. (Diagnosing this was the trickiest part of the build.)
- The database and personal data are excluded from version control via `.gitignore`.

## Roadmap

- Wire live receipt-photo OCR directly into the inventory flow
- Ingest real appliance manuals (PDF) into the search index
- Add a shopping-list tool that surfaces low-stock items
- Upgrade RAG from keyword-based (TF-IDF) to embedding-based semantic searchOnce you've saved it, upload it to GitHub with these three commands in the terminal, one at a time:git add README.mdgit commit -m "Add README"git pushThat last git push should just work now since you're already authenticated — no login window this time.Then refresh your GitHub repo page. The README will appear automatically as a nicely formatted front page right below your file list — that's how GitHub works, it displays any README.md as the repo's homepage. You'll see your project title, description, the tech stack, everything, laid out cleanly.Go create the file, paste, save, and run those three commands. Tell me when it's up or if any command shows a red error. Once that README is showing on your repo page, your project is complete and professionally presented — genuinely portfolio-ready.
