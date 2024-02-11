from flask import Flask, request

app = Flask(__name__)

db = {}

@app.route("/fetch-data")
def get_valid_data():
    houses = [{'lat': 33.75069091548666, 'lng': -84.40901082117557},
              {'lat': 33.77069091548666, 'lng': -84.40901082117557},
              {'lat': 33.74069091548666, 'lng': -84.40901082117557},
              ]
    print(db)
    return houses

@app.route('/submit-property', methods=['POST'])
def submit_article():
    data = request.json
    min_price = data.get('min_price')
    max_price = data.get('max_price')
    min_year = data.get('min_year')
    bedrooms = data.get('bedrooms')
    bathrooms = data.get('bathrooms')
    sqft = data.get('squareFeet')
    distance = data.get('sliderValue')
    position = data.get('position')
    print(min_price, max_price, bedrooms, bathrooms, sqft, min_year, distance, position)
    db['min_price'] = min_price
    db['max_price'] = max_price
    db['min_year'] = min_year
    db['bedrooms'] = bedrooms
    db['bathrooms'] = bathrooms
    db['sqft'] = sqft
    db['distance'] = distance
    db['position'] = position
    # Process the submitted data (e.g., save it to the database)
    return 'Article submitted successfully!', 200

if __name__ == "__main__":
    app.run(debug=True)