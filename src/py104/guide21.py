from to_do import TODO


def guide21(a: set[str], b: set[str]) -> set[str]:
    # solution 1: for loop in set
    """
    result = set()
    for email in b:
        if email not in a:
            result.add(email)

    return result

    # solution 2: set comprehension
    result = set((email for email in b if email not in a))
    return  result

    # solution 2: set comprehension(Refactoring)
    return set((email for email in b if email not in a))
    """
    # solution 3: type casting from  List
    result = [email for email in b if email not in a]
    return set(result)


if __name__ == "__main__":

    # a= {"jim@gmail.com","jane@outlook.se","info@alpha.se"} ,
    # b= {"jim@gmail.com","jane@outlook.se","info@beta.se","info@vcs.se"}
    print(guide21(a= {"jim@gmail.com","jane@outlook.se","info@alpha.se"} ,
                  b= {"jim@gmail.com","jane@outlook.se","info@beta.se","info@vcs.se"}))
     # --->  {"info@beta.se", "info@vcs.se"}
