import requests
from hashlib import sha1
import string


class Decipher(object):

    def get_json(self, url):
        r = requests.get(url)
        return r.text

    def save_json(self, text):
        with open('answer.json', 'w+') as json_file:
            json_file.write(text)

    def decrypt_julio(self, n_casas, text):
        alphabet = list(string.ascii_lowercase)
        text = text.lower()
        decrypted_text = list(text)
        for i in range(0, len(text)):
            #import pdb; pdb.set_trace()
            if text[i] != '.' and text[i] != ' ':
                letter_index = alphabet.index(text[i])
                if letter_index + n_casas < len(alphabet):
                    decrypted_text[i] = alphabet[alphabet.index(text[i]) + n_casas]
                else:
                    letter_index = (letter_index + n_casas) - len(alphabet)
                    decrypted_text[i] = alphabet[letter_index]
        return ''.join(decrypted_text)

    def get_sha1_hexdigest(self, text):
        value = sha1(text.encode())
        return value.hexdigest()
