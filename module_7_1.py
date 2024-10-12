import os.path

class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, 'w', encoding='utf-8') as f:
                pass

    def get_products(self):
        with open(self.__file_name, encoding='utf-8') as f:
            return f.read()

    def add(self, *products):
        with open(self.__file_name, 'a+', encoding='utf-8') as f:
            f.seek(0)
            file_data = f.read()

            for product in products:
                if product.name not in file_data:
                    f.write(f'{product.name}, {product.weight}, {product.category}\n')
                else:
                    print(f'Продукт {product.name}, {product.weight}, {product.category} уже есть в магазине')

if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())