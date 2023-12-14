import psycopg2

connect_string = "dbname=my_database user=my_user password=secret host=127.0.0.1"

stmt = """
SELECT * from orders 
join orders_item on orders_item.orders_id =orders.id 
join fooditem on fooditem.id=orders_item.fooditem_id where customer_id=1;
"""
stmt2 = 'SELECT COUNT(*) from fooditem;'
with psycopg2.connect(connect_string) as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(stmt)
        result = cursor.fetchall()
        for row in result:
            print (row)
    except psycopg2.Error as e:
        print(e)
