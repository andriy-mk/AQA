import pytest
from modules.common.database import (
    Database,
)  # Імпортуємо клас Database, для роботи з базою даних


@pytest.mark.database
def test_database_connection():  # створюємо тест
    db = Database()  # створюємо екземпляр класу Database
    db.test_connection()  # виконуємо метод testconnection


@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()  # в змінну записуємо роботу методу get_all_users обєкта db
    print(users)


@pytest.mark.database
def test_check_user_sergii():  # тест для перевірки покупця з іменем Сергій
    db = Database()
    # отримуємо знайдені в результаті виконання методу get_user_address_by_name дані для покупця з Імене Сергій
    user = db.get_user_address_by_name('Sergii')
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    # ставимо нову кількість товару з унікальним номером
    db.update_product_qnt_by_id(1, 25)
    # читаємо кількість товару з унікальним номером 1
    water_qnt = db.select_product_qnt_by_id(1)
    # перевіряємо що нова кількість відповідає очікуваній
    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, "печиво", "солодке", 30)
    # після створення перевіряємо що дані зявилися в таблиці, перевірка кількості товару
    water_qnt = db.select_product_qnt_by_id(4)
    assert water_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(999)
    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print(f"Замовлення, {orders}")
    assert len(orders) == 1  # Check quantity of orders equal to 1
    # Check structure of data
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"
