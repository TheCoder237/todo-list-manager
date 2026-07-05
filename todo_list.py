import time, os, random, json

todo = []

try:  
  with open('tasks.json', 'r') as f:
    todo = json.load(f)
except FileNotFoundError:  
  todo = []

def save():
  with open('tasks.json', 'w') as f:
    json.dump(todo,f,indent=4)

def add():
  time.sleep(1)
  os.system("clear")
  task = input("Task: ").title()
  due = input("Due by: ")
  priority = input("Priority (low, medium, high): ").capitalize()

  row = [task, due, priority]
  todo.append(row)
  save()
  print("Task Successfully added")


def view():
  time.sleep(1)
  os.system('clear')
  print("1: View All \n2: View Priority\n")
  menu = input("> ")

  if menu == '1':
    for row in todo:
      for item in row:
        print(f"{item:^5}", end=" | ")
      print()
    print()
  elif menu == '2':
    priority = input('See low, medium, or high priority tasks: ').capitalize()
    for row in todo:
      if priority in row:
        for item in row:
          print(f"{item:^10}", end="")
        print()
      print()
  else:
    print("Make a valid selection")
  time.sleep(1)


def remove():
  time.sleep(1)
  os.system("clear")
  name = input("Name of task to remove: ").lower()
  for row in todo:
    if name in row:
      print(f"\n{name} has been deleted\n")
      todo.remove(row)
      save()


def edit():
  time.sleep(1)
  os.system("clear")
  name = input("Name of task to edit: ").lower()

  for row in todo:
    if row[0] == name:
      type = input("Edit: \n1: Name \n2: Date \n3: Priority\n")
      if type == '1':
        print(f"Change {row[0]} to: ")
        row[0] = input("> ")
      elif type == '2':
        print(f"Change {row[1]} to: ")
        row[1] = input("> ")
      elif type == '3':
        print(f"Change {row[2]} to: ")
        row[2] = input("> ")
      save()
      print("Task updated successfully")
      break
  else:
    print("Task Not Found")


while True:
  print("TODO List Management System\n")
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
  
  
