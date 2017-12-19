import osa


def convert_temp_2_celsius(temp_fahrenheit):
    client = osa.Client("http://www.webservicex.net/ConvertTemperature.asmx?WSDL")
    return client.service.ConvertTemp(temp_fahrenheit, 'degreeFahrenheit', 'degreeCelsius')


with open('temps.txt', 'r') as f:
    data = f.read()
    data_list = data.split('\n')
    temp_list = [int(i.replace(' F', '')) for i in data_list]

average_temp_f = sum(temp_list) / len(temp_list)
print(f"Средняя температура {convert_temp_2_celsius(average_temp_f)} C")


def cross_rate(base_currency, to_currency):
    client = osa.Client("http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL")
    return client.service.RateNum(baseCurrency=base_currency.upper(), toCurrency=to_currency.upper(), rounding='false')


with open('currencies.txt', 'r') as f:
    data = f.read()
    data_list = data.split('\n')
    travel_list = [i.split(' ') for i in data_list]

sum = 0
for travel in travel_list:
    sum += int(travel[1]) * cross_rate(travel[2], 'rub')

print(f"Стоимость путешествия {int(sum)} в рублях ")


def convert_mile_2_km(mile):
    client = osa.Client("http://www.webservicex.net/length.asmx?WSDL")
    return client.service.ChangeLengthUnit(mile, 'Miles', 'Kilometers')


with open('travel.txt', 'r') as f:
    data = f.read()
    data_list = data.split('\n')
    travel_list = [i.split(' ') for i in data_list]
    miles = float(0)
    for i in travel_list:
        miles += float(i[1].replace(',', ''))

print('Длина пути  {} в  километрах'.format('%.2f' % convert_mile_2_km(miles)))
