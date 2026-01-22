from to_do import TODO


def task18(customers: list[str]) -> list[str]:

    """
    product = []
    value = str(customers)
    result = value.split("@",".")
    if result not in product:
        product.append(result)
    return list(product)
   """

    result = []
    for customer in customers:
        (username,domain) = customer.split("@")
        #separate_username_domain.split(".")
        (product,domain) = domain.split(".",1)
        if product not in result:
            result.append(product)
    return result

if __name__ == "__main__":
    customer_list = [
        "tgundrey1l@prlog.org",
        "bgrix1u@apache.org",
        "mbreakspear1v@wordpress.com",
        "cdalli1w@ft.com",
        "rclayborn1x@mtv.com",
        "rclayborn1x@mtv.com",
        "jchidlow1y@nasa.gov",
        "jchidlow1y@nasa.gov",
        "kovell1z@washingtonpost.com",
        "kovell1z@washingtonpost.com",
        "kovell1z@washingtonpost.com",
    ]

    print(f"The companies that purchased from you include: {task18(customer_list)}")
