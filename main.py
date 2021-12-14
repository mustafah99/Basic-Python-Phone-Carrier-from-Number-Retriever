import phonenumbers
from phonenumbers import carrier

while True:
    print('Enter your phone number with specified country code.')
    numberInput = input()
    x = phonenumbers.parse(numberInput, None)
    numberCarrier=carrier.name_for_number(x, "se")
    print(numberCarrier)
