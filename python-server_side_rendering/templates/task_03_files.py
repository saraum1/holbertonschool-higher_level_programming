import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

def read_csv(file_path):
    products = []
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")
    
    if source == 'json':
        data = read_json('products.json')
    else:
        data = read_csv('products.csv')
    
    if product_id:
        data = [p for p in data if p['id'] == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found")
            
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
