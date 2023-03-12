import requests
def zapytaj():
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=json"
    response=requests.get(url)
    response
    return response.json()

print('Kalkulator Walut')
waluta=input('Podaj rodzaj Waluty: ')
dane=zapytaj()
data=dane['rates'] [0]['effectiveDate']
rodzaj=dane['currency']
kwota=dane['rates'][0]['mid']
print(data)
print(rodzaj)
print(float(kwota))
#edycjaa