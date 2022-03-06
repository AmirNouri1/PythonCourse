salary = int(input("how much is your Salary ?? "))

if 0 < salary < 1000:
    Result = salary
    print("The Result Is", end=" ")
    print(Result)
elif 1000 < salary <= 2500:
    Result = salary - (salary * 0.1)
    print("The Result Is", end=" ")
    print(Result)
elif 2500 < salary <= 4000:
    Result = salary - (salary * 0.15)
    print("The Result Is", end=" ")
    print(Result)
elif 4000 < salary <= 6000:
    Result = salary - (salary * 0.2)
    print("The Result Is", end=" ")
    print(Result)
elif 6000 < salary <= 8000:
    Result = salary - (salary * 0.25)
    print("The Result Is", end=" ")
    print(Result)
elif  salary < 8000:
    Result = salary - (salary * 0.3)
    print("The Result Is", end=" ")
    print(Result)
else:
    print("error")