from abc import ABC, abstractmethod
from codecs import encode


class Cipher(ABC):
    @abstractmethod
    def do_cipher(self, text):
        raise NotImplementedError

    @abstractmethod
    def do_decipher(self, text):
        raise NotImplementedError


class Rot47Cipher(Cipher):
    def do_cipher(self, text: str) -> str:
        temp_array = []
        for i in range(len(text)):
            j = ord(text[i])
            if 33 <= j <= 126:
                temp_array.append(chr(33 + ((j + 14) % 94)))
            else:
                temp_array.append(text[i])
        return "".join(temp_array)

    def do_decipher(self, text):
        pass


class Rot13Cipher(Cipher):
    def do_cipher(self, text):
        return encode(text, "rot_13")

    def do_decipher(self, text):
        pass


class CipherFactory(ABC):
    @abstractmethod
    def cipher(self):
        raise NotImplementedError

    @abstractmethod
    def decipher(self):
        raise NotImplementedError


class Rot47CipherFactory(CipherFactory):
    def cipher(self):
        return Rot47Cipher()

    def decipher(self):
        pass


class Rot13CipherFactory(CipherFactory):
    def cipher(self):
        return Rot13Cipher()

    def decipher(self):
        pass
