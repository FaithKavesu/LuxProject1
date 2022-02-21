year = int(input("Enter year: "))
calculateRemainder = year % 4
calculateRemainder00 = year % 100
calculateRemainder400 = year % 400

if calculateRemainder == 0 and calculateRemainder00 != 0:
  
  print(f"{year} is a Leap Year")

elif calculateRemainder00 == 0 and calculateRemainder400 == 0:

  print(f"{year} is a Leap Year" )

else:

  print(f"{year} is not a Leap Year")
