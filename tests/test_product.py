from src.product import Product


def test_product(first_product, second_product):
    assert first_product.name == "Product"
    assert first_product.description == "Description of the product"
    assert first_product.price == 84.50
    assert first_product.quantity == 10

    assert second_product.name == "Product number two"
    assert second_product.description == "Description of the product number two"
    assert second_product.price == 155.87
    assert second_product.quantity == 34


def test_new_product():
    product_4 = new_product(
        Product,
        {
            "name": "Product 4",
            "description": "Description of the product 4",
            "price": 145.75,
            "quantity": 23,
        },
    )
    assert product_4.name == "Product 4"
    assert product_4.description == "Description of the product 4"
    assert product_4.price == 145.75
    assert product_4.quantity == 23
