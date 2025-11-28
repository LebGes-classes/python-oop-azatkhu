from Product import (
    Product,
)


class Menu:
    """"Класс, описывающий взаимодействие с пользователем."""

    def __init__(self, process = 1) -> None:
        """
        Конструктор класса.
        params:
            process: регулировка началы и конца работы программы. 
        """

        self.process = process

    def add_name(self, product_name: str, product_code: str, product_quantity: int, res: list) -> None:
        """Создание нового товара.
        
        Args:
            product_name: наименование товара. 
            product_code: шифр товара. 
            product_quantity: количество товара. 
            res: список, элементами которого являются экземлпяры класса Product. 
        """

        while (len(product_name) == 0 or len(product_code) == 0 or product_quantity == 0):
            print("Все поля должны быть заполнены")

            if len(product_name) == 0:
                product_name = input("Введите наименование товара: ")

            if len(product_code) == 0:
                product_code = input("Введите шифр товара: ")
            
            if product_quantity == 0:
                product_quantity = input("Введите количество товара: ")

        res += [Product(product_name, product_code, product_quantity)]
        
        print("Товар добавлен в список")

    def show_my_products(self, res: list) -> None:
        """Вывод всех созданных товаров. 
        Args: 
            res: список, элементами которого являются экземлпяры класса Product. 
        """
        
        for i in res:
            print(i.show_info())

        esc = input("Вы хотите выйти? ")

        if esc in ["да", "Да", "ДА", "Хочу", "хочу", "Выйти", "выйти"]:
            self.process = 0

    def change_options_of_product(self, res: list) -> None:
        """Выбор товара и последующее изменение его данных, вывод информации о товаре с изменёнными данными. 

        Args: 
            res: список, элементами которого являются экземлпяры класса Product. 
        """
       
        print("Выберите товар, данные которого вы хотите изменить")

        for i in res:
            print(i.get_name())

        change_info = input()
        for i in res:
            if i.get_name() == change_info:
                change_option = input(f'Выберите данные, которые хотите изменить для товара {change_info} ')

                match change_option:
                    case ("Наименование" | "наименование"):
                        changing_name = input("Введите новое название товара: ")

                        print(f"Название товара {change_option} изменено на {changing_name}")

                        i.set_name(changing_name)
                        
                        print(i.show_info())
                    case ("Шифр" | "шифр"):
                        changing_code = input("Введите новый шифр товара: ")

                        print(f"Шифр товара {change_option} изменен на {changing_code}")

                        i.set_code(changing_code)

                        print(i.show_info())
                    case ("Количество" | "количество"):
                        changing_quantity = int(input("Введите новое количество товара: "))

                        print(f"Количество товара {change_option} изменено на {changing_quantity}")

                        i.set_quantity(changing_quantity)

                        print(i.show_info())
                    case _:

                        print("Параметр не найден")
    
    def is_amount_enough(self, res: list) -> None:
        """Вывод информации о том, достаточное ли количество каждого из товаров.
        
        Args: 
            res: список, элементами которого являются экземлпяры класса Product.
        """
        
        minn = int(input("Для начала введите нужное количество товара (>0): "))
        for i in res:
            print(i.get_name(), end = " ")

            if i.a_lot_or_a_little(minn):
                print("- достаточно")
                
            else:
                print("- не достаточно")

    def is_name_long(self, res: list) -> None:
        """Вывод информации о том, длинное ли название имеет товар. 
        
        Args:
            res: список, элементами которого являются экземлпяры класса Product.
        """
        
        for i in res:

            print("Название товара", end = " ")
            print(i.get_name(), end = " ")

            if i.long_name():

                print("длинное")

            else:

                print("короткое")
    
    def start(self) -> None:
        """Запуск программы, вывод сообщения об отсутствии команды при её неправильном вводе. """

        res = []
        while self.process:
            text = input("1) Чтобы добавить товар, введите: Добавить новый товар \n2) Чтобы посмотреть все товары в списке, введите: Показать мои товары \n3) Для того, чтобы выйти, введите: Выйти \n4) Для изменения данных товара введите: Изменить данные \n5) Для того, чтобы узнать, достаточно ли какого-то товара введите: Узнать \n6) Чтобы узнать, длинное ли название товара, введите: Узнать длину \n")
            
            if text in ["добавить новый товар", "Добавить новый товар"]:
                product_name = input("Введите наименование товара: ")
                product_code = input("Введите шифр товара: ")
                product_quantity = int(input("Введите количество товара > 0: "))
                
                self.add_name(product_name, product_code, product_quantity, res)
                
            elif text in ["Показать мои товары", "показать мои товары"]:
                self.show_my_products(res)

            elif text in ["Выйти", "выйти"]:
                self.process = 0

            elif text in ["Изменить данные", "изменить данные", "изменить"]:
                self.change_options_of_product(res)
                    
            elif text in ["Узнать", "узнать"]: 
                self.is_amount_enough(res)

            elif text in ["Узнать длину", "узнать длину"]:
                self.is_name_long(res)

            elif len(text) > 0:

                print("Такой команды нет")
