import time

from .exceptions import ChoiceOutOfRange


class Menu:
    MENU_CONTEXT = {
        1: "Encrypt plain text (ROT47/ROT13)",
        2: "Save encrypted texts to file",
        3: "Decrypt encrypted texts from file",
        4: "Print encrypted texts stored in memory",
        5: "Exit",
    }

    def show(self) -> int:
        for key, value in self.MENU_CONTEXT.items():
            print(f"{key}. {value}")
        return self.get_choice()

    def get_choice(self) -> int:
        default = 0
        try:
            choice = int(
                input(
                    "Please choose an option by typing the associated number and then press <Enter>:\n"
                )
            )
        except ValueError:
            print("Invalid choice. It should be a number.")
            time.sleep(1)
            return default
        choice_list = list(self.MENU_CONTEXT.keys())
        try:
            if choice not in choice_list:
                raise ChoiceOutOfRange(choice_list)
            return choice
        except ChoiceOutOfRange as e:
            print(e)
            time.sleep(1)
            return default


class CipherMenu(Menu):
    MENU_CONTEXT = {
        1: "Use ROT47",
        2: "Use ROT13",
        3: "Go back",
    }
