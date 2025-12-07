if __name__ == '__main__':
    from abc import ABC, abstractmethod

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
