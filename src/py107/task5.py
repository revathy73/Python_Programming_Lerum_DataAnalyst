def groceries(supermarket: list[dict[str, Any]]) -> float:

    if len(items) == 0:
        return 0.0

    result = 0.0
    total_price = 0.0

    for product,details in supermarket.items():
            how_many = details["quantity"]
            price = details["price"]

        """
            for price in product.values:
            total_price = quantity.values * price.values
            result += total_price
        
        """

if __name__ == "__main__":