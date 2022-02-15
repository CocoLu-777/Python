# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def sub(n1, n2):
  return n1 - n2

# Multiply
def mul(n1, n2):
  return n1 * n2

# Divide
def di(n1, n2):
  return n1 / n2

dic = {
  "+": add, 
  "-": sub, 
  "*": mul, 
  "/": di
}

def calculator():
  num1 = float(input("Enter the first number: "))
  should_continue = True

  while should_continue:
    num2 = float(input("Enter the second number: "))
    for symbol in dic:
      print(symbol)
    dic_symbol = input("Pick one operation: ")
    calculation_test = dic[dic_symbol]
    answer = calculation_test(num1, num2)

    print(f"{num1} {dic_symbol} {num2} = {answer}")

    con = input("Type 'Y' to continue, type 'N' to stop. ").lower()
    if con == "y":
      num1 = answer
    else:
      should_continue = False
      calculator()

calculator()
