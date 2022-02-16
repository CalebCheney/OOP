import InsectClass as i

def main():
    #wings = int(input("How many wings does the insect have?"))
    #legs = int(input("How many legs does the insect have?"))
    my_fly = i.Insect(2,4)
    moscetio = i.Insect(3, 6)
    my_fly.flight()
    print(my_fly.get_wings())
    print(my_fly.get_legs())
    print('Number of miles in flight:', my_fly.get_flight())

main()