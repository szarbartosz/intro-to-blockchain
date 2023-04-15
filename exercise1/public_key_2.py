from dataclasses import dataclass
from simple_cryptography import (
    PrivateKey,
    PublicKey,
    generate_key_pair,
    asymmetric_decrypt,
    asymmetric_encrypt,
)


class Alice:
    def __init__(self, bob: "Bob"):
        self.bob = bob

    def encrypt(self, message: str) -> bytes:
        """
        TODO: zaimplementuj szyfrowanie wiadomości
            Przydadzą ci się funkcje/metody
                - self.bob.get_public_key()
                - bytes(string, 'utf-8')
                - asymmetric_encrypt
        """
        return asymmetric_encrypt(self.bob.get_public_key(), bytes(message, 'utf-8'))

class Bob:
    def __init__(self):
        """
        TODO: wygeneruj parę klucz publiczny, prywatny za pomocą metody generate_key_pair z simple_cryptography.
        """
        self._public_key, self._private_key = generate_key_pair()

    def get_public_key(self):
        return self._public_key

    def decrypt(self, encrypted_message: bytes) -> str:
        """
        TODO: Zaimplementuj deszyfrowanie wiadomości.
            Przydadzą ci się funkcje/metody:
                - self._private_key
                - asymmetric_decrypt
                - string.decode("utf-8")
        """
        return asymmetric_decrypt(self._private_key, encrypted_message).decode("utf-8")
