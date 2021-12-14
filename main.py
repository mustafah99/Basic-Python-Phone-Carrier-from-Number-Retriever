import phonenumbers
from phonenumbers import carrier 
from phonenumbers import geocoder

while True:
    print("1. Find Phone Carrier by Number /  2. Find Country by Number")
    selectionNumberInput = input()
    if selectionNumberInput == "1":
        print('Enter your phone number with specified country code.')
        numberInput = input()
        x = phonenumbers.parse(numberInput, None)
        numberCarrier = carrier.name_for_number(x, "se")
        print(numberCarrier)
    elif selectionNumberInput == "2":
        print('Enter your phone number with specified country code.')
        numberInputForSecondOption = input()
        countryByNumber = phonenumbers.parse(numberInputForSecondOption, None)
        print("Now enter your country name in this format, for example 'se' for Sweden or 'us' for the United States.")
        countryInputForSecondOption = input()
        result = geocoder.description_for_number(countryByNumber, countryInputForSecondOption)
        print(result)


