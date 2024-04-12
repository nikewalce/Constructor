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
        # Нужное количество деталей для 1 стула Эми
        self.parts_for_Emm = {'Hind_legs': 2, 'Front_legs': 2, 'Seat_diagonals': 2, 'Seat_textile': 1, 'Upper_back_textile': 1,
                              'Screws': 12, 'Glue': 0.4}
        # Нужное количество деталей для 1 стула Фиби
        self.parts_for_Fibi = {'Hind_legs': 2, 'Front_legs': 2, 'Horizontals_legs': 2, 'Seat_textile': 1,
                              'Screws': 12, 'Glue': 0.4}
        #Все детали(** распаковка словарей и их слияние, чего нет - добавляется)
        self.all_parts = {**self.parts_for_Eve, **self.parts_for_Emm, **self.parts_for_Fibi}

        # #del - деструктор
    # def __del__(self):
    #     print('del')

    #Проверка ключей словарей на соотвествие(если какой-то детали нет, тогда стул не собрать(детали присваивается 0))
    def Dict_matching_check(self):
        #Проходим по ключам нужных деталей для Евы
        for item in self.all_parts:
            #Если ключ есть в словаре остатка на складе, то словарь не трогам. Если ключа нет, добавляем его и приравниваем к 0
            self.stock.setdefault(item, 0)
        return self.stock


    #Метод для нахождения максимального кол-ва стульев из остатка деталей для Евы
    def Dict_items_Eve(self):
        answer_dict = {}
        #Проходим по ключам нужных деталей для Евы
        for item in self.parts_for_Eve:
            #Рассчитываем сколько есть деталей для 2 стула из остатка
            min_amount = floor(self.stock[item] / self.parts_for_Eve[item])
            answer_dict[item] = min_amount
            print(f'{item} = {min_amount}')
        #Кол-во стульев, которое можно сделать
        min_value = min(answer_dict.values())
        #Возвращаем минимальный ключ и его округленное значение вниз. Если есть одинаковые минимальные ключи, возвращаем все
        #return min(answer_dict, key=answer_dict.get), floor(min(answer_dict.values())) #для одного ключа
        return ([k for k, v in answer_dict.items() if v == min_value], min_value) #для нескольких ключей

    # Метод для нахождения максимального кол-ва стульев из остатка деталей для Эми
    def Dict_items_Emm(self):
        answer_dict = {}
        # Проходим по ключам нужных деталей для Эми
        for item in self.parts_for_Emm:
            # Рассчитываем сколько есть деталей для 2 стула из остатка
            min_amount = floor(self.stock[item] / self.parts_for_Emm[item])
            answer_dict[item] = min_amount
            print(f'{item} = {min_amount}')
        # Кол-во стульев, которое можно сделать
        min_value = min(answer_dict.values())
        # Возвращаем минимальный ключ и его округленное значение вниз. Если есть одинаковые минимальные ключи, возвращаем все
        # return min(answer_dict, key=answer_dict.get), floor(min(answer_dict.values())) #для одного ключа
        return ([k for k, v in answer_dict.items() if v == min_value], min_value)  # для нескольких ключей

    # Метод для нахождения максимального кол-ва стульев из остатка деталей для Эми
    def Dict_items_Fibi(self):
        answer_dict = {}
        # Проходим по ключам нужных деталей для Фиби
        for item in self.parts_for_Fibi:
            # Рассчитываем сколько есть деталей для 2 стула из остатка
            min_amount = floor(self.stock[item] / self.parts_for_Fibi[item])
            answer_dict[item] = min_amount
            print(f'{item} = {min_amount}')
        # Кол-во стульев, которое можно сделать
        min_value = min(answer_dict.values())
        # Возвращаем минимальный ключ и его округленное значение вниз. Если есть одинаковые минимальные ключи, возвращаем все
        # return min(answer_dict, key=answer_dict.get), floor(min(answer_dict.values())) #для одного ключа
        return ([k for k, v in answer_dict.items() if v == min_value], min_value)  # для нескольких ключей

    #Остаток на складе
    def Remaining_Stock(self):
        print(f'Детали для 1 стула Ева: {self.parts_for_Eve}')
        print(f'Оставшиеся запасы на складе: {self.stock}')

        return 1

#словарь остатка на складе
rem_stock_list = {'Hind_legs': 90, 'Front_legs': 56, 'Seat_diagonals': 70, 'Seat': 90, 'Upper_back': 78, 'Screws': 1000, 'Glue':40, 'Seat_textile': 45, 'Upper_back_textile': 70}
p = Constructor(rem_stock_list)
#Проверка на соответствие
p.Dict_matching_check()
print(f'Ева: {p.Dict_items_Eve()}, Эми: {p.Dict_items_Emm()}, Фиби: {p.Dict_items_Fibi()}')
#print(p.Remaining_Stock())