import time, os, json

tasks = []

def load():
  try:  
    with open('tasks.json', 'r') as f:
      return json.load(f)
  except FileNotFoundError:  
    return []

tasks = load()

def save():
  with open('tasks.json', 'w') as f:
    json.dump(tasks, f, indent=4)

def add():
  time.sleep(1)
  os.system("clear")
  task = input("Task: ").title()
  due = input("Due by: ")
  priority = input("Priority (low, medium, high): ").capitalize()

  row = {
    "task": task,
    "due":due,
    "priority": priority
    }
  tasks.append(row)
  save()
  print("Task Successfully added")


def view():
  time.sleep(1)
  os.system('clear')

  if not tasks:
    print("No tasks found")
    return

  print("1: View All \n2: View Priority\n")
  
  menu = input("> ")

  if menu == '1':
    print(f"{'Task':^15} | {'Due':^15} | {'Priority':^10}")
    print("-" * 50)
    for row in tasks:
      print(f"{row['task']:^15} | {row['due']:^15} | {row['priority']:^10}")
    print()
  elif menu == '2':
    priority = input('See low, medium, or high priority tasks: ').capitalize()
    
    print(f"{'Task':^15} | {'Due':^15} | {'Priority':^10}")
    print("-" * 50)
    
    for row in tasks:
      if row['priority'] == priority:
        print(f"{row['task']:^15} | {row['due']:^15} | {row['priority']:^10}")
    print()
      
  else:
    print("Make a valid selection")
  time.sleep(1)


def remove():
  time.sleep(1)
  os.system("clear")
  name = input("Name of task to remove: ").lower()
  for row in tasks:
    if name in row['task'].lower():
      print(f"\n{name} has been deleted\n")
      tasks.remove(row)
      save()


def edit():
  time.sleep(1)
  os.system("clear")
  name = input("Name of task to edit: ").lower()

  for row in tasks:
    if row['task'].lower() == name:
      type = input("Edit: \n1: Name \n2: Date \n3: Priority\n")
      if type == '1':
        print(f"Change {row['task']} to: ")
        row['task'] = input("> ").title()
      elif type == '2':
        print(f"Change {row['due']} to: ")
        row['due'] = input("> ")
      elif type == '3':
        print(f"Change {row['priority']} to: ")
        row['priority'] = input("> ").capitalize()
      save()
      print("Task updated successfully")
      break
  else:
    print("Task Not Found")

def main()
  while True:
    print("tasks List Management System\n")
    print("1: Add \n2: View \n3: Remove \n4: Edit \n5: Exit \n")

    menu = input("> ")

    if menu == '1':
      add()
    elif menu == '2':
      view()
    elif menu == '3':
      remove()
    elif menu == '4':
      edit()
    elif menu == '5':
      break
    else:
      print("Make a valid selection")
      continue

    time.sleep(3)
    os.system("clear")
    
if --__name__ == "__main__":
  main()
