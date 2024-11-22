from voice_control import speak, listen
from task_manager import setup_database, add_task_to_db, delete_task_from_db, list_tasks_from_db

def main():
    setup_database()
    print("Database setup complete. Starting Voice Task Manager...")
    print("Commands: 'add task <task>', 'delete task <task>', 'list tasks', 'exit'")
    speak("Hello! I am ready to help you manage your tasks.")
    
    while True:
        try:
            command = listen()
            if command:
                command = command.lower()
                if 'exit' in command:
                    speak("Goodbye!")
                    break
                elif 'add task' in command:
                    task = command.replace('add task', '').strip()
                    if task:
                        result = add_task_to_db(task)
                        speak(result)
                    else:
                        speak("Please specify a task to add.")
                elif 'delete task' in command:
                    task = command.replace('delete task', '').strip()
                    if task:
                        result = delete_task_from_db(task)
                        speak(result)
                    else:
                        speak("Please specify a task to delete.")
                elif 'list tasks' in command:
                    tasks = list_tasks_from_db()
                    if "No tasks available" in tasks:
                        speak("You have no tasks at the moment.")
                    else:
                        speak("Here are your tasks.")
                        speak(tasks)
                    print(tasks)
                else:
                    speak("I didn't understand that. Please try again.")
        except Exception as e:
            speak("Sorry, I couldn't process that. Please try again.")
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
