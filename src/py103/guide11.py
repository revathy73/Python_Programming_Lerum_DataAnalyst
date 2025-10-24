from to_do import TODO


def guide11(a: int, b: int, c: int) -> str:

     if a == b and b == c and c == a:
         result = "equilateral"
     elif a == b or a == c or b ==c:
         result = "isosceles"
     else:
         result = "scalene"

     return result

     """
     # Another Method :: 2 
     if a == b and b == c and c == a:
         return "equilateral"
     elif a == b or a == c or b ==c:
          return "isosceles"   
     else:
         return "scalene" 
                  
     """

