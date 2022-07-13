import time
from .menu import Menu, SubMenu
from .buffer import Buffer


class Manager:
    def __init__(self):
        self.submenu = SubMenu(self)
        self.menu = Menu(self)
        self.buffer = Buffer()

    def start(self):
        print("Welcome!")
        time.sleep(1)
        self.show_menu()

    def show_menu(self):
        self.menu.show()

    def encrypt_text(self):
        pass

    def decrypt_text(self):
        pass

    def save_to_file(self):
        print("Save to file.")

    def read_from_file(self):
        print("Read from file.")

    def read_from_memory(self):
        print("Read from memory.")
