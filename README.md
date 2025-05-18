# POO-UNAL-2025-1-RETO-3

1. se realiza el ejercicio de clase (no lo he hecho aún, espero tenerlo en una hora)
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
y a continuación se coloca el programa:
