class MenuItem:
    def __init__(self, name:str, price:float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate(self):
        total_price = self.price*self.quantity
        return total_price
            
class Rice(MenuItem): 
    def __init__(self, name, price, quantity, meat: bool, vegetables: bool, 
                 seafood: bool ):
        super().__init__(name, price, quantity)
        self.meat = meat
        self.vegetables = vegetables
        self.seafood = seafood
        if self.meat == True :
            self.price += 2
        if self.vegetables == True :
            self.price += 2
        if self.seafood == True :
            self.price += 3
class Soup(MenuItem):
    def __init__(self, name, price, quantity, meat: bool, changua:bool, 
                 seafood: bool):
        super().__init__(name, price, quantity)
        self.meat = meat
        self.seafood = seafood
        self.changua = changua
        if self.changua == True:
            self.price -= 1
        if self.meat == True :
            self.price += 2
        if self.seafood == True :
            self.price += 3
class Salad(MenuItem):
    def __init__(self, name, price, quantity, meat:bool, seafood:bool, 
                 fruit : bool):
        super().__init__(name,price,quantity)
        self.meat = meat
        self.seafood = seafood
        self.fruit = fruit
        if self.meat == True :
            self.price += 2
        if self.seafood == True :
            self.price += 3
        if self.fruit == True:
            self.price += 1   
class Dessert(MenuItem):
    def __init__(self, name, price, quantity, ice_cream: bool, special: bool, 
                 extra_candys: bool):
        super().__init__(name, price, quantity)
        self.ice_cream = ice_cream
        self.special = special
        self. extra_candys = extra_candys
        if self.ice_cream == True :
            self.price += 1
        if self.special == True :
            self.price += 2
        if self.extra_candys == True:
            self.price += 2
class Drink(MenuItem):
    def __init__(self, name, price, quantity, suggar: bool, milk :bool, 
                buffet: bool ):
        super().__init__(name, price, quantity)
        self.suggar = suggar
        self.milk = milk
        self.buffet = buffet
        if self.milk == True :
            self.price += 1
        if self.buffet == True:
            self.price += 3
class AlcoholicDrink(Drink):
    def __init__(self, name, price, quantity, suggar, milk, bottle : bool):
        super().__init__(name, price, quantity, suggar, milk, buffet = False)
        self.bottle = bottle
        if self.bottle == True:
            self.price = self.price*4
class Snacks(MenuItem): 
    def __init__(self, name, price, quantity, doritos: bool, chips: bool, 
                 spicy: bool):
        super().__init__(name, price, quantity)
        self.doritos = doritos
        self.chips = chips
        self.spicy = spicy
        if self.doritos == True :
            self.price += 2
        if self.spicy == True:
            self.price += 2
class Entrance(MenuItem): 
    def __init__(self, name, price, quantity, potatoes: bool, sausage : bool, 
                 sauce: bool):
        super().__init__(name, price, quantity)
        self.potatoes = potatoes
        self.sausage = sausage
        self.sauce = sauce
        if self.potatoes == True :
            self.price += 1
        if self.sausage == True :
            self.price += 2
        if self.sauce == True:
            self.price += 0.2
        
class FastFood(MenuItem): 
    def __init__(self, name, price, quantity, sauce: bool, premium:bool, 
                 extra: bool):
        super().__init__(name, price, quantity)
        self.sauce = sauce
        self.premium = premium
        self.extra = extra
        if self.extra == True :
            self.price += 2
        if self.premium == True :
            self.price += 3
        if self.sauce == True:
            self.price += 0.2
class ForeignFood(MenuItem):
    def __init__(self, name, price, quantity, japanese: bool, italian: bool,
                 arabic: bool):
        super().__init__(name, price, quantity)
        self.japanese = japanese
        self.italian = italian
        self.arabic = arabic
        if self.japanese == True :
            self.price += 3
        if self.italian == True :
            self.price += 2
        if self.arabic == True:
            self.price += 1.5
class Order: #a la cuenta de 3 lloro
    def __init__(self,order = []):
        self.order = order
    def additem(self,item:"MenuItem"):
        self.order.append(item)
    def calculate(self):
        amount = 0
        for i in range(0,len(self.order),1):
            amount += self.order[i].calculate()
        return amount
    def order_list(self):
        list = []
        for i in range(0,len(self.order),1):
            pre_list = []
            pre_list.append(self.order[i].name)
            pre_list.append(self.order[i].quantity)
            pre_list.append(self.order[i].price)
            pre_list.append(self.order[i].calculate())
            list.append(pre_list)
        return list
"""
arroz_con_pollo = Rice("pollito",15,2, True, True, False)
piña_colada = AlcoholicDrink("piñita",10,3, False, True, True)
arroz_con_pollo.calculate()
piña_colada.calculate()
picada = Entrance("picadita",5, 1, True, True, True)
orden = Order()
orden.additem(arroz_con_pollo)
orden.additem(picada)
print(orden.order[0].name)
print(picada.calculate())
print(arroz_con_pollo.calculate())
orden.calculate()
orden.order_list()
""" #parte de pruebas
if __name__ == "__main__":
    print("Buen día, bienvenido al restaurante XYZ")
    print("por favor elija que comida desea, tenemos:")
    print("Arroces(Rice), Sopas(Soup), Ensaladas(Salad), Postres(Dessert), Bebidas(Drink),")
    print("Bebidas Alcohólicas(AlcoholicDrink), Snacks, Entradas(Entrance), Comida Rápida(FastFood),")
    print("Comida Extranjera(ForeignFood)")
    tipo = input("ingrese")
    while tipo != '':
        tipo = input("ingrese el tipo(parentesís de las opciones)")
        nombre = str(input("ingrese el nombre del plato:"))
        cantidad = input("ingrese la cantidad de platos que se van a consumir:")
        precio = input("ingrese el precio individual de cada plato:")
        primera_adicion = bool("ingrese True o False si desea o no agregar la primera adición(costo extra):")
        segunda_adicion = bool("ingrese True o False si desea o no agregar la segunda adición(costo extra):")
        tercera_adicion = bool("ingrese True o False si desea o no agregar la tercera adición(costo extra):")
        match tipo:
            case "Rice":
                item = Rice(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
            case "Soup":
                item = Soup(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
            case "Salad":
                item = Salad(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
            case "Dessert":
                item = Dessert(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
            case "Drink":
                item = Drink(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
            case "AlcoholicDrink":
                item = AlcoholicDrink(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
            case "Snacks":
                item = Snacks(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
            case "Entrance":
                item = Entrance(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
            case "FastFood":
                item = FastFood(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
            case "ForeignFood":
                item = ForeignFood(nombre,precio,cantidad,primera_adicion,segunda_adicion,tercera_adicion)
        orden = Order()
        orden.additem(item)
        print("¿Desea agregar otro plato? (si/no)")
        respuesta = input()
        if respuesta == "si":
            continue
        else:
            print("Su orden es la siguiente:")
            for i in range(0,len(orden.order),1):
                print(orden.order[i].name)
            print("El total de su orden es: ",orden.calculate())
            break