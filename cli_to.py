#!/usr/bin/env python3
"""
Cli-To: A simple command line todo application
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import List, Dict, Any


class TodoManager:
    """Manages todo items with persistence"""
    
    def __init__(self, data_file: str = "todos.json"):
        self.data_file = data_file
        self.todos = self.load_todos()
    
    def load_todos(self) -> List[Dict[str, Any]]:
        """Load todos from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def save_todos(self) -> None:
        """Save todos to JSON file"""
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.todos, f, indent=2)
        except IOError as e:
            print(f"Error saving todos: {e}", file=sys.stderr)
    
    def add_todo(self, description: str) -> None:
        """Add a new todo item"""
        # Generate a unique ID by finding the max existing ID and adding 1
        max_id = max([todo['id'] for todo in self.todos], default=0)
        todo = {
            'id': max_id + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().isoformat()
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"Added todo: {description}")
    
    def list_todos(self, show_completed: bool = True) -> None:
        """List all todo items"""
        if not self.todos:
            print("No todos found.")
            return
        
        print("\nTodos:")
        print("-" * 50)
        for todo in self.todos:
            if not show_completed and todo['completed']:
                continue
            
            status = "✓" if todo['completed'] else "○"
            description = todo['description']
            todo_id = todo['id']
            
            print(f"{status} [{todo_id}] {description}")
        print()
    
    def complete_todo(self, todo_id: int) -> None:
        """Mark a todo as completed"""
        todo = self.find_todo_by_id(todo_id)
        if todo:
            todo['completed'] = True
            todo['completed_at'] = datetime.now().isoformat()
            self.save_todos()
            print(f"Completed todo: {todo['description']}")
        else:
            print(f"Todo with ID {todo_id} not found.")
    
    def remove_todo(self, todo_id: int) -> None:
        """Remove a todo item"""
        todo = self.find_todo_by_id(todo_id)
        if todo:
            self.todos.remove(todo)
            self.save_todos()
            print(f"Removed todo: {todo['description']}")
        else:
            print(f"Todo with ID {todo_id} not found.")
    
    def find_todo_by_id(self, todo_id: int) -> Dict[str, Any] or None:
        """Find a todo by its ID"""
        for todo in self.todos:
            if todo['id'] == todo_id:
                return todo
        return None


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Cli-To: A simple command line todo application",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s add "Buy groceries"          # Add a new todo
  %(prog)s list                         # List all todos
  %(prog)s list --pending               # List only pending todos
  %(prog)s complete 1                   # Mark todo #1 as completed
  %(prog)s remove 1                     # Remove todo #1
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Add command
    add_parser = subparsers.add_parser('add', help='Add a new todo')
    add_parser.add_argument('description', help='Todo description')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List todos')
    list_parser.add_argument('--pending', action='store_true', 
                           help='Show only pending todos')
    
    # Complete command
    complete_parser = subparsers.add_parser('complete', help='Mark todo as completed')
    complete_parser.add_argument('id', type=int, help='Todo ID to complete')
    
    # Remove command
    remove_parser = subparsers.add_parser('remove', help='Remove a todo')
    remove_parser.add_argument('id', type=int, help='Todo ID to remove')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    todo_manager = TodoManager()
    
    if args.command == 'add':
        todo_manager.add_todo(args.description)
    
    elif args.command == 'list':
        show_completed = not args.pending
        todo_manager.list_todos(show_completed)
    
    elif args.command == 'complete':
        todo_manager.complete_todo(args.id)
    
    elif args.command == 'remove':
        todo_manager.remove_todo(args.id)


if __name__ == '__main__':
    main()