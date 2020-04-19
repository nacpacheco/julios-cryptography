from Decipher import Decipher
import json

URL_GET = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=6d6bcfdb678af8c8d90730b3c44ad79d086a68d7"
URL_POST = ""

dec = Decipher()
info = dec.get_json(URL_GET)
dec.save_json(info)

info_json = json.loads(info)
print(dec.decrypt_julio(info_json['numero_casas'], info_json['cifrado']))