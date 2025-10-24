from to_do import TODO


def guide9(email: str) -> bool:

    is_not_empty = len(email) > 0
    contains_at_sign = "@" in email
    has_correct_ending = ".se" in email[-3:]


    if is_not_empty == True and contains_at_sign == True and has_correct_ending == True:
        result = True
    else:
        result = False

    return result

if __name__ == "__main__":

    # email = student@gmail.com
    print(guide9(email = "student@gmail.com"))

    # email = ""
    print(guide9(email = ""))

    # email = student#gmail.se
    print(guide9(email = "student#gmail.se"))

    # email = student@gmail.se
    print(guide9(email = "student@gmail.se"))

    """
    # Another Method ::1
    if is_not_empty == True and contains_at_sign == True and has_correct_ending == True:
         return True
    else:
         return False
         
    # Another Method ::2
    if is_not_empty and contains_at_sign and has_correct_ending:
        return True
    else:
        return False
        
    # Another Method ::3
    return is_not_empty and contains_at_sign and has_correct_ending
    
    # Another Method ::4
    
    return len(email) > 0 and "@" in email and ".se" in email[-3:]   
       
    is_not_empty = len(email) > 0
    contains_at_sign = "@" in email
    has_ending = ".se" in email[-3:]

    if is_not_empty == True and contains_at_sign == True and has_ending == True:
        result = True
    else:
        result = False

    return result

    if len(email) > 0 and "@" in email and ".se" in email[-3:]:
        result = True
    else:
        result =False

    return result

    return len(email) > 0 and "@" in email  and ".se" in email[-3:]

    if is_not_empty and contains_at_sign and has_ending:
        return True
    else:
        return False

    return
    
    """
