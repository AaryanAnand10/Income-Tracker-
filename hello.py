def main():
  expense=input("Enter your daily expenses : ")
  salary=input("Enter your salary : ")
  exp=int(expense)
  sal=int(salary)
  print("Your remaining balance is",sal-exp,"only")

if __name__=="__main__":
  main()
