# Cli-To

A simple command line todo application built in Python. Manage your tasks efficiently from the command line with persistent storage.

## Features

- ✅ Add new todo items
- 📋 List all todos or only pending ones
- ✓ Mark todos as completed
- 🗑️ Remove todos
- 💾 Persistent storage using JSON
- 🎨 Clean, intuitive interface

## Installation

Clone the repository:

```bash
git clone https://github.com/Bennnto/Cli-To.git
cd Cli-To
```

Make the script executable:

```bash
chmod +x todo
```

## Usage

### Basic Commands

```bash
# Add a new todo
./todo add "Buy groceries"
./todo add "Write documentation"

# List all todos
./todo list

# List only pending (incomplete) todos
./todo list --pending

# Complete a todo (mark as done)
./todo complete 1

# Remove a todo completely
./todo remove 2
```

### Alternative Usage

You can also run the application directly with Python:

```bash
python3 cli_to.py add "Your task here"
python3 cli_to.py list
python3 cli_to.py complete 1
python3 cli_to.py remove 1
```

### Help

Get help for any command:

```bash
./todo --help
./todo add --help
./todo list --help
```

## Examples

```bash
# Add some todos
./todo add "Buy groceries"
./todo add "Write report"
./todo add "Call dentist"

# List all todos
./todo list
# Output:
# Todos:
# --------------------------------------------------
# ○ [1] Buy groceries
# ○ [2] Write report  
# ○ [3] Call dentist

# Complete the first todo
./todo complete 1

# List todos again
./todo list
# Output:
# Todos:
# --------------------------------------------------
# ✓ [1] Buy groceries
# ○ [2] Write report
# ○ [3] Call dentist

# List only pending todos
./todo list --pending
# Output:
# Todos:
# --------------------------------------------------
# ○ [2] Write report
# ○ [3] Call dentist

# Remove a todo
./todo remove 3

# Final list
./todo list
# Output:
# Todos:
# --------------------------------------------------
# ✓ [1] Buy groceries
# ○ [2] Write report
```

## Data Storage

Todos are stored in a `todos.json` file in the same directory as the script. Each todo contains:

- `id`: Unique identifier
- `description`: Todo description
- `completed`: Completion status
- `created_at`: Creation timestamp
- `completed_at`: Completion timestamp (if completed)

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Contributing

Feel free to submit issues and enhancement requests!