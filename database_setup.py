import sqlite3
import random

def create_db():
    conn = sqlite3.connect('property_listings.db')
    c = conn.cursor()
    
    # Create the property listings table
    c.execute('''CREATE TABLE IF NOT EXISTS properties (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    type TEXT,
                    price INTEGER,
                    location TEXT,
                    bedrooms INTEGER,
                    bathrooms INTEGER,
                    description TEXT,
                    status TEXT)''')

    # List of possible property types, locations, and statuses
    property_types = ['Apartment', 'House', 'Condo', 'Townhouse']
    locations = ['New York', 'Los Angeles', 'San Francisco', 'Miami', 'Chicago', 'Austin', 'Houston', 'Seattle', 'Dallas', 'Denver']
    statuses = ['For Sale', 'For Rent']
    
    # Generate 100 records
    for i in range(100):
        type_ = random.choice(property_types)
        location = random.choice(locations)
        price = random.randint(100000, 1000000)  # Random price between 100,000 and 1,000,000
        bedrooms = random.randint(1, 5)  # Random bedrooms between 1 and 5
        bathrooms = random.randint(1, 4)  # Random bathrooms between 1 and 4
        description = f"Description for {type_} in {location}"
        status = random.choice(statuses)
        
        # Insert the data into the database
        c.execute("INSERT INTO properties (type, price, location, bedrooms, bathrooms, description, status) VALUES (?, ?, ?, ?, ?, ?, ?)",
                  (type_, price, location, bedrooms, bathrooms, description, status))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_db()
