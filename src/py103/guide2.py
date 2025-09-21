from to_do import TODO


def guide2(month: str) -> bool:

     if month.upper() == "NOVEMBER":
         result = True
     else:
         result = False

     return result

     # return month.lower == "november"

     #return month.upper() == "NOVEMBER"



if __name__ == "__main__":

     # month ="December"
     print(guide2(month = "December"))

     # month ="November"
     print(guide2(month = "November"))

     # month ="March"
     print(guide2(month="March"))

     # month ="NOVEMBER"
     print(guide2(month="NOVEMBER"))

     # month ="January"
     print(guide2(month="January"))

     # month ="NoVemBeR"
     print(guide2(month="NoVemBeR"))