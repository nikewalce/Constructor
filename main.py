class Constructor:
    #init - конструктор, self - ссылка на текущий объект, stock - запас
    def __init__(self, stock):
        self.stock = stock

    # #del - деструктор
    # def __del__(self):
    #     print('del')

    def Remaining_Stock(self):
        print(f'Оставшиеся запасы на складе: {self.stock}')
        return 1

rem_stock_list = {'Hind_legs': 5, 'Front_legs': 8, 'Seat_diagonals': 5, 'Seat': 3, 'Upper_back': 3, 'Screws': 100, 'Glue':2}
p = Constructor(rem_stock_list)
#print(p.stock['Glue'], type(p.stock))
print(p.Remaining_Stock())