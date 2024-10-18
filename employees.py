employees = []
def add_or_update_employee(name, hours_worked, hourly_wage):
    for employee in employees:
        if employee['name'].lower() == name.lower():
            employee['hours_worked'] = hours_worked
            employee['hourly_wage'] = hourly_wage
            print(f"Employee '{name}' updated.")
            return
    employee = {
        'name': name,
        'hours_worked': hours_worked,
        'hourly_wage': hourly_wage
    }
    employees.append(employee)
    print(f"Employee '{name}' added to the payroll system.")
def calculate_pay(hours, wage):
    if hours > 40:
        regular_pay = 40 * wage
        overtime_pay = (hours - 40) * wage * 1.5
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = hours * wage
    return total_pay
def calculate_total_payroll():
    total_payroll = 0
    print("Payroll details:")
    for employee in employees:
        name = employee['name']
        hours = employee['hours_worked']
        wage = employee['hourly_wage']
        pay = calculate_pay(hours, wage)
        total_payroll += pay
        print(f"{name}: Worked {hours} hours, Hourly wage: ${wage}, Total pay: ${pay}")
    print(f"\nTotal payroll: ${total_payroll}")
add_or_update_employee("harsh", 45, 20) 
add_or_update_employee("yash", 38, 15)    
add_or_update_employee("diksha", 50, 25) 
calculate_total_payroll()
add_or_update_employee("sahil", 50, 22)
calculate_total_payroll()