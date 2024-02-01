import mysql.connector


conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='0000',
    database='laplateforme2'
)

cursor = conn.cursor()


# Utilisation de la méthode execute du curseur avec une jointure
query = """
    SELECT employe.id, employe.nom AS nom_employe, employe.prenom, employe.salaire, service.nom AS nom_service
    FROM employe
    LEFT JOIN service ON employe.id_service = service.id
"""

cursor.execute(query)

# Récupération de toutes les lignes de la méthode execute
results = cursor.fetchall()

# Imprimer chaque ligne directement



print(results)

# Fermeture du curseur
conn.close()

