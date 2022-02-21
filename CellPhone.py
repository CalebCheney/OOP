import CellPhoneClass as c

def main():
    
    man = "Google"
    model = "Pixel"
    price = 900
    

    my_phone = c.CellPhone(man, model, price)

    print()
    print('My manufaturer is:', my_phone.get_manufact())
    print('My model is:', my_phone.get_model())
    print('My price is: ', '$', my_phone.get_retail_price(), sep='')

    man = input('Enter manufacturer: ')
    model = input('Enter model: ')
    price = int(input('Enter price: '))

    my_phone = c.CellPhone(man, model, price)

    print()
    print('New manufaturer is:', my_phone.get_manufact())
    print('New model is:', my_phone.get_model())
    print('New price is: ', '$', my_phone.get_retail_price(), sep='')

main()