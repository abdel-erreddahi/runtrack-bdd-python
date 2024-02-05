import mysql.connector
conn = mysql.connector.connect(
 
    host='localhost',
    user='root',
    password='0000',
    database='store'
)

cursor = conn.cursor()


# Utilisation de la méthode execute du curseur avec une jointure
query = """
    SELECT product.id, product.name AS name_product, product.desription, product.price, product.quantitiy, category.name AS name_category
    FROM product
    LEFT JOIN category ON product.id_category = category.id
"""

cursor.execute(query)
# Récupération de toutes les lignes de la méthode execute
results = cursor.fetchall()
# Imprimer chaque ligne directement
print(results)
# Fermeture du curseur


# les variables
choix_1 ='ajouter un produit'
choix_2 = 'supprimer un produit'
choix_3 = 'modifier le produit (stock, price)'
def choix():
    print('1 :',choix_1)
    print('2 :',choix_2)
    print('3 :',choix_3)

def ajouter_produit():
    produit_ajouter = input('Insert the product information (description, price, quantity, category ID) separated by commas: ')
    
    # Split the input string into individual values
    product_info = produit_ajouter.split(', ')
    
    # Assuming 'product' is the name of your table and 'name', 'desription', 'price', 'quantitiy', 'id_category' are columns
    query = "INSERT INTO product (name, desription, price, quantitiy, id_category) VALUES (%s, %s, %s, %s, %s)"
    values = (product_info[0], product_info[1], float(product_info[2]), int(product_info[3]), int(product_info[4]))
    
    try:
        cursor.execute(query, values)
        conn.commit()
        print("Product added successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def supprimer_produit():
    produit_supprimer = input('which product would you delete :')
    
    query = "DELETE FROM product WHERE name = %s"
    values = (produit_supprimer,)

    try:
        cursor.execute(query, values)
        conn.commit()
        print(f"Product '{produit_supprimer}' deleted successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    

def modifier_produit():
    produit_modifier = input('what would you like to change')
    new_stock = input('Enter the new stock quantity: ')
    new_price = input('Enter the new price: ')

    query = "UPDATE product SET quantity = %s, price = %s WHERE name = %s"
    values = (new_stock, new_price, produit_modifier)

    try:
        cursor.execute(query, values)
        conn.commit()
        print(f"Product '{produit_modifier}' modified successfully.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    

def fonction(choice):
    
    if choice == 1 :
        return ajouter_produit()
    if choice == 2 :
        return supprimer_produit()
    if choice == 3 :
        return modifier_produit() 

choix()

user_choice = int(input('Choose what you want to do (1-3): '))
fonction(user_choice)
conn.close()

