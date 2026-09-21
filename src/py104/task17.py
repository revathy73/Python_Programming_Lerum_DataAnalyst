"""
In each question you are given the variable customers. It contains the
emails of the people who bought a product.

Use this information to solve the questions below.

Which customers purchased multiple times?

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
    "john@nas.gov",
    "ema@post.com"
]
Notes
At least one of your solutions must use a loop
"""

from to_do import TODO


def task17(customers: list[str]) -> list[str]:

    result = []
    for customer in customers:
        if customers.count(customer) >= 2:
            if customer not in result:
                result.append(customer)
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

    print(
        f"The customers that purchased multiple times include: {task17(customer_list)}"
    )
