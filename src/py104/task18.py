"""
In each question you are given the variable customers. It contains the
emails of the people who bought a product.

Use this information to solve the questions below.

Which companies purchased the product?

Save your result in a variable called result of type List<String>.

result cannot have repeated elements.
Example Solution
Assume that
customers is
[
    "mary@tv.com",
    "john@nas.gov",
    "john@nas.gov",
    "ema@post.com",
    "ema@post.com"
]
Then
result is
[
    "tv",
    "nas",
    "post"
]
Hint
Look at the domain of each email
Notes
At least one of your solutions must use a loop
"""

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
