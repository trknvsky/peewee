from peewee import *

db = SqliteDatabase('C:/Users/dLnnnnnn/Desktop/database.db')


class BaseModel(Model):
    class Meta:
        database = db

    def select_from_table(self, table):
        for row in table.select().dicts():
            print(row)

    def select_by_id(self, table, table_id):
        count_id = 0
        for row in table.select().dicts():
            count_id += 1
            if count_id == table_id:
                print(row)

    def delete_id(self, table, table_id):
        table.delete_by_id(table_id)


class Pizza(BaseModel):
    name = CharField(max_length=50)
    price = IntegerField()

    def insert_to_pizza(self, pizza_id, name, price):
        insert = Pizza.create(id='{}'.format(pizza_id), name='{}'.format(name), price='{}'.format(price))
        insert.save()


class Ingredients(BaseModel):
    name = CharField(max_length=50)

    def insert_to_ingredients(self, ingredient_id, name):
        insert = Ingredients.create(id='{}'.format(ingredient_id), name='{}'.format(name))
        insert.save()


class PizzaStructure(BaseModel):
    pizza = ForeignKeyField(Pizza, related_name='id')
    ingredient = ForeignKeyField(Ingredients, related_name='id')

    def insert_to_pizza_structure(self, pizza_id, ingredient_id):
        insert = PizzaStructure.create(pizza='{}'.format(pizza_id), ingredient='{}'.format(ingredient_id))
        insert.save()


class Staff(BaseModel):
    name = CharField(max_length=50)

    def insert_to_staff(self, table_id, name):
        insert = Staff.create(id='{}'.format(table_id), name='{}'.format(name))
        insert.save()


class Orders(BaseModel):
    pizza = ForeignKeyField(Pizza, related_name='id')
    date_order = DateField()
    table_number = IntegerField()
    staff_name = ForeignKeyField(Staff, related_name='id')
    sum_order = IntegerField()

    def insert_to_orders(self, pizza_id, date, table_number, staff_id, sum_order):
        insert = Orders.create(pizza='{}'.format(pizza_id),
                               date_order='{}'.format(date),
                               table_number='{}'.format(table_number),
                               staff_name='{}'.format(staff_id),
                               sum_order='{}'.format(sum_order)
                               )
        insert.save()


Pizza.create_table()
Ingredients.create_table()
PizzaStructure.create_table()
Staff.create_table()
Orders.create_table()
pizza = Pizza()
ingredients = Ingredients()
pizza_structure = PizzaStructure()
basemodel = BaseModel()
orders = Orders()
staff = Staff()
pizza.insert_to_pizza(1, 'Наполи', 140)
pizza.insert_to_pizza(2, 'Лигурия', 150)
pizza.insert_to_pizza(3, 'Fresh pizza', 155)
pizza.insert_to_pizza(4, 'Mushroom pizza', 145)
pizza.insert_to_pizza(5, 'Crazy pizza', 160)
ingredients.insert_to_ingredients(1, 'сыр')
ingredients.insert_to_ingredients(2, 'курица')
ingredients.insert_to_ingredients(3, 'Горгонзола')
ingredients.insert_to_ingredients(4, 'Грибы')
ingredients.insert_to_ingredients(5, 'Телятина')
pizza_structure.insert_to_pizza_structure(1, 1)
pizza_structure.insert_to_pizza_structure(2, 2)
pizza_structure.insert_to_pizza_structure(3, 3)
staff.insert_to_staff(1, 'Антон')
staff.insert_to_staff(2, 'Алла')
staff.insert_to_staff(3, 'Виталий')
staff.insert_to_staff(4, 'Андрей')
staff.insert_to_staff(5, 'Анастасия')
basemodel.select_from_table(pizza)
basemodel.select_by_id(ingredients, 2)
basemodel.delete_id(pizza, 3)











