# Country Brazil
address = "Av. João Naves de Ávila, 1331 - Tibery, Uberlândia - MG, 38408902"

# Regular Expression -- RegEx
import re

# zip code standart: 5 digits + hifen (opcional) + 3 digits

p = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
s = p.search(address) # will return Match
if s:
    zip_code = s.group() #return the default string
    print(zip_code)
