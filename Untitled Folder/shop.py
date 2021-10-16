def menu(triangular_poppet_unit_price, spring_roll_unit_price):
    triangular_poppet = 0
    spring_roll = 0
    triangular_poppet += triangular_poppet_unit_price
    spring_roll += spring_roll_unit_price
    d = {}
    d['triangular_poppet'] = triangular_poppet
    d['spring_roll'] = spring_roll
    return (d)


def calculate_bill(order, amount):
    if order == 'triangular_poppet':
        price = triangular_poppet_unit_price * amount
    else:
        price = spring_roll_unit_price * amount
    return (price)


def MyBakeShop():
    y = (calculate_bill(order, amount))
    print(f'your total_bill is {y} Rs')
    var = (switch_stock(triangular_poppet_in_stock, spring_roll_in_stock, order, amount))
    if var['triangular_poppet'] <= 0 or var['spring_roll'] <= 0:
        triangular_poppet += 50
        spring_roll += 50
        var['triangular_poppet'] = triangular_poppet
        var['spring_roll'] = spring_roll
        print(var)
    print(var)  ##stock nhi set horhy 0 hony pt

    salary_check = input('Enter y or Y for finding employee salary')
    if salary_check == ('y' or 'Y'):
        employee_salary(employee_A_wage_rate, employee_B_wage_rate, employee_A_hrs, employee_B_hrs)
    else:
        print('checkout another things in my bake shop')


def switch_stock(triangular_poppet_in_stock, spring_roll_in_stock, order, amount):
    triangular_poppet = 0
    spring_roll = 0
    triangular_poppet += triangular_poppet_in_stock
    spring_roll += spring_roll_in_stock
    d = {}
    d['triangular_poppet'] = triangular_poppet
    d['spring_roll'] = spring_roll
    x = d[order]  # this minus the value of stock from user enter amount to mange it
    x -= amount
    d[order] = x
    return (d)


def employee_salary(employee_A_wage_rate, employee_B_wage_rate, employee_A_hrs, employee_B_hrs):
    i = employee_A_wage_rate * employee_A_hrs
    j = employee_B_wage_rate * employee_B_hrs
    bonus_hr = 500
    check = input("choose a or b")
    if check == "a":
        bonus_a = int(input("enter bonus hrs for employee A:"))
        if (bonus_a ) == 0:
            print('employee A salary is', i)
        elif (bonus_a ) > 0:
            i += (bonus_hr * bonus_a)
    if check == "b":
        bonus_b = int(input("enter bonus hrs for employee B:"))
        if (bonus_b) == 0:
            print('employee B salary is ', j)
        elif (bonus_b) > 0:
            j += (bonus_hr * bonus_b)
            print(' employee B salary is ', j)
        return


employee_A_wage_rate = 300
employee_B_wage_rate = 350
employee_A_hrs = 8
employee_B_hrs = 10

triangular_poppet_in_stock = 10
spring_roll_in_stock = 15

triangular_poppet_unit_price = 25
spring_roll_unit_price = 30

while True:
    print('''  ***** WELCOME ****
            to My Bake Shop
            There is menu of snacks.
            Enter NO if you want to buy nothing''')
    try:
        print(menu(triangular_poppet_unit_price, spring_roll_unit_price))
        order = input('Enter the name of snacks you want to buy\n>>>')
        order = order.lower()
        if order == 'no':
            print('Thanks for coming , you can go now!!!!')
        else:
            amount = int(input(f'enter how many {order} you want to buy\n>>>'))
            MyBakeShop()
    except ValueError:
        print('Please select correctly')

