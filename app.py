from models import (
    load_users, 
    create_user,
    save_users,
    load_tasks,
    save_tasks,
)

todos = []
stop = False

def get_todos():
    global todos
    return todos

def delete_task(number_to_delete):
    # your code here
    pass

def save_todos():
    # your code here
    pass

    
def load_todos():
    # your code here
    pass

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    # cargar todos los usuarios desde users_lists.json
    users = load_users()
    current_user = None
    # si no hay usuarios, o no hay archivo:
    if len(users) == 0:
        # crear el primer usuario
        current_user = create_user()
        users.append(current_user)
    else:
        while current_user is None:
            # listar los usuarios para escoger uno
            index = 0
            for user in users:
                print(f"{index + 1}. {user.name}")
                index += 1
            print(f"{index + 1}. Crear un usuario nuevo")
            index += 1
            print(f"{index + 1}. Eliminar un usuario")
            index += 1

            choice = int(input("escoja un usuario por su número:\n"))
            if choice in range(1, index - 1):
                # el usuario escogió un usuario
                current_user = users[choice - 1]
            elif choice == index - 1:
                # el usuario escogió crear un nuevo usuario
                current_user = create_user()
                users.append(current_user)
            elif choice == index:
                # el usuario escogió borrar un usuario
                if len(users) > 0:
                    # hay usuarios que borrar
                    index_to_delete = int(input("escoja el usuario a eliminar:\n"))
                    if index_to_delete in range(1, index - 1):
                        # escogio un index valido
                        # users = list(filter(lambda user, i: i != index_to_delete - 1))
                        users = list(filter(lambda user: user.id != users[index_to_delete - 1].id, users))
                    else: current_user = None                  
                else:
                    current_user = None
            else:
                current_user = None

    # ya tenemos un usuario escogido
    print(f"Bienvenido, {current_user.name}")
    # cargamos todas las tareas
    todos = load_tasks()
    print(todos)
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
        7. Print all tasks for all users
    """)
        response = input()
        if response == "6":
            save_users(users)
            save_tasks(todos)
            stop = True
        elif response == "3":
            current_user.print_list(todos)
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            new_task = current_user.add_task(title)
            print(new_task.serialize())
            todos.append(new_task)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        elif response == "7":
            current_user.print_list(todos, users)
        else:
            print("Invalid response, asking again...")