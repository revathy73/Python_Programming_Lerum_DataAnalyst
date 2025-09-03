from to_do import TODO


def task9() -> str:
    return """
    INPUT ATM CARD
    IF CARD is valid
       ENTER PIN
          IF PIN is CORRECT 
          OUTPUT SERVICES
             IF CHOOSE WITHDRAWAL
             OUTPUT enter AMOUNT
                 IF ((AMOUNT >= 500) && (AMOUNT <= 20000))  
                 OUTPUT TAKE YOUR CASH 
                 OUTPUT THANK YOU FOR BANKING WITH US             
                 ELSE
                 OUTPUT CORRECT AMOUNT
             ELSE 
             OUTPUT ERROR
          ELSE
          OUTPUT WRONG PIN        
    ELSE 
       OUTPUT CARD is not valid
    """
