#Ramir Maldonado
#CTI-110
#P3HW2
#11/21/2023
#use if/else to determine an employees pay

#Create variables to hold totals paid to epmloyees
num_em = 0
total_reg = 0
total_ot = 0
total_gross = 0

emp_name = input("Enter employee name or type Done to quit: ")
#Loop to control adding employees
while emp_name != "Done":
    num_em += 1
    emp_hours = int(input("Enter employee's hours: "))
    emp_pay = float(input("Enter the employee's pay rate"))

    #calculations
    if emp_hours > 40:
        OT_hours = emp_hours - 40
        reg_hours = 40

    else: #This represents if emp_hours is 40 or less
        OT_hours = 0
        reg_hours = emp_hours

    #Calculate pay
    ot_pay = (emp_pay * 1.5) * OT_hours
    total_ot += ot_pay
    
    reg_pay = emp_pay * reg_hours
    total_reg += reg_pay
    
    gross_pay = ot_pay + reg_pay
    total_gross += gross_pay

    print("------------------------------------")
    print("employee name", emp_name)

    print(f"Hours Worked    Pay Rate    OverTime    OverTime Pay     RegHour Pay     Gross Pay")
    print(f"-------------------------------------------------------------------------------------")
    print(f"{emp_hours}               {emp_pay}             {OT_hours}           {ot_pay}            {reg_pay}           {gross_pay}")
    print()
    emp_name = input("Enter employee name or type Done to quit: ")

#Codes execute when loop is broken
print("loop ended")
print()
print(f"Total number of employees: {num_em}")
print(f"Total regular pay to employees: {total_reg}")
print(f"Total OT pay to employees: {total_ot}")
print(f"Total gross pay to employees: {total_gross}")



