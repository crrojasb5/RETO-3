#CARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTER

class MenuItem:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
    def calculate_total_price(self):
        return self.price

class Beverage(MenuItem):
    def __init__(self, name: str, price: int, volume_ml: int):
        super().__init__(name, price)
        self.volume_ml = volume_ml

class MainCourse(MenuItem):
    def __init__(self, name: str, price: int, protein: str, side_dish: str):
        super().__init__(name, price)
        self.protein = protein
        self.side_dish = side_dish


class Dessert(MenuItem):
    def __init__(self, name: str, price: int, texture: str):
        super().__init__(name, price)
        self.texture = texture
 
class Order:
    def __init__(self):
        self.item = []
    
    def add_item(self, item: MenuItem):
        self.item.append(item)
    
    def calculate_total(self):
        total = 0
        for item in self.item:
            total += item.calculate_total_price()
        return total
    
    def apply_discount(self):
        total = self.calculate_total()
        if total > 40000:
            discount = 15
        else:
            discount = 10
        discount_applied = total * (discount / 100)
        return total - discount_applied
    
#CARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTERESCARACTER

menu = [
    Beverage("Coca-Cola", 5000, 350), #0
    Beverage("Jugo Naranja", 8000, 700), #1
    Beverage("Agua", 4000, 400), #2
    MainCourse("Carne en Bistec", 15000, "Res", "Arroz"), #3
    MainCourse("Pollo Frito en BBQ", 17000, "Pollo", "Papas Fritas"), #4
    MainCourse("Salmon al Horno", 25000, "Pescado", "Pasta al Gusto"), #5
    MainCourse("Costillas BBQ", 18000, "Cerdo", "Papas Fritas"), #6
    Dessert("Cheesecake", 8000, "Cremoso"), #7
    Dessert("Galleta Chips", 5000, "Crujiente"), #8
    Dessert("Granizado", 7500, "Refrescante") #9
]

orden = Order()

orden.add_item(menu[0])
orden.add_item(menu[5])
orden.add_item(menu[6])
orden.add_item(menu[9])

print("Cuenta Total:", orden.calculate_total())
print("Total con descuento:", orden.apply_discount())
