import requests
def zapytaj():
    url = f"http://api.nbp.pl/api/exchangerates/rates/A/{waluta}/?format=json"
    response=requests.get(url)
    response
    return response.json()

print('Kalkulator Walut')
waluta=input('Podaj symbol Waluty: ')
dane=zapytaj()

data=dane['rates'][0]['effectiveDate']
rodzaj=dane['currency']
kwota=dane['rates'][0]['mid']
def wyswietl():
    print(data)
    print(rodzaj)
    print(float(kwota))
wyswietl()
oblicz=float(input('podaj kwotę jaką chcesz przeliczyć na zł: '))
wynik=oblicz*kwota
print(wynik,'zł')
#edycjaa
