from Decipher import Decipher
import json

URL_GET = ""
URL_POST = ""

dec = Decipher()
info = dec.get_json(URL_GET)
dec.save_json(info)

info_json = json.loads(info)

info_json["decifrado"] = dec.decrypt_julio(info_json["numero_casas"], info_json["cifrado"])
info_json["resumo_criptografico"] = dec.get_sha1_hexdigest(info_json["decifrado"])

dec.save_json(json.dumps(info_json))

print(dec.post_json(URL_POST,'answer.json'))