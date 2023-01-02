# Country Brazil
address = "Av. João Naves de Ávila, 1331 - Tibery, Uberlândia - MG, 38408902"

# Regular Expression -- RegEx
import re

# padrao do CEP: 5 digitos + hifen (opcional) + 3 digitos

p = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
s = p.search(address) # ira retornar o Match
if s:
    zip_code = s.group() # retorna a string padrao
    print(zip_code)