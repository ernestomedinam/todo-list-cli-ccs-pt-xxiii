from base64 import b64encode
import os, json

class Base():

    def __init__(self):
        self.id = b64encode(os.urandom(32)).decode("utf-8")

class UserList(Base):
    
    def __init__(self, name):
        super().__init__()
        self.name = name

    @classmethod
    def create(cls):
        """ 
            pide el nombre del usuario, al usuario,
            y con este nombre crea una instancia de
            UserList y la devuelve.
        """
        name = input("¿cuál es el nombre del usuario?\n")
        new_user = cls(name)
        return new_user        

    def add_task(self, label):
        """ crea una tarea para este usuario """
        new_task = Task(label, self.id)
        return new_task
    
    def complete_task(self, task):
        task.done = True
        return task

    def delete_task():
        pass

    def print_list(self, tasks, users = []):
        """ 
            imprime las tareas del usuario si all = False,
            imprime las tareas de todos los usuarios si 
            all = True.
        """
        if len(users) == 0:
            # imprimimos las tareas de este usuario
            user_tasks = list(filter(
                lambda task: task.user_list_id == self.id,
                tasks
            ))
            for task in user_tasks:
                if task.done:
                    print(f"✔ {task.label}")
                else:
                    print(f"✖ {task.label}")
        else:
            # imprimimos todas las tareas
            for user in users:
                print(f"\nLas tareas de {user.name}:")
                print(f"==================================")
                user_tasks = list(filter(
                    lambda task: task.user_list_id == user.id,
                    tasks
                ))
                for task in user_tasks:
                    if task.done:
                        print(f"✔ {task.label}")
                    else:
                        print(f"✖ {task.label}")



    def delete():
        pass

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Task(Base):

    def __init__(self, label, user_list_id):
        super().__init__()
        self.label = label
        self.done = False
        self.result = None
        self.user_list_id = user_list_id

    def serialize(self):
        return {
            "id": self.id,
            "user_list_id": self.user_list_id,
            "label": self.label,
            "done": self.done,
            "result": self.result if self.result is not None else ""
        }

def load_users():
    """ 
        carga todos los diccionarios del archivo 
        users_lists.json y crea instancias de UserList
        con estos diccionarios y devuelve una lista
        con estos objetos users_lists.
    """
    users = []
    if os.path.isfile(os.path.join(os.getcwd(), "users_lists.json")):
        # existe, abrimos el archivo
        users_lists_dictionaries = []
        with open(os.path.join(os.getcwd(), "users_lists.json"), "r") as users_file:
            users_lists_dictionaries = json.load(users_file)
        for dictionary in users_lists_dictionaries:
            new_user = UserList(dictionary["name"])
            new_user.id = dictionary["id"]
            users.append(new_user)
        return users
    else:
        # no existe, return None
        return users

def create_user():
    return UserList.create()

def save_users(users):
    """
        abre/crea el archivo users_lists.json y guarda
        la lista de diccionarios que representan a los
        usuarios.
    """
    with open(os.path.join(os.getcwd(), "users_lists.json"), "w") as users_file:
        users_as_dictionaries = []
        for user in users:
            users_as_dictionaries.append(user.serialize())
        json.dump(users_as_dictionaries, users_file)
         
def load_tasks():
    """ 
        carga todos los diccionarios del archivo 
        tasks.json y crea instancias de Task
        con estos diccionarios y devuelve una lista
        con estos objetos tasks.
    """
    tasks = []
    if os.path.isfile(os.path.join(os.getcwd(), "tasks.json")):
        # existe, abrimos el archivo
        tasks_as_dictionaries = []
        with open(os.path.join(os.getcwd(), "tasks.json"), "r") as tasks_file:
            tasks_as_dictionaries = json.load(tasks_file)
        for dictionary in tasks_as_dictionaries:
            new_task = Task(dictionary["label"], dictionary["user_list_id"])
            new_task.id = dictionary["id"]
            new_task.done = bool(dictionary["done"])
            # if dictionary["result"] != "":
            #     new_task.result = dictionary["result"]
            # else:
            #     new_task.result = None
            new_task.result = dictionary["result"] if dictionary["result"] != "" else None

            tasks.append(new_task)
        return tasks
    else:
        # no existe, return None
        return tasks

def save_tasks(tasks):
    """
        abre/crea el archivo tasks.json y guarda
        la lista de diccionarios que representan a las
        tareas.
    """
    with open(os.path.join(os.getcwd(), "tasks.json"), "w") as tasks_file:
        tasks_as_dictionaries = []
        for task in tasks:
            tasks_as_dictionaries.append(task.serialize())
        json.dump(tasks_as_dictionaries, tasks_file)