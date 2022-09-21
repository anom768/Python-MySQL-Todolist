class Todolist() :

    def __init__(self, todo:str = "") -> None:
        self.__id = 0
        self.__todo = todo
    
    def setId(self, id:int) -> None :
        self.__id = id
    
    def getId(self) -> int :
        return self.__id
    
    def setTodo(self, todo:str) -> None :
        self.__todo = todo

    def getTodo(self) -> str :
        return self.__todo