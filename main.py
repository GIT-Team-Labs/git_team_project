if __name__ == '__main__':
    from abc import ABC, abstractmethod
    from typing import List


    class IUser(ABC):
        @property
        @abstractmethod
        def name(self) -> str:
            """ Повертає ім'я користувача """
            pass

        @name.setter
        @abstractmethod
        def name(self, value: str):
            """ Встановлює ім'я користувача """
            pass

        @abstractmethod
        def display_info(self):
            """ Виводить інформацію про користувача """
            pass


    class ITask(ABC):
        @property
        @abstractmethod
        def description(self) -> str:
            """ Опис завдання """
            pass

        @description.setter
        @abstractmethod
        def description(self, value: str):
            pass

        @property
        @abstractmethod
        def is_completed(self) -> bool:
            """ Статус виконання """
            pass

        @is_completed.setter
        @abstractmethod
        def is_completed(self, value: bool):
            pass

        @abstractmethod
        def complete(self):
            """ Позначити завдання виконаним """
            pass


    class IProject(ABC):
        @property
        @abstractmethod
        def title(self) -> str:
            """ Назва проєкту """
            pass

        @title.setter
        @abstractmethod
        def title(self, value: str):
            pass

        @abstractmethod
        def add_task(self, task: ITask):
            """ Додає завдання в проєкт """
            pass

# РЕАЛИЗАЦіЯ

class User(IUser):
    
    """ Реалізація інтерфейсу IUser.
    Цей клас представляє реального користувача системи.
    Він зберігає ім'я користувача та вміє виводити інформацію про себе. """
    
    def __init__(self, name: str):
        # Використовуємо setter, щоб одразу застосувати валідацію
        self.name = name

    @property
    def name(self) -> str:
        # Повертаємо приватне поле _name
        return self._name

    @name.setter
    def name(self, value: str):
        # Перевіряємо, що ім'я не порожнє
        if not value or not value.strip():
            raise ValueError("Ім'я користувача не може бути порожнім")
        self._name = value.strip()

    def display_info(self):
        # Просте виведення інформації про користувача
        print(f"Користувач: {self.name}")


class Task(ITask):
    
    """ Реалізація інтерфейсу ITask.
    Клас описує одне завдання:
    - Текст завдання
    - виконана вона чи ні """
    
    def __init__(self, description: str):
        # Встановлюємо опис завдання
        self.description = description
        
        # За замовчуванням завдання НЕ виконано
        self._is_completed = False

    @property
    def description(self) -> str:
        # Повертаємо опис завдання
        return self._description

    @description.setter
    def description(self, value: str):
        # Перевіряємо, що опис не порожній
        if not value or not value.strip():
            raise ValueError("Опис завдання не може бути порожнім")
        self._description = value.strip()

    @property
    def is_completed(self) -> bool:
        # Повертаємо статус виконання
        return self._is_completed

    @is_completed.setter
    def is_completed(self, value: bool):
        # Перевіряємо, що передано boolean
        if not isinstance(value, bool):
            raise ValueError("Статус виконання має бути boolean")
        self._is_completed = value

    def complete(self):        
        
        """ Позначає завдання як виконане. Використовує setter is_completed. """
        
        self.is_completed = True

    def __str__(self):
        # Текстове подання задачі        
        status = "Виконано" if self.is_completed else "Не Виконано"
        return f"{self.description} — {status}"


class Project(IProject):
    
    """ Реалізація інтерфейсу IProject.
    Проект:
    - має назву
    - Містить список завдань
    - дозволяє додавати завдання """
    
    def __init__(self, title: str):
        # Встановлюємо назву проекту
        self.title = title
        
        # Зберігаємо завдання у списку
        self._tasks: List[ITask] = []

    @property
    def title(self) -> str:
        # Повертаємо назву проекту
        return self._title

    @title.setter
    def title(self, value: str):
        # Перевіряємо, що назва не порожня
        if not value or not value.strip():
            raise ValueError("Назва проекту не може бути порожньою")
        self._title = value.strip()

    def add_task(self, task: ITask):
        
        """ Додає завдання до проекту. Приймає будь-який об'єкт, що реалізує інтерфейс ITask. """
        
        if not isinstance(task, ITask):
            raise TypeError("Можна додавати лише завдання типу ITask")
        self._tasks.append(task)

    def show_tasks(self):
        
        """ Виводить перелік завдань проекту. """
        
        print(f"\nПроект: {self.title}")
        if not self._tasks:
            print("Завдання немає")
            return

        for idx, task in enumerate(self._tasks, start=1):
            print(f"{idx}. {task}")

    def count_completed_tasks(self) -> int:
        return len([t for t in self._tasks if t.is_completed])
