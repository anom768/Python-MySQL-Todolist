from Service import TodolistServiceImpl
from Repository import TodolistRepositoryImpl
from Config import Database

class ServiceTest() :

    def __init__(self) -> None:
        self.__repository = TodolistRepositoryImpl(Database.getConnection())
        self.__service = TodolistServiceImpl(self.__repository)
    
    def testShowTodolist(self) :
        self.__service.showTodolist()
    
    def testAddTodolist(self) :
        self.__service.addTodolist("Satu")
        self.__service.addTodolist("Dua")
        self.__service.addTodolist("Tiga")
        self.__service.showTodolist()
    
    def testRemoveTodolist(self) :
        self.__service.removeTodolist(3)
        self.__service.removeTodolist(0)
        self.__service.removeTodolist(1)
        self.__service.removeTodolist(6)
        self.__service.showTodolist()

test = ServiceTest()
test.testRemoveTodolist()