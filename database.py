import pymysql
import os
timeout = 10
connection = pymysql.connect(
  charset="utf8mb4",
  connect_timeout=timeout,
  cursorclass=pymysql.cursors.DictCursor,
  db="defaultdb",
  host="firstsite-site1.a.aivencloud.com",
  password=os.environ['db_pass'],
  read_timeout=timeout,
  port=12336,
  user=os.environ['db_user'],
  write_timeout=timeout,
)
cursor = connection.cursor()

def load_animals_from_db():
  cursor.execute("SELECT * FROM animals")
  list_animals = cursor.fetchall()
  #print(list_animals[1])
  #connection.close()
  return list_animals

#cursor = connection.cursor()
#cursor.execute("SELECT * FROM animals")
#list_animals = cursor.fetchall()
#print(list_animals[1])
#connection.close()

