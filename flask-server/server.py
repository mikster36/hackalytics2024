from flask import Flask, request

app = Flask(__name__)

# members api route
@app.route("/fetch-data")
def members():
    return {"members": ["1", "2", "3"]}

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
    # Process the submitted data (e.g., save it to the database)
    return 'Article submitted successfully!', 200

if __name__ == "__main__":
    app.run(debug=True)