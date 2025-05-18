# POO-UNAL-2025-1-RETO-3

1. se realiza el ejercicio de clase (esto me tocó hacerlo en la casa y me tomó más de lo planeado, *hay una parte hecha por copilot). En este ejercicio se crea una clase línea y luego un rectángulo empleando 4 líneas.
   
```python
#Class Exercise
class Line:
    def __init__(self, point_start:list, point_end:list):
        self.point_start = point_start
        self.point_end = point_end
    def compute_length(self):
        length = (float(self.point_end[0] - self.point_start[0])**2 +
                  float(self.point_end[1] - self.point_start[1])**2)**(1/2)
        return length
    def compute_slope(self):
        if (self.point_end[0] - self.point_start[0]) == 0:
            print("Esta línea es vertical, su pendiente está indefinida")
            return None
        else:
            slope = (float(self.point_end[1] - self.point_start[1])/
                  float(self.point_end[0] - self.point_start[0]))
            return slope
    def compute_horizontal_cross(self): #está complicado de entender
#pero este if verifica que los signos de los Y de los puntos sean contrarios o alguno sea 0
        primer_y = '-' in str(self.point_start[1])
        segundo_y = '-' in str(self.point_end[1])
        alguno = primer_y or segundo_y #(debe retornar True)
        ambos = primer_y and segundo_y #(debe retornar False)
        if ((alguno == True and ambos == False)
            or(self.point_start[1] == 0 or self.point_end[1] == 0)) :
            return True
        else:
            return False
    def compute_vertical_cross(self): #se aplica la misma lógica que el anterior con los X de los puntos
        primer_y = '-' in str(self.point_start[0])
        segundo_y = '-' in str(self.point_end[0])
        alguno = primer_y or segundo_y #(debe retornar True)
        ambos = primer_y and segundo_y #(debe retornar False)
        if ((alguno == True and ambos == False)
            or(self.point_start[0] == 0 or self.point_end[0] == 0)) :
            return True
        else:
            return False
class Rectangle:
    def __init__(self,linea_1: "Line", linea_2: "Line",linea_3: "Line", linea_4: "Line"):
        self.linea_horizontal = linea_1 #inferior
        self.linea_vertical = linea_2 #izquierda
        self.linea_horizontal_2 = linea_3 #superior
        self.linea_vertical_2 = linea_4 #derecha
        #se validan las líneas de entrada
        horizontales = ((self.linea_horizontal != self.linea_horizontal_2) 
            and ( self.linea_horizontal.compute_slope() == 0 and 
                 self.linea_horizontal_2.compute_slope() == 0))
        verticales = ((self.linea_vertical != self.linea_vertical_2) 
            and (self.linea_vertical.compute_slope() == None and 
                 self.linea_vertical_2.compute_slope() == None))
        if not (horizontales and verticales ):
            print("ingrese lineas válidas")
        else: #aquí se verifica que compartan vertices
            #*la solución que está a continuación es muy estricta así que solo sirve para algunos rectángulos
            """
            lado_izquierdo = (self.linea_horizontal.point_start[0] == 
                              self.linea_vertical.point_start[0] == 
                              self.linea_horizontal_2.point_start[0])
            lado_derecho = (self.linea_horizontal.point_end[0] == 
                            self.linea_vertical_2.point_start[0] == 
                            self.linea_horizontal_2.point_end[0])
            lado_superior = (self.linea_horizontal.point_start[1] == 
                             self.linea_vertical_2.point_start[1] == 
                             self.linea_horizontal_2.point_start[1])
            lado_inferior = (self.linea_horizontal.point_end[1] == 
                             self.linea_vertical.point_start[1] == 
                             self.linea_horizontal_2.point_end[1])
            self.validador = (lado_izquierdo and lado_derecho) and (lado_superior and lado_inferior)
            """
            #* la solución a continuación es más universal aunque sinceramente me la dió copilot
            puntos = [
                tuple(self.linea_horizontal.point_start), tuple(self.linea_horizontal.point_end),
                tuple(self.linea_vertical.point_start), tuple(self.linea_vertical.point_end),
                tuple(self.linea_horizontal_2.point_start), tuple(self.linea_horizontal_2.point_end),
                tuple(self.linea_vertical_2.point_start), tuple(self.linea_vertical_2.point_end)
                    ]
            self.validador = len(set(puntos)) == 4 and horizontales and verticales #el set(puntos) quita los duplicados
    def compute_area(self):
        if self.validador == True:
            area = self.linea_horizontal.compute_length()*self.linea_vertical.compute_length()
            return area
        else: return "ingrese líneas válidas"
    def compute_perimeter(self):
        if self.validador == True:
            perimeter = (self.linea_horizontal.compute_length()*2 
                            + self.linea_vertical.compute_length()*2)
            return perimeter
        else: return "ingrese líneas válidas"
point_1 = [-10,10]
point_2 = [-20,0]
linea = Line(point_1,point_2)
linea.compute_length()
linea.compute_slope()
linea.compute_horizontal_cross()
linea.compute_vertical_cross()

p1 = [0, 0]    # esquina inferior izquierda
p2 = [4, 0]    # esquina inferior derecha
p3 = [0, 3]    # esquina superior izquierda
p4 = [4, 3]    # esquina superior derecha

linea_inferior = Line(p1, p2)    
linea_izquierda = Line(p1, p3)   
linea_superior = Line(p3, p4)   
linea_derecha = Line(p2, p4) 

rectangulo = Rectangle(linea_inferior, linea_izquierda, linea_superior, linea_derecha)

rectangulo.compute_area()
```
2. se realiza el programa del menú. En este los MenuItem tienen la peculiaridad de que cambian de precio si tienen adiciones a continuación su diagrama de clases:
   ```Mermaid
   classDiagram
    class MenuItem {
        -name: str
        -price: float
        -quantity: int
        +calculate()
    }
    class Rice {
        -meat: bool
        -vegetables: bool
        -seafood: bool
    }
    class Soup {
        -meat: bool
        -changua: bool
        -seafood: bool
    }
    class Salad {
        -meat: bool
        -seafood: bool
        -fruit: bool
    }
    class Dessert {
        -ice_cream: bool
        -special: bool
        -extra_candys: bool
    }
    class Drink {
        -suggar: bool
        -milk: bool
        -buffet: bool
    }
    class AlcoholicDrink {
        -bottle: bool
    }
    class Snacks {
        -doritos: bool
        -chips: bool
        -spicy: bool
    }
    class Entrance {
        -potatoes: bool
        -sausage: bool
        -sauce: bool
    }
    class FastFood {
        -sauce: bool
        -premium: bool
        -extra: bool
    }
    class ForeignFood {
        -japanese: bool
        -italian: bool
        -arabic: bool
    }
    class Order {
        -order: list
        +additem(item)
        +calculate()
        +order_list()
    }

    Rice --|> MenuItem
    Soup --|> MenuItem
    Salad --|> MenuItem
    Dessert --|> MenuItem
    Drink --|> MenuItem
    AlcoholicDrink --|> Drink
    Snacks --|> MenuItem
    Entrance --|> MenuItem
    FastFood --|> MenuItem
    ForeignFood --|> MenuItem
    ```

y a continuación se coloca el código del programa:

```python
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
```