import re


class UrlExtractor:
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def validate_url(self):
        # not will “invert” the boolean value of the url variable. That is, if url is empty (“”) or zero (0), it will be converted to True and then the ValueError will be thrown.
        if not self.url:
            raise ValueError("URL is empty")

        pattern_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/exchange')
        match = pattern_url.match(self.url)
        if not match:
            raise ValueError('Invalid URL')

    def get_url_base(self):
        index_interrogation = self.url.find('?')
        url_base = self.url[0:index_interrogation]
        return url_base

    def get_url_parameters(self):
        index_interrogation = self.url.find('?')
        url_parameter = self.url[index_interrogation + 1:]
        return url_parameter

    def get_valor_parameters(self, parametro_busca):
        index_parameter = self.get_url_parameters().find(parametro_busca)
        index_value = index_parameter + len(parametro_busca) + 1
        ampersand_index = self.get_url_parameters().find('&', index_value)  # second parameter from position
        if ampersand_index == -1:
            value = self.get_url_parameters()[index_value:]
        else:
            value = self.get_url_parameters()[index_value:ampersand_index]
        return value

    def __len__(self):
        return len(self.url)

    # method called when you want to print an object
    def __str__(self):
        return self.url + "\n" + "Parameters: " + self.get_url_parameters() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url


url_extractor = UrlExtractor("https://bytebank.com/exchange?moedaOrigem=real&moedaDestino=dollar&quantity=500")
url_extractor2 = UrlExtractor("https://bytebank.com/exchange?moedaOrigem=real&moedaDestino=dollar&quantity=500")
print('URL length: ', len(url_extractor))
print("Full URL: ", url_extractor)

# Check that two instances with the same URL are equal
print("extrator_url == extrator_url_2? ", url_extractor == url_extractor2)

# Fetch the value of the quantity parameter
amount_value = url_extractor.get_valor_parameters("quantity")
print("Parameter value 'quantity': ", amount_value)
