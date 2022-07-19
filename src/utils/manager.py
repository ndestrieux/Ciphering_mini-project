import os
import time
from pathlib import Path
from typing import Dict, List

from .buffer import Buffer
from .cipher import Rot13CipherFactory, Rot47CipherFactory
from .menu import CipherMenu, Menu


class Manager:
    DATA_FOLDER = Path("src/utils/data/")

    def __init__(self):
        self.rot47_cipher = Rot47CipherFactory()
        self.rot13_cipher = Rot13CipherFactory()
        self.cipher_menu = CipherMenu()
        self.menu = Menu()
        self.buffer = Buffer()
        self.is_running = True
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
                3: (self.decrypt_from_file,),
                4: (self.read_from_memory,),
                5: (self.exit,),
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
        while self.is_running:
            self.show_menu("MainMenu")

    def exit(self):
        self.is_running = False

    def show_menu(self, which_menu: str):
        choice = self.get_menu.get(which_menu).show()
        self.execute(which_menu, choice)

    def execute(self, which_menu: str, choice: int):
        func, *args = self.options[which_menu].get(choice)
        func(*args)

    @staticmethod
    def get_text() -> str:
        text = input("Text to encrypt:\n")
        return text

    def get_data_from_file(self, file: str) -> List:
        path = Path(f"{self.DATA_FOLDER}/{file}")
        with open(path, "r", encoding="utf-8") as f:
            encrypted_text_list = f.read().splitlines()
        return encrypted_text_list

    def get_data_from_memory(self) -> Dict:
        memory = self.buffer.encrypted_text_dict
        return memory

    @staticmethod
    def display_data(data: Dict):
        print(25 * "=")
        print(25 * "=")
        for key, values in data.items():
            print(key + ":")
            for value in values:
                print(value)
            print(25 * "=")
        input("Hit <Enter> to continue.")

    def encrypt_text(self, encryption_type: str):
        text = self.get_text()
        ciphering = self.encryption_types.get(encryption_type).cipher()
        encrypted_text = ciphering.do_action(text)
        self.buffer.add(encryption_type, encrypted_text)

    def save_to_file(self):
        memory = self.get_data_from_memory()
        for key, values in memory.items():
            file = Path(f"{self.DATA_FOLDER}/{key}")
            with open(file, "a+", encoding="utf-8") as f:
                for value in values:
                    f.write(value + "\n")
        self.buffer.clear()

    def decrypt_from_file(self):
        from_file_to_dict = {}
        file_list = os.listdir(self.DATA_FOLDER)
        for file in file_list:
            encrypted_text_list = self.get_data_from_file(file)
            ciphering = self.encryption_types.get(file).decipher()
            decrypted_text_list = []
            for encrypted_text in encrypted_text_list:
                decrypted_text_list.append(ciphering.do_action(encrypted_text))
            from_file_to_dict[file] = decrypted_text_list
        self.display_data(from_file_to_dict)

    def read_from_memory(self):
        memory = self.get_data_from_memory()
        self.display_data(memory)
