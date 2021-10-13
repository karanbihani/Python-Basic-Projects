#Program for pay slip

import csv

def add_rows():
    while True:
        ID = int(input('Enter ID: '))
        name = input('Enter Name: ')
        grade = input("Enter Grade: ")
        salary = int(input("Enter basic salary: "))
        employee_data = [ID, name, grade, salary]
        with open('payroll.csv','a+') as f:
            w = csv.writer(f, delimiter = ' ')
            w.writerow(employee_data)
        cont = input('Add more?(Y/N) => ')
        if cont in 'NnoO':
            print("Data Entered Successfuly!")
            break
        else:
            continue

def fetch_data():
    ID = 0
    while True:
        B = True
        ID = int(input('Enter ID to Display Payslip: '))
        with open('payroll.csv','r+') as f:            
            r = csv.reader(f, delimiter = ' ')
            for Line in r:
                if ID == int(Line[0]):
                    Name, Grade, Salary = str(Line[1]), str(Line[2]), int(Line[3])
                    lop_input = int(input("No. of days on leave: "))
                    lop = (lop_input/30)*Salary
                    B = False
                if B == False:
                    break
        if Grade == 'A':
            HRA = 7500
            PF = (15.75/Salary)*100
            DA = (45/Salary)*100         
        elif Grade == "B":
            HRA = 6000
            PF = (14/Salary)*100
            DA = (30/Salary)*100
        else:    
            HRA = 2000
            PF = (12/Salary)*100
            DA = (27/Salary)*100
            
        net_salary = Salary + HRA + DA
        gross_salary = Salary - PF - lop
        print("\n\nEmpID: ",ID," Name: ",Name," Grade: ",Grade,"\n\n\n\tBasic Salary --> ",Salary,"\n\t\t\tHRA:",HRA)
        print("\t\t\tDA:",DA,"\n\n\tNet Salary -->",net_salary,"\n\t\t\tLOP:",lop,"\n\t\t\tPF:",PF,"\n\n\tGross Salary -->",gross_salary)
        print("\nDo you wish to continue?(Y/N): ")
        c = input()
        if c in "NnoO":
            break
while True:
    print("\tEMPLOYEE PAYSLIP\n\nWhat do you want to do-\n1)Add new employee data \n2)Display existing employee payslip \n3)Exit\n")
    main_choice = int(input())
    if main_choice == 1:
        add_rows()
    elif main_choice == 2:
        fetch_data()
    else:
        print("\n\Exited")
        break
