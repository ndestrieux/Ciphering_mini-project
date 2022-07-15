import time
import sys
from typing import Dict
from .menu import Menu, CipherMenu
from .cipher import Rot47CipherFactory, Rot13CipherFactory
from .buffer import Buffer


class Manager:
    def __init__(self):
        self.rot47_cipher = Rot47CipherFactory()
        self.rot13_cipher = Rot13CipherFactory()
        self.cipher_menu = CipherMenu()
        self.menu = Menu()
        self.buffer = Buffer()
        self._options = self.options
        self._get_menu = self.get_menu
        self._encryption_types = self.encryption_types

    @property
    def options(self) -> Dict:
        options_dict = {
            "MainMenu": {
                0: (self.show_menu, "MainMenu"),
                1: (self.show_menu, "CipherMenu"),
                2: (self.save_to_file,),
                3: (self.decript_from_file,),
                4: (self.read_from_memory,),
                5: (sys.exit,),
            },
            "CipherMenu": {
                0: (self.show_menu, "CipherMenu"),
                1: (self.encrypt_text, "ROT47"),
                2: (self.encrypt_text, "ROT13"),
                3: (self.show_menu, "MainMenu"),
            },
        }
        return options_dict

    @property
    def get_menu(self) -> Dict:
        menu_dict = {
            "MainMenu": self.menu,
            "CipherMenu": self.cipher_menu,
        }
        return menu_dict

    @property
    def encryption_types(self) -> Dict:
        encryption_types_dict = {
            "ROT47": self.rot47_cipher,
            "ROT13": self.rot13_cipher,
        }
        return encryption_types_dict

    def start(self):
        print("Welcome!")
        time.sleep(1)
        self.show_menu("MainMenu")

    def show_menu(self, which_menu: str):
        choice = self.get_menu.get(which_menu).show()
        self.execute(which_menu, choice)

    def execute(self, which_menu, choice):
        func, *args = self.options[which_menu].get(choice)
        func(*args)

    @staticmethod
    def get_text() -> str:
        text = input("Text to encrypt:\n")
        return text

    def encrypt_text(self, encryption_type: str):
        text = self.get_text()
        ciphering = self.encryption_types.get(encryption_type).cipher()
        encrypted_text = ciphering.do_cipher(text)
        self.buffer.add(encryption_type, encrypted_text)
        self.show_menu("MainMenu")

    def save_to_file(self):
        print("Save to file.")

    def decript_from_file(self):
        print("Read from file.")

    def read_from_memory(self):
        print(self.buffer)
        time.sleep(2)
        self.show_menu("MainMenu")
