import psycopg2

try:
    connection = psycopg2.connect(
       user = "jfrn_kallil",
       password = "k@lLil2020",
       host = "buenosaires.jfrn.jus.br"
    )

    cursor = connection.cursor()
    print(connection.get_dsn_parameters(),"\n")

    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected into the - {}".format(record))

except(Exception, psycopg2.Error) as error:
    print("Error connecting to PostgreSQL database", error)
    connection = None

#Close the database connection
finally:
    if(connection != None):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is now closed")
