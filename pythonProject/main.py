class Product:
    def __init__(self, name: str, price: int, in_stock:bool):
        self.name = name
        self.price = price
        self.in_stock = in_stock


if __name__ == '__main__':
    external_data ={
        "name": "laptop",
        "price": "999.99",
        "in_stock": "True"

    }

    product =Product(
        name=external_data.get("name"),
        price=external_data.get("price"),
        in_stock=external_data.get("in_stock")
)
    print(type(product.in_stock))