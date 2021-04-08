import jaydebeapi
from classes.User import User

def intialize():
    _execute(
        (
         "CREATE TABLE IF NOT EXISTS geo ("
         "  id INT PRIMARY KEY NOT NULL,"
         "  lat INT NOT NULL,"
         "  lng INT NOT NULL);"

         "CREATE TABLE IF NOT EXISTS address ("
         "  id INT PRIMARY KEY NOT NULL,"
         "  city VARCHAR NOT NULL,"
         "  geo_id INT NOT NULL,"
         "  street VARCHAR NOT NULL,"
         "  suite VARCHAR NOT NULL,"
         "  zipcode VARCHAR NOT NULL);"

         " CREATE TABLE IF NOT EXISTS company ("
         "  id INT PRIMARY KEY NOT NULL,"
         "  bs VARCHAR NOT NULL,"
         "  catchPhrase VARCHAR NOT NULL,"
         "  name VARCHAR NOT NULL);"

         " CREATE TABLE IF NOT EXISTS user ("
         "  id INT PRIMARY KEY NOT NULL,"
         "  address_id INT NOT NULL,"
         "  company_id INT NOT NULL,"
         "  name VARCHAR NOT NULL,"
         "  phone VARCHAR NOT NULL,"
         "  username VARCHAR NOT NULL,"
         "  website VARCHAR NOT NULL)"
        )
    )

def _convert_to_schema(cursor):
    column_names = [record[0].lower() for record in cursor.description]
    column_and_values = [dict(zip(column_names, record)) for record in cursor.fetchall()]

    return User().load(column_and_values, many=True)

def _execute(query, returnResult=None):
    connection  = jaydebeapi.connect(
        "org.h2.Driver",
        "jdbc:h2:tcp://localhost:5234/vodafone",
        ["SA", ""],
        "../h2-1.4.200.jar")
    cursor = connection.cursor()
    cursor.execute(query)
    if returnResult:
        returnResult = _convert_to_schema(cursor)
    cursor.close()
    connection.close()

    return returnResult

def get_all():
    return _execute("SELECT * FROM user", returnResult=True)

def create(user):
    columns = ", ".join(user.keys())
    values = ", ".join("'{}'".format(value) for value in user.values())
    _execute("INSERT INTO user ({}) VALUES({})".format(columns, values))