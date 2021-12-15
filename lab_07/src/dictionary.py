FULL = 1
BIN = 2
SEG = 3
ALL = 4

class Dictionary(object):
    """
        Класс, задающий словарь.
    """

    TITLE = 0
    RATING = 1
    NO_RESULT = 0
    FIRST_SYMBOL = 0

    data = dict()


    def __init__(self, file):
        self.get_data(file)
    

    def get_data(self, file):
        """
            Получить данные из
            файла.
        """

        f = open(file, "r")
        first_read = False

        for record in f:
            if first_read:
                row = record.split(",")
                key = row[Dictionary.TITLE]
                value = row[Dictionary.RATING]

                self.data[key] = value
            
            first_read = True

    
    def print_pair(self, pair):
        """
            Вывод пары значений.
        """

        print(pair[Dictionary.TITLE], "--->", 
              pair[Dictionary.RATING])


    def print_data(self):
        """
            Вывод словаря.
        """

        if len(self.data) == 0:
            print("\nСловарь пуст.")
            return
        
        pairs = self.data.items()

        print("TITLE ---> RATING\n")

        for pair in pairs:
            self.print_pair(pair)
    

    def print_search_result(self, alg, compares, pair):
        """
            Вывод результата
            поиска.
        """

        print(alg)

        if compares:
            print("Результат поиска:")
            self.print_pair(pair)
            print("Число сравнений: ", compares)
        else:
            print("Фильм не найден.\n")


    def brute_force(self, need):
        """
            Полный перебор.
        """

        compares = 0
        value = None

        keys = self.data.keys()

        for key in keys:
            compares += 1

            if key == need:
                value = self.data[key]
                return compares, value
        
        return Dictionary.NO_RESULT, value

    
    def sort_keys(self, data):
        """
            Сортировка словаря
            по ключам.
        """

        keys = list(data.keys())
        keys.sort()

        sorted_data = dict()

        for key in keys:
            sorted_data[key] = data[key]
        
        return sorted_data

    
    def binary_search(self, need, sorted_data):
        """
            Бинарный поиск.
        """

        compares = 0
        value = None

        keys = list(sorted_data)
        left = 0
        right = len(keys) - 1

        while left <= right:
            compares += 1
            middle = (left + right) // 2
            now_key = keys[middle]

            if now_key < need:
                left = middle + 1
            elif now_key > need:
                right = middle - 1
            else:
                value = sorted_data[now_key]
                return compares, value
        
        return Dictionary.NO_RESULT, value

    
    def sort_values(self, data):
        """
            Сортировка словаря
            по убыванию значений.
        """

        sorted_data = dict()

        pairs = list(data.items())
        pairs.sort(key = lambda k: k[1], reverse = True)

        for pair in pairs:
            sorted_data[pair[Dictionary.TITLE]] = pair[Dictionary.RATING]

        return sorted_data


    def segment_data(self):
        """
            Сегментирование словаря.
        """

        segments = {symbol: 0 for symbol in "ABCDEFGHIJMS12345679"}

        for key in self.data:
            segments[key[Dictionary.FIRST_SYMBOL]] += 1

        segments = self.sort_values(segments)

        segmented_data = {pair: dict() for pair in segments}

        for key in self.data:
            segmented_data[key[Dictionary.TITLE]].update({key: self.data[key]})
        
        return segmented_data

    
    def segment_search(self, need, segmented_data):
        """
            Сегментный поиск.
        """

        compares = 0
        value = None

        symbols = list(segmented_data.keys())

        for symbol in symbols:
            compares += 1

            if symbol == need[Dictionary.FIRST_SYMBOL]:
                segment_compares = 0

                for key in segmented_data[symbol]:
                    segment_compares += 1

                    if key == need:
                        value = segmented_data[symbol][key]
                        return compares + segment_compares, value
                
                return Dictionary.NO_RESULT, value

        
        return Dictionary.NO_RESULT, value


    def search(self, search_type, output = True):
        """
            Поиск в словаре.
        """

        key = input("\nВведите название фильма: ")

        if search_type == FULL or search_type == ALL:
            compares, value = self.brute_force(key)

            if output:
                self.print_search_result("\nПолный перебор:", 
                                         compares, [key, value])
        
        if search_type == BIN or search_type == ALL:
            sorted_data = self.sort_keys(self.data)
            compares, value = self.binary_search(key, sorted_data)

            if output:
                self.print_search_result("\nБинарный поиск:", 
                                         compares, [key, value]) 


        if search_type == SEG or search_type == ALL:
            segmented_data = self.segment_data()
            compares, value = self.segment_search(key, segmented_data)

            if output:
                self.print_search_result("\nПоиск сегментами:", 
                                         compares, [key, value]) 

