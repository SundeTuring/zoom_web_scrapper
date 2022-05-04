from scrapper import Scrapper
from flask import Flask

app = Flask(__name__)


@app.route("/product/<product_name>")
def home(product_name):
    url = f"https://www.zoom.com.br/search?q={product_name}&page=1&sortBy=default&isDealsPage=false"
    scrapper = Scrapper(url)

    product_info = scrapper.get_product_info()
    return product_info


if __name__ == "__main__":
    app.run(debug=True)
