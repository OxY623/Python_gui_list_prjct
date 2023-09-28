# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, \
    QListWidget, QListWidgetItem, QMessageBox

# Установка переменной среды DJANGO_SETTINGS_MODULE для указания настроек Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "list_prjct.settings")

import django
from django.conf import settings

# Инициализация Django
django.setup()
# settings.configure()

# Импорт модели после инициализации Django
from list_app.models import Item


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Daily Task")

        # Создание главного виджета
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Установка темного фона
        self.central_widget.setStyleSheet("background-color: #333333;")

        # Создание вертикального макета
        layout = QVBoxLayout()
        layout.setContentsMargins(80, 20, 80, 30)
        layout.setSpacing(20)

        # Создание виджетов
        title_label = QLabel("Daily Tasks")
        title_label.setStyleSheet("font-size: 24px; text-align: center; margin: 10px; color: #FFFFFF;")
        layout.addWidget(title_label)

        self.title_input = QLineEdit()
        self.title_input.setStyleSheet("color: #FFFFFF;")
        layout.addWidget(self.title_input)

        self.item_list = QListWidget()
        self.item_list.setStyleSheet("background-color: #FFFFFF;")
        layout.addWidget(self.item_list)

        add_button = QPushButton("Add")
        add_button.clicked.connect(self.add_item)
        add_button.setStyleSheet("background-color: #0074D9; color: #FFFFFF; height:18px;")
        layout.addWidget(add_button)

        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(self.confirm_delete)
        delete_button.setStyleSheet("background-color: #0074D9; color: #FFFFFF; height:18px;")
        layout.addWidget(delete_button)

        # Применение макета к центральному виджету
        self.central_widget.setLayout(layout)

        # Загрузка списка задач при запуске приложения
        self.load_items()

    def add_item(self):
        title = self.title_input.text()
        if title:
            item = Item(title=title)
            item.save()
            self.title_input.clear()
            self.load_items()

    def load_items(self):
        self.item_list.clear()
        items = Item.objects.all()
        for item in items:
            list_item = QListWidgetItem(item.title)
            self.item_list.addItem(list_item)

    def delete_item(self):
        selected_items = self.item_list.selectedItems()
        if not selected_items:
            QMessageBox.information(self, "ERROR", "The item to delete is not selected.", QMessageBox.Ok)
            return

        confirm_dialog = QMessageBox.question(self, "DELETE", "Are you sure you want to delete this?",
                                              QMessageBox.Yes | QMessageBox.No)
        if confirm_dialog == QMessageBox.Yes:
            title = selected_items[0].text()
            item = Item.objects.get(title=title)
            item.delete()
            self.load_items()

    def confirm_delete(self):
        self.delete_item()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Запуск главного окна приложения
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
