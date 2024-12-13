# app.py
from flask import Flask, render_template, jsonify # type: ignore
import sqlite3

app = Flask(__name__)

# Function to fetch property listings from the database
def get_properties():
    conn = sqlite3.connect('property_listings.db')
    c = conn.cursor()
    
    # Query to fetch all properties
    c.execute("SELECT * FROM properties")
    properties = c.fetchall()
    
    conn.close()
    return properties

# Route to serve the property listings page
@app.route('/')
def property_listing_page():
    properties = get_properties()
    return render_template('index.html', properties=properties)

# API route to fetch properties in JSON format (for potential use by JavaScript)
@app.route('/api/properties')
def api_properties():
    properties = get_properties()
    return jsonify(properties)

if __name__ == "__main__":
    app.run(debug=True)
