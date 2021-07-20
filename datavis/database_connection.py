import mysql.connector as connection
from mysql.connector import Error
import pandas as pd


try:
    conn = connection.connect(host='204.11.59.250',
                                         database='austinst_gasmonitor',
                                         user='austinst_root',
                                         password='0797277217Sk')
    if conn.is_connected():
        db_Info = conn.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

def datafr():
query = "SELECT username, residence, gasValue, leakagecase FROM gaslevel";
df = pd.read_sql(query, conn)
print(df)
# finally:
#     if connection.is_connected():
#         mycursor.close()
#         connection.close()
#         print("MySQL connection is closed")

