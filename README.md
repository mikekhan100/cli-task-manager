# CLI Task Manager

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Status](https://img.shields.io/badge/Status-Active-success)

A command-line task management application built with Python. This project demonstrates fundamental Python concepts including file I/O, JSON handling, error handling, and user input validation.

## Features

- ✅ Add tasks with automatic timestamping
- 🚦 Priority levels (High, Medium, Low) with color-coded display
- 📋 View all tasks with status indicators
- ✔️ Mark tasks as complete
- 🗑️ Delete tasks
- 📊 Export tasks to CSV for use in Excel/Google Sheets
- 💾 Persistent storage using JSON
- 🛡️ Input validation and error handling

## Demo
```bash
$ python task_manager.py

🎯 Welcome to Task Manager!

============================================================
TASK MANAGER
============================================================
1. Add a task
2. View all tasks
3. Mark task as complete
4. Delete a task
5. Export to CSV
6. Exit
============================================================

Enter your choice (1-6): 1
Enter task description: Complete Python portfolio project

Select priority:
1. High
2. Medium
3. Low
Enter priority (1-3, default is Medium): 1
✓ Task added successfully! (ID: 1, Priority: High)
```

## Installation
```bash
# Clone the repository
git clone https://github.com/mikekhan100/task-manager.git

# Navigate to the directory
cd task-manager

# Run the program (Python 3.x required)
python task_manager.py
```

## Usage
Adding a Task
1. Select option 1 from the main menu
2. Enter your task description
3. Choose priority level (1-3)
4. Task is automatically saved with timestamp

## Viewing Tasks
- Select option 2 to see all tasks
- Tasks display with color-coded priorities:
    -🔴 High (Red) - Urgent tasks
    -🟡 Medium (Yellow) - Normal priority
    -🟢 Low (Green) - Can wait

## Completing Tasks
1. Select option 3
2. Enter the task ID
3. Task is marked complete with completion timestamp

## Exporting to CSV
1. Select option 5
2. Enter filename (or press Enter for default "tasks.csv")
3. Open the file in Excel, Google Sheets, or any spreadsheet program

## Project Structure
task-manager/
├── task_manager.py    # Main application
├── README.md          # Project documentation
├── .gitignore         # Git ignore rules
├── tasks.json         # Task storage (created on first run)
└── LICENSE            # MIT License

## Technologies Used
- Python 3.14
- Built-in libraries:
    - json - Data persistence
    - os - File system operations
    - datetime - Timestamp generation
    - csv - Export functionality

## Skills Acquired
Python Fundamentals
- Working with Python lists and dictionaries
- File I/O operations and the `with` statement
- JSON serialisation and deserialisation
- Dictionary constants and mappings
- ANSI color codes for terminal output

Error Handling & Validation
- Try/except blocks for robust error handling
- Input validation with default values
- Backwards compatibility with .get() method
- Graceful handling of corrupted data files

Code Organisation
- Modular function design
- Single responsibility principle
- Clear separation of concerns
- Professional code documentation

Data Management
- Persistent storage with JSON
- CSV export for interoperability
- Data structure design
- Handling optional fields

## Development History
v1.0 - Initial release
- Basic CRUD operations
- JSON persistence
- Task completion tracking

v1.1 - Priority feature
- Added High/Medium/Low priority levels
- Color-coded terminal display
- Priority validation with defaults

v1.2 - CSV Export
- Export tasks to spreadsheet format
- Custom filename support
- Excel/Google Sheets compatible

## Future Enhancements
- [✅] Add task priority levels
- [ ] Filter tasks by status or priority
- [ ] Add due dates with overdue warnings
- [ ] Implement task categories/tags
- [ ] Search functionality
- [✅] Export to CSV
- [ ] Recurring tasks

## Requirements
- Python 3.x (tested on Python 3.14)
- No external dependencies - uses only built-in libraries

## License
This project is licensed under the MIT License

## Author
Michael Khan (https://github.com/mikekhan100)

## Contact
GitHub: https://github.com/mikekhan100
LinkedIn: https://www.linkedin.com/in/mikekhan100/
Email: mike.khan100@gmail.com