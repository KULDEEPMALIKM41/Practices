import json

def readData():
    with open("statics/attendance.json", "r") as read_file:
        return json.load(read_file)

def monthWiseEmp(employee_details, month):
    return [employee for employee in employee_details if month in employee['date']] 

def removeAbsentEmp(employees):
    return [employee for employee in employees if employee['total_hours'] >= 4 or employee['weekday'] == 7 or employee['weekday'] == 1] 
    
def genderWiseEmpFilter(employees):
    male_emp, female_emp = [], []
    for emp in employees:
        if emp['gender'] == 'Male':
            male_emp.append(emp)
        else: 
            female_emp.append(emp)
    return (male_emp,female_emp)

def empOvertimePaid(employees):
    weekEndEmpOvertimePaid = 0
    for emp in employees:
        if (emp['weekday'] == 7 or emp['weekday'] == 1) and emp['designation'] == "Worker":
            per_hour_salary = (emp['per_day_salary'] /8)*2
            weekEndEmpOvertimePaid += per_hour_salary*emp['total_hours']
        elif emp['designation'] == "Worker":
            if emp['total_hours'] > 8:
                per_hour_salary = (emp['per_day_salary'] /8)*2
                weekEndEmpOvertimePaid += per_hour_salary*(emp['total_hours']-8)        
    return weekEndEmpOvertimePaid

def empBasicSalary(employees):
    weekDayEmpSalary = 0
    for emp in employees:
        if (emp['weekday'] != 7 and emp['weekday'] != 1):
            if emp['total_hours'] >= 8:
                weekDayEmpSalary += emp['per_day_salary']
            elif 4 <= emp['total_hours'] < 8:
                weekDayEmpSalary += emp['per_day_salary']/2
    return weekDayEmpSalary

def calculateBonus(male_total_salary, female_total_salary):
    if male_total_salary < female_total_salary:
        return male_total_salary*(1/100)
    else:
        return female_total_salary*(1/100)

employee_details = readData()
feb_emp = monthWiseEmp(employee_details,"Feb")
feb_emp = removeAbsentEmp(feb_emp)
male_emp,female_emp = genderWiseEmpFilter(feb_emp)
male_overtime_paid = empOvertimePaid(male_emp)
female_overtime_paid = empOvertimePaid(female_emp)
male_emp_basic_salary = empBasicSalary(male_emp)
female_emp_basic_salary = empBasicSalary(female_emp)

Basic_Salary = male_emp_basic_salary + female_emp_basic_salary
Overtime = male_overtime_paid + female_overtime_paid
Bonus = calculateBonus(male_overtime_paid+male_emp_basic_salary, female_overtime_paid+female_emp_basic_salary)
Total_Salary = Basic_Salary + Overtime + Bonus

print("Basic Salary :\t\t\t\t",round(Basic_Salary,2))
print("Overtime :\t\t\t\t",round(Overtime,2))
print("Bonus :\t\t\t\t\t",round(Bonus,2))
print("Total Salary :\t\t\t\t",round(Total_Salary,2))