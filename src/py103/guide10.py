from to_do import TODO


def guide10(a: int, b: int, c: int) -> bool:

    condition_1 = a + b > c
    condition_2 = a + c > b
    condition_3 = b + c > a

    if condition_1 == True  and condition_2 == True and condition_3 == True:
        result = True
    else:
        result = False

    return result
    """
    # Another Method :: 1
    if condition_1 and condition_2 and condition_3:
        result = True (return True)
    else:
        result = False (return False) 
    return result
        
    # Another Method :: 2 
    if condition_1 and condition_2 and condition_3:
        return True
    else:
        return False 
        
    # Another Method :: 3
    
    return condition_1 and condition_2 and condition_3
     
    """