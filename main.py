url = "bytebank.com/exchange?currencyDestination=dollar&quantity=500&currencyOrigin=real"


# URL sanitization
url = url.strip()

# URL Validation
if url == "":
    raise ValueError("URL is empty")

# Separate base and parameters
index_interrogation = url.find('?')
url_base = url[0:index_interrogation]
url_parameter = url[index_interrogation+1:]
print(url_parameter)

# Fetch the value of a parameter
parameter_search = 'quantity'
index_parameter = url_parameter.find(parameter_search)
index_value = index_parameter + len(parameter_search) + 1
ampersand_index = url_parameter.find('&', index_value) # segundo parametro a partir da posicao
if ampersand_index == -1:
    valor = url_parameter[index_value:]
else:
    valor = url_parameter[index_value:ampersand_index]
print(valor)