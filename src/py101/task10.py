from to_do import TODO


def task10() -> str:
    return """
    INPUT EMAIL
    INPUT PASSWORD
    INPUT Login
       IF(EMAIL == empty)
       OUTPUT Enter EMAIL
          IF(PASSWORD.length <= 6)
          OUTPUT Enter more than six characters
          ELSE(PASSWORD.length > 6)
          OUTPUT YOU ARE SUCCESSFULLY LOGGED IN    
    """
