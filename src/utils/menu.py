import sys


class Menu:
    MENU = {
        1: "Encrypt plain text (ROT47/ROT13)",
        2: "Save encrypted texts to file",
        3: "Decrypt encrypted texts from file",
        4: "Print encrypted texts stored in memory",
        5: "Exit",
    }

    def __init__(self, manager):
        self.manager = manager
        self._options = self.options

    @property
    def options(self):
        option_list = {
            1: self.manager.submenu.show,
            2: self.manager.save_to_file,
            3: self.manager.read_from_file,
            4: self.manager.read_from_memory,
            5: sys.exit,
        }
        return option_list

    def show(self):
        for key, value in self.MENU.items():
            print(f"{key}. {value}")
        self.get_choice()

    def get_choice(self):
        try:
            choice = int(
                input(
                    "Please choose an option by typing the associated number and then press <Enter>:\n"
                )
            )
            self.options.get(choice, self.show)()
        except ValueError:
            input("Choice should be a number.\nPress enter to continue.")
            self.show()


class SubMenu(Menu):
    SUBMENU = {
        1: "Use ROT47",
        2: "Use ROT13",
        3: "Go back",
    }

    def __init__(self, manager):
        super().__init__(manager)

    @property
    def options(self):
        option_list = {
            1: "ROT47",
            2: "ROT13",
            3: self.manager.show_menu,
        }

    def show(self):
        print("Submenu")

    def get_choice(self):
        pass
