import cmath #using cmath to support complex numbers

def main():
  print("\nax^2 + bx + c = 0\n")

  try:
    a = int(input("What is a?: "))
    b = int(input("What is b?: "))
    c = int(input("What is c?: "))
  except:
    print("An error occured, make sure to put intergers")
  else:
    solve = ((-b) - cmath.sqrt(b**2 - 4 * a * c)) / (2 * a)
  
    print("\nAnswer:\n")
    print(f"Positive: {abs(solve)}\n")
    print(f"Negitive: {solve}\n")

main()