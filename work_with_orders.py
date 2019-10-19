from models import *
from datetime import date


basemodel.select_from_table(pizza)
pizza_id = input('Выберите пиццу: ')
date_order = date.today()
print('Дата: {}'.format(date_order))
table_number = int(input('Введите номер столика: '))
basemodel.select_from_table(staff)
staff_id = int(input('Выберите официанта: '))
sum_order = int(input('Введите сумму заказа: '))
orders.insert_to_orders(pizza_id, date_order, table_number, staff_id, sum_order)

