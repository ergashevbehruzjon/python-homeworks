file=open("employees.txt","w+")
while True:
    print("""1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")
    op=int(input("Enter your option: "))
    if op==1:
        # emp_id,emp_name,emp_pos,emp_salary=input().split(", ")
        while True:
            emp=input("Enter employee details (id, name, position, salary): ")
            try:
                emp.split(", ")[3]
            except Exception:
                print("-"*50)
                print("Invalid input. Try again.")
                print("-"*50)
            else:
                emps=file.readlines()
                for e in emps:
                    if emp.split(", ")[0] in e:
                        print("-"*50)
                        print("Employee already exists.")
                        print("-"*50)
                        break
                else:
                    file.write(emp+"\n")
                    print("-"*50)
                    print("Employee added.")
                    print("-"*50)
                break
    elif op==2:
        file.seek(0)
        print("-"*50)
        print(file.read(),end="")
        print("-"*50)
    elif op==3:
        file.seek(0)
        emps=file.readlines()
        emp_id=input("Enter employee ID: ")
        for emp in emps:
            if emp_id in emp:
                print("-"*50)
                print(emp.strip())
                print("-"*50)
                break
        else:
            print("-"*50)
            print("Employee not found.")
            print("-"*50)
    elif op==4:
        file.seek(0)
        emps=file.readlines()
        emp_id=input("Enter employee ID: ")
        for index in range(len(emps)):
            if emp_id in emps[index]:
                while True:
                    emp=input("Enter new employee details (id, name, position, salary): ")
                    try:
                        emp.split(", ")[3]
                    except Exception:
                        print("-"*50)
                        print("Invalid input. Try again.")
                        print("-"*50)
                    else:
                        emps[index]=emp+'\n'
                        print("-"*50)
                        print("Employee updated.")
                        print("-"*50)
                        break
                file.truncate(0)
                for emp in emps:
                    file.write(emp)
                break
        else:
            print("-"*50)
            print("Employee not found. If you want to add a new employee, select option 1.")
            print("-"*50)
    elif op==5:
        file.seek(0)
        emp_id=input("Enter employee ID: ")
        emps=file.readlines()
        for index in range(len(emps)):
            if emp_id in emps[index]:
                emps.pop(index)
                file.truncate(0)
                for emp in emps:
                    file.write(emp)
                break
        else:
            print("-"*50)
            print("Employee not found")
            print("-"*50)
    elif op==6:
        break
    else:
        print("-"*50)
        print("Invalid option")
        print("-"*50)
file.close()
# 1001, John Doe, Software Engineer, 75000
# 1002, Behruz, Designer, 50000
# 1003, Person, Backend dev, 100000