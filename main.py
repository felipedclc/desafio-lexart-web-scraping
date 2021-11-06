from flask_cors import CORS
from flask import Flask, jsonify
from scrap.fetch import get_url_products_buscape, fetch, scrape_buscape


app = Flask(__name__)
CORS(app)


@app.route("/")
def hello():
    return "Hello World"


@app.route("/<string:product>")
def index(product):
    url = get_url_products_buscape(product)
    html_content = fetch(url)
    return jsonify(scrape_buscape(html_content))  # apenas a pagina 1


if __name__ == "__main__":
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)
