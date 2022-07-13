from abc import ABC


class Cipher(ABC):
    def __init__(self):
        pass

    def do_cipher(self):
        pass

    def do_decipher(self):
        pass


class Rot47Cipher(Cipher):
    def __init__(self):
        pass

    def do_cipher(self):
        pass

    def do_decipher(self):
        pass


class Rot13(Cipher):
    def __init__(self):
        pass

    def do_cipher(self):
        pass

    def do_decipher(self):
        pass


class CipherFactory(ABC):
    def cipher(self):
        pass

    def decipher(self):
        pass


class CipherROT47Factory(CipherFactory):
    def cipher(self):
        pass

    def decipher(self):
        pass


class CipherROT13Factory(CipherFactory):
    def cipher(self):
        pass

    def decipher(self):
        pass
