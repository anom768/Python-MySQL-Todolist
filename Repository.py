from Entity import Todolist
from abc import ABC, abstractmethod
from Config import Database

class TodolistRepository(ABC) :

    @abstractmethod
    def save(self) -> None :
        pass

    @abstractmethod
    def remove(self) -> bool :
        pass

    @abstractmethod
    def findAll(self) -> list :
        pass

class TodolistRepositoryImpl(TodolistRepository) :

    def __init__(self, connection:Database) -> None:
        super().__init__()
        self.connection = connection

    def save(self, todo:Todolist) -> None :
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO todolist(todo) VALUES(%s)",[todo.getTodo()])
        self.connection.commit()
    
    def remove(self, number:int) -> bool :
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM todolist WHERE id = %s", [number])
        if cursor.fetchone() :
            cursor.execute("DELETE FROM todolist WHERE id = %s",[number])
            self.connection.commit()
            return True
        else :
            return False
    
    def findAll(self) -> list:
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM todolist")
        result = []
        for i in cursor :
            result.append(i)
        
        return result