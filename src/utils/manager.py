import time
from .menu import Menu, CipherMenu
from .cipher import Rot47CipherFactory, Rot13CipherFactory


class Manager:
    def __init__(self):
        self.rot47_cipher = Rot47CipherFactory(self)
        self.rot13_cipher = Rot13CipherFactory(self)
        self.cipher_menu = CipherMenu(self)
        self.menu = Menu(self)

    def start(self):
        print("Welcome!")
        time.sleep(1)
        self.show_menu()

    def show_menu(self):
        self.menu.show()

    def encrypt_text(self):
        self.cipher_menu.show()

    def save_to_file(self):
        print("Save to file.")

    def decript_from_file(self):
        print("Read from file.")

    def read_from_memory(self):
        print("Read from memory.")
