import sqlite3

def create_database():
    # Connexion à la base de données SQLite
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    
    # Création de la table Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Insertion de données d'exemple
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')
    
    # Sauvegarder et fermer
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()