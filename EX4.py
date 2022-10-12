a = int(input("entrez un chiffre "))
b = int (input("entrez un autre chiffre "))
o=input("choisi un operation a effectuer ")

#if o=="+":
#   print("a=",a,"b=",b,"a+b=",a+b)
#elif o=="-":
#   print("a=",a,"b=",b,"a-b=",a-b)
#elif o=="/":
#    print("a=",a,"b=",b,"a/b=",a/b)
#elif o=="*":
#    print("a=",a,"b=",b,"a*b=",a*b)
#else:
#    print("signe incorrecte")
match o:
    case "+" :
         print("a=",a,"b=",b,"a+b=",a+b)
    case "-":
        print("a=",a,"b=",b,"a-b=",a-b)
    case "*":
        print("a=",a,"b=",b,"a*b=",a*b)
    case "/":
        print("a=",a,"b=",b,"a/b=",a/b)
    case _:
        print("signe incorrecte")
