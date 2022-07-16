from abc import ABC, abstractmethod
from codecs import encode
from typing import ClassVar


class Cipher(ABC):
    @abstractmethod
    def do_action(self, text):
        raise NotImplementedError


class Rot47Cipher(Cipher):
    def do_action(self, text: str) -> str:
        temp_array = []
        for i in range(len(text)):
            j = ord(text[i])
            if 33 <= j <= 126:
                temp_array.append(chr(33 + ((j + 14) % 94)))
            else:
                temp_array.append(text[i])
        return "".join(temp_array)


class Rot13Cipher(Cipher):
    def do_action(self, text: str) -> str:
        return encode(text, "rot_13")


class CipherFactory(ABC):
    @abstractmethod
    def cipher(self):
        raise NotImplementedError

    @abstractmethod
    def decipher(self):
        raise NotImplementedError


class Rot47CipherFactory(CipherFactory):
    def cipher(self) -> ClassVar:
        return Rot47Cipher()

    def decipher(self):
        return Rot47Cipher()


class Rot13CipherFactory(CipherFactory):
    def cipher(self):
        return Rot13Cipher()

    def decipher(self):
        return Rot13Cipher()
