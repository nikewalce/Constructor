#ceil - Округляем вверх, floor - Округляем вниз
from math import ceil, floor

class Constructor:
    #init - конструктор, self - ссылка на текущий объект, stock - запас
    def __init__(self, stock):
        #Остаток на складе
        self.stock = stock
        # Нужное количество деталей для 1 стула Евы
        self.parts_for_Eve = {'Hind_legs': 2, 'Front_legs': 2, 'Seat_diagonals': 2, 'Seat': 1, 'Upper_back': 1,
                          'Screws': 12, 'Glue': 0.4}

    # #del - деструктор
    # def __del__(self):
    #     print('del')

    #Проверка ключей словарей на соотвествие(если какой-то детали нет, тогда стул не собрать(детали присваивается 0))
    def Dict_matching_check(self):
        #Проходим по ключам нужных деталей для Евы
        for item in self.parts_for_Eve:
            #Если ключ есть в словаре остатка на складе, то словарь не трогам. Если ключа нет, добавляем его и приравниваем к 0
            self.stock.setdefault(item, 0)
        return self.stock

    def Dict_items(self):
        answer_dict = {}
        #Проходим по ключам нужных деталей для Евы
        for item in self.parts_for_Eve:
            #Узнаем сколько стульев можно сделать из остатка элементов
            a = self.stock[item] / self.parts_for_Eve[item]
            answer_dict[item] = a
            print(f'{item} = {a}')
        #Если есть одинаковые минимальные ключи, возвращаем все
        #min_value = min(answer_dict.values())
        #[k for k, v in answer_dict.items() if v == min_value]
        #Возвращаем минимальный ключ и его округленное значение вниз
        return min(answer_dict, key=answer_dict.get), floor(min(answer_dict.values()))

    #Остаток на складе
    def Remaining_Stock(self):
        print(f'Детали для 1 стула Ева: {self.parts_for_Eve}')
        print(f'Оставшиеся запасы на складе: {self.stock}')

        return 1

#словарь остатка на складе
rem_stock_list = {'Hind_legs': 5, 'Front_legs': 8, 'Seat_diagonals': 5, 'Seat': 3, 'Upper_back': 3, 'Screws': 100, 'Glue':2}
p = Constructor(rem_stock_list)
#Проверка на соответствие
p.Dict_matching_check()
print(p.Dict_items())
#print(p.Remaining_Stock())