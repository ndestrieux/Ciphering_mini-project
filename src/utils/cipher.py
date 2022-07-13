from abc import ABC


class Cipher(ABC):
    def do_cipher(self):
        raise NotImplementedError

    def do_decipher(self):
        raise NotImplementedError


class Rot47Cipher(Cipher):
    def do_cipher(self):
        pass

    def do_decipher(self):
        pass


class Rot13Cipher(Cipher):
    def do_cipher(self):
        pass

    def do_decipher(self):
        pass


class CipherFactory(ABC):
    def __init__(self, manager):
        self.manager = manager

    def cipher(self):
        raise NotImplementedError

    def decipher(self):
        raise NotImplementedError


class Rot47CipherFactory(CipherFactory):
    def cipher(self):
        print("ROT47 cipher")

    def decipher(self):
        pass


class Rot13CipherFactory(CipherFactory):
    def cipher(self):
        print("ROT13 cipher")

    def decipher(self):
        pass
