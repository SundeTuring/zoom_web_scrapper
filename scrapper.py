from network import Networker


class Scrapper:
    def __init__(self, url):
        self.soup = Networker.get_data(url)

    def get_product_info(self):
        product_name = self.get_product_name()
        product_img = self.get_product_img()
        product_price = self.get_product_price()
        product_dict = {
            "name": product_name,
            "image": product_img,
            "price": product_price,
        }

        return product_dict

    def get_product_name(self):
        product_name = self.soup.find(name="h2", class_="Text_Text__VJDNU").text
        return product_name

    def get_product_img(self):
        product_img = self.soup.find_all(class_="Cell_Image__K_7_C", )
        product_img = product_img[1]["src"]

        return product_img

    def get_product_price(self):
        product_price_info = self.soup.find(class_="CellPrice_Block__2KAo4")
        product_price = self.format_price(product_price_info)

        return product_price

    @staticmethod
    def format_price(price):
        formatted_price = price.text.split("$")[1].strip()
        formatted_price = formatted_price.split(",")[0]

        return float(formatted_price)
