from abc import ABC, abstractmethod
from Entity import Todolist
from Repository import TodolistRepositoryImpl

class TodolistService(ABC) :

    @abstractmethod
    def showTodolist(self) -> None :
        pass

    @abstractmethod
    def addTodolist(self) -> None :
        pass

    @abstractmethod
    def removeTodolist(seld) -> None :
        pass

class TodolistServiceImpl(TodolistService) :

    def __init__(self, todolistRepository:TodolistRepositoryImpl) -> None:
        self.__todolistRepository = todolistRepository
    
    def showTodolist(self) -> None:
        print("TODOLIST")
        for i in self.__todolistRepository.findAll() :
            print(f"{i[0]}. {i[1]}")
    
    def addTodolist(self, todo:str) -> None:
        todolist = Todolist(todo)
        self.__todolistRepository.save(todolist)
        print("SUKSESS MENAMBAH TODO")

    def removeTodolist(self, number:int) -> None:
        if self.__todolistRepository.remove(number) :
            print("SUKSES MENGHAPUS TODO")
        else :
            print("GAGAL MENGHAPUS TODO")