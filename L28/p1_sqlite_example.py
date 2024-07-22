import sqlite3

connection = sqlite3.connect('db/data.db', isolation_level=None)
print(connection)
cursor = connection.cursor()
for row in cursor:
    print(row)

# result = cursor.execute('select * from Vendors;')
# print(result is cursor)
# for row in cursor:
#     print(row)
# cursor.execute('select * from Vendors;')
# for row in cursor:
#     print(row)

# cursor.execute('select * from Vendors;')
# print(cursor.fetchall())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchone())
# print(cursor.fetchmany(size=2))
# print(cursor.fetchmany(size=2))
# print(cursor.fetchmany(size=2))
# print(cursor.fetchmany(size=2))

# deal = 2
# cursor.execute(f"select name, deal from Vendors where deal>{deal}")
# for row in cursor:
#     print(row)


# deal = 2
# cursor.execute("select name, deal from Vendors where deal>(?)", (deal,))
# for row in cursor:
#     print(row)

# deal = 2
# price = 300
# cursor.execute("select name, deal from Vendors where deal>? and price<?", (deal, price))
# for row in cursor:
#     print(row)

# deal = 2
# price = 300
# cursor.execute("select name, deal from Vendors where deal>:deal and price<:price", {'deal': deal, 'price': price})
# for row in cursor:
#     print(row)

# cursor.execute("INSERT INTO Vendors(name, item, deal, price) VALUES ('Oksana', 'Helicopter', 55, 111)")
# cursor.execute('select * from Vendors;')
# for row in cursor:
#     print(row)
# connection.commit()

# cursor.execute("INSERT INTO Vendors(name, item, deal, price) VALUES ('Bob', 'Car', 66, 222);")
# cursor.execute('select * from Vendors;')
# for row in cursor:
#     print(row)

# cursor.executemany("INSERT INTO Vendors(name, item, deal, price) VALUES (?, ?, ?, ?);",
#                    [('Bob2', 'Car', 66, 222), ('Bob3', 'Car', 66, 222)])
# cursor.execute('select * from Vendors;')
# for row in cursor:
#     print(row)

with open('test_script.sql', 'r') as sql_script:
    cursor.executescript(sql_script.read())


if connection:
    connection.close()
