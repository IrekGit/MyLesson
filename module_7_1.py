class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r', encoding='utf-8')
            products = file.read()
            file.close()
            return products
        except FileNotFoundError:
            return ""

    def add(self, *products):
        existing_products = set()
        current_products = self.get_products().strip().split('\n')

        for line in current_products:
            if line:  # Проверяем, что строка не пустая
                name = line.split(', ')[0]
                existing_products.add(name)
        file = open(self.__file_name, 'a', encoding='utf-8')
        for product in products:
            if product.name in existing_products:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                file.write(str(product) + '\n')
                print(f"Продукт {product.name} добавлен в магазин")
                existing_products.add(product.name)

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(f"Привезли новую партию товаров в магазин:\n"
      f"Имя: {p1.name}, вес: {p1.weight}, категория {p1.category}\n"
      f"Имя: {p2.name}, вес: {p2.weight}, категория {p2.category}\n"
      f"Имя: {p3.name}, вес: {p3.weight}, категория {p3.category}") # __str__

s1.add(p1, p2, p3)
print(s1.get_products())