import mysql.connector



conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000",
    database="laplateforme"
)


cursor = conn.cursor()

cursor.execute("SELECT superficie FROM etage ;")


superficies = cursor.fetchall()

superficieTotal = 0 
for supercie in superficies:

    superficieTotal = superficieTotal + supercie[0]
print('La superficie de LaPlateforme est de', superficieTotal, 'm2')

cursor.close()
conn.close()
