import sqlite3


class Database:
    def __init__(self):  # конструктор класу
        self.connection = sqlite3.connect(
            r"/Users/andriy/AQA" + r"/become_qa_auto.db"
        )  # сутність щоб взаємодіяти з базою даних (sqlite3 взаємодіє з базою даних)
        self.cursor = (
            self.connection.cursor()
        )  # сутність яка може виконувати наші команди в базі даних

    def test_connection(self):
        sqlite_select_query = "Select sqlite_version();"  # вивести версію бази даних
        # виконання запиту в базі даних
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()  # вивід результату
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        # в змінну, записуємо SQL запит
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)  # виконуємо запит в базу даних
        # змінній присвоюємо отриманий за допомогою методу fetchall обєкта cursor результат виконання запиту
        record = self.cursor.fetchall()
        return record  # повертаємо результат виконання

    # приймає імя користувача як параметр
    def get_user_address_by_name(self, name):
        # записуємо наш запит в базу даних
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)  # виконуємо запит в базу даних
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        # через те що qnt та product_id числове значення в лапки брати не требам значенням в таблиці products на значення вказаного в параметрі qnt
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        # підтвердження змін в базі даних, виконується для того щоб випадково не змінили дані, які не хотіли змінювати
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        # записуємо наш запит в базу даних
        query = f"SELECT quantity from products WHERE id = {product_id}"
        self.cursor.execute(query)
        # отримати результати роботи SQL запиту та записати їх у змінну
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = f"SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
