def generate_table(number,till):
    print("multiplication table for:",number)
    for i in range(1,till+1):
         print(f"{number} x {i} = {number * i}")
    print()
def generate_table_1to10():
    for number in range(1,11):
        generate_table(number,10)
def main():
    while True:
        print("1.table for a number")
        print("tables from 1 to 10:")
        choice=input("enter your choice:")
    if choice=='1':
        num=int(input("enter a number:"))
        generate_table(num,10)
    elif choice=='2':
        generate_table_1to10()
    else:
        print("invalid choice")
main()