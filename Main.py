
# 🎯 Personal Task Manager

A complete Python command-line task management application that helps you stay organized and productive!

## ✨ Features

- ➕ **Add Tasks** with priority levels (High, Medium, Low)
- 📋 **View Tasks** - see pending or all tasks
- ✅ **Complete Tasks** - mark tasks as done
- 🗑️ **Delete Tasks** - remove unwanted tasks
- 📊 **Statistics** - track your productivity
- 💾 **Data Persistence** - tasks saved to JSON file
- 🎨 **Clean Interface** - emoji-rich, user-friendly display

## 🚀 Quick Start

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd personal-task-manager
   ```

2. **Run the application:**
   ```bash
   python main.py
   ```

3. **Start managing your tasks!**

## 📸 Screenshot

```
==================================================
🎯 PERSONAL TASK MANAGER
==================================================
1. Add Task
2. View Pending Tasks
3. View All Tasks
4. Complete Task
5. Delete Task
6. View Statistics
7. Exit
--------------------------------------------------
```

## 🛠️ Requirements

- Python 3.11 or higher
- No external dependencies required! Uses only Python standard library.

## 📁 Project Structure

```
personal-task-manager/
├── main.py          # Main application code
├── tasks.json       # Task data storage (auto-generated)
├── README.md        # This file
└── pyproject.toml   # Project configuration
```

## 🎮 Usage

### Adding Tasks
- Choose option 1 from the menu
- Enter your task description
- Set priority: `high`, `medium`, or `low`

### Viewing Tasks
- **Option 2**: View only pending tasks
- **Option 3**: View all tasks (including completed)

### Managing Tasks
- **Option 4**: Mark tasks as complete
- **Option 5**: Delete tasks permanently
- **Option 6**: View productivity statistics

## 💡 Code Features

This project demonstrates:
- **Object-Oriented Programming** with the `TaskManager` class
- **File I/O** with JSON data persistence
- **Error Handling** and input validation
- **Data Structures** using lists and dictionaries
- **Date/Time Management** with the `datetime` module
- **Clean Code Practices** with proper documentation

## 🔧 Technical Details

- **Language**: Python 3.11+
- **Storage**: JSON file (`tasks.json`)
- **Architecture**: Class-based design with separation of concerns
- **Error Handling**: Comprehensive try-catch blocks
- **Input Validation**: Type checking and range validation

## 🌟 Future Enhancements

Ideas for extending this project:
- 📅 Due dates and reminders
- 🏷️ Task categories/tags
- 🔍 Search and filter functionality
- 📊 Advanced analytics and reporting
- 📤 Export to CSV/TXT formats
- 🔄 Recurring tasks
- ⏱️ Time tracking features

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Built with ❤️ using Python

---

⭐ **Star this repository if you found it helpful!**
