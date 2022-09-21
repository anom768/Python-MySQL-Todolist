from Repository import TodolistRepositoryImpl
from Service import TodolistServiceImpl
from View import TodolistView
from Config import Database

if __name__ == "__main__" :
    print("APLIKASI TODOLIST")
    repository = TodolistRepositoryImpl(Database.getConnection())
    service = TodolistServiceImpl(repository)
    app = TodolistView(service)
    app.showTodolist()