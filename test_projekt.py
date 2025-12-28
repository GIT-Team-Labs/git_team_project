import unittest
from main import User, Task, Project, ITask

class TestProjectSystem(unittest.TestCase):

    # --- ТЕСТИ КОРИСТУВАЧА (USER) ---

    def test_create_valid_user(self):
        """Перевірка створення коректного користувача"""
        user = User("Олексій")
        self.assertEqual(user.name, "Олексій")

    def test_user_empty_name(self):
        """Перевірка валідації: ім'я не може бути порожнім"""
        # Перевіряємо порожній рядок
        with self.assertRaises(ValueError) as context:
            User("")
        self.assertIn("Ім'я користувача не може бути порожнім", str(context.exception))
        
        # Перевіряємо рядок з пробілів
        with self.assertRaises(ValueError) as context:
            User("   ")
        self.assertIn("Ім'я користувача не може бути порожнім", str(context.exception))

    def test_user_display_info(self):
        """Перевірка методу виведення інформації (через перехоплення print)"""
        # Цей тест трохи складніший, він перевіряє, що функція друкує в консоль
        import io
        import sys
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        user = User("Марія")
        user.display_info()
        
        sys.stdout = sys.__stdout__ # Повертаємо стандартний вивід
        self.assertIn("Користувач: Марія", captured_output.getvalue())

    # --- ТЕСТИ ЗАВДАННЯ (TASK) ---

    def test_create_task(self):
        """Створення завдання та перевірка початкового статусу"""
        task = Task("Написати звіт")
        self.assertEqual(task.description, "Написати звіт")
        self.assertFalse(task.is_completed, "Нове завдання має бути невиконаним")

    def test_task_empty_description(self):
        """Валідація опису завдання"""
        with self.assertRaises(ValueError) as context:
            Task("")
        self.assertIn("Опис завдання не може бути порожнім", str(context.exception))

    def test_task_completion(self):
        """Перевірка зміни статусу завдання"""
        task = Task("Тест")
        task.complete()
        self.assertTrue(task.is_completed)

    def test_task_invalid_status_type(self):
        """Перевірка, що статус може бути тільки boolean"""
        task = Task("Тест")
        with self.assertRaises(ValueError) as context:
            task.is_completed = "Completed" # Передаємо рядок замість bool
        self.assertIn("Статус виконання має бути boolean", str(context.exception))

    def test_task_str_representation(self):
        """Перевірка текстового представлення завдання (Українською)"""
        task = Task("Купити хліб")
        # Перевірка для невиконаного
        self.assertEqual(str(task), "Купити хліб — Не Виконано")
        
        # Перевірка для виконаного
        task.complete()
        self.assertEqual(str(task), "Купити хліб — Виконано")

    # --- ТЕСТИ ПРОЄКТУ (PROJECT) ---

    def test_create_project(self):
        """Створення проєкту"""
        project = Project("Лабораторна 1")
        self.assertEqual(project.title, "Лабораторна 1")
        self.assertEqual(len(project._tasks), 0)

    def test_project_empty_title(self):
        """Валідація назви проєкту"""
        with self.assertRaises(ValueError) as context:
            Project("  ")
        self.assertIn("Назва проекту не може бути порожньою", str(context.exception))

    def test_add_task_to_project(self):
        """Додавання коректного завдання до проєкту"""
        project = Project("Git Course")
        task = Task("Вивчити merge")
        project.add_task(task)
        
        self.assertEqual(len(project._tasks), 1)
        self.assertEqual(project._tasks[0].description, "Вивчити merge")

    def test_add_invalid_task_type(self):
        """Спроба додати щось, що не є завданням (String замість Task)"""
        project = Project("Git Course")
        with self.assertRaises(TypeError) as context:
            project.add_task("Це просто текст")
        self.assertIn("Можна додавати лише завдання типу ITask", str(context.exception))

if __name__ == '__main__':
    unittest.main()
