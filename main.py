from abc import ABC, abstractmethod
from typing import List  

class IUser(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Повертає ім'я користувача"""
        pass

    @name.setter
    @abstractmethod
    def name(self, value: str):
        """Встановлює ім'я користувача"""
        pass

    @abstractmethod
    def display_info(self):
        """Виводить інформацію про користувача"""
        pass


class ITask(ABC):
    @property
    @abstractmethod
    def description(self) -> str:
        """Опис завдання"""
        pass

    @description.setter
    @abstractmethod
    def description(self, value: str):
        pass

    @property
    @abstractmethod
    def is_completed(self) -> bool:
        """Статус виконання"""
        pass

    @is_completed.setter
    @abstractmethod
    def is_completed(self, value: bool):
        pass

    @abstractmethod
    def complete(self):
        """Позначити завдання виконаним"""
        pass


class IProject(ABC):
    @property
    @abstractmethod
    def title(self) -> str:
        """Назва проєкту"""
        pass

    @title.setter
    @abstractmethod
    def title(self, value: str):
        pass

    @abstractmethod
    def add_task(self, task: ITask):
        """Додає завдання в проєкт"""
        pass

# --- РЕАЛІЗАЦІЯ ---

class User(IUser):
    """ Реалізація інтерфейсу IUser. """
    
    def __init__(self, name: str):
        self._name = None
        self.name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Ім'я користувача не може бути порожнім")
        self._name = value.strip()

    def display_info(self):
        print(f"Користувач: {self.name}")


class Task(ITask):
    """ Реалізація інтерфейсу ITask. """
    
    def __init__(self, description: str):
        self._description = None
        self.description = description
        self._is_completed = False

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str):
        if not value or not value.strip():
            raise ValueError("Опис завдання не може бути порожнім")
        self._description = value.strip()

    @property
    def is_completed(self) -> bool:
        return self._is_completed

    @is_completed.setter
    def is_completed(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("Статус виконання має бути boolean")
        self._is_completed = value

    def complete(self):        
        self.is_completed = True

    def __str__(self):
        status = "Виконано" if self.is_completed else "Не Виконано"
        return f"{self.description} — {status}"


class Project(IProject):
    """ Реалізація інтерфейсу IProject. """
    
    def __init__(self, title: str):
        self._title = None
        self.title = title
        self._tasks: List[ITask] = [] # Тепер List працюватиме коректно

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, value: str):
        if not value or not value.strip():
            raise ValueError("Назва проекту не може бути порожньою")
        self._title = value.strip()

    def add_task(self, task: ITask):
        if not isinstance(task, ITask):
            raise TypeError("Можна додавати лише завдання типу ITask")
        self._tasks.append(task)

    def show_tasks(self):
        print(f"\nПроект: {self.title}")
        if not self._tasks:
            print("Завдання немає")
            return

        for idx, task in enumerate(self._tasks, start=1):
            print(f"{idx}. {task}")
