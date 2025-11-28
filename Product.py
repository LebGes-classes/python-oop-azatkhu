class Product:
    """Класс описывающий товар."""

    def __init__(self, name = None, code = None, quantity = 1):
        """Инициализация\конструктор класса.

        Args:
            name: Наименование товара.
            code: Шифр товара.
            quantity: Количество товара.
        """

        self.__name = name
        self.__code = code
        self.__quantity = quantity
        
    def get_name(self) -> str:
        """Геттер наименования товара.
        
        Returns:
            __name: наименование товара.
        """

        return self.__name
    
    def set_name(self, name: str) -> None:
        """Сеттер наименования товара.
        
        Args:
            name: наименование товара.
        """

        self.__name = name
        
    def get_code(self) -> str:
        """Геттер шифра товара.

        Returns:
            __code: шифр товара
        """

        return self.__code
    
    def set_code(self, code: str) -> None:
        """Сеттер шифра товара.
        
        Args:
            code: шифр товара.
        """

        self.__code = code
        
    def get_quantity(self) -> int:
        """Геттер количества товара.
        
        Returns: 
            __quantity: количество товара
        """

        return self.__quantity
    
    def set_quantity(self, quantity: int) -> None:
        """Сеттер количества товара.

        Args:
            quantity: количество товара.
        """

        self.__quantity = quantity
        
    def show_info(self) -> str:
        """Вывод полной информации о товаре.

        Returns:
            str: наименование, шифр, количество.
        """

        return f'Наименование: {self.__name}, шифр: {self.__code}, количество: {self.__quantity}'
    
    def a_lot_or_a_little(self, specified_quantity: int) -> bool:
        """Просмотр инфорамции о том, достаточно ли количества товара.
        
        Returns:
            bool: True.
            Bool: False.
        """

        if self.__quantity >= specified_quantity:

            return True
        
        else:
            
            return False
        
    def long_name(self) -> bool:
        """Просмотр информации о том, длинное ли то или иное слово.
        
        Returns:
            bool: True.
        """

        if len(self.__name) > 10:

            return True 
