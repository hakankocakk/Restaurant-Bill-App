tables = dict()
for i in range(10):
    tables[i] = 0


def addBill():
    tableno = int(input("Table No: "))
    currentValue = tables[tableno]
    addedAmount = float(input("Added Amount: "))
    total = currentValue + addedAmount
    tables[tableno] = float(total)
    print("Bill: {}".format(tables[tableno]))


def payBill():
    tableno = int(input("Table No: "))
    currentValue = tables[tableno]
    paidAmount = float(input("Paid Amount: "))
    total = currentValue - paidAmount
    if total <0:
        print("There is an error in the value, please enter a correct value!!!")
    else:
        tables[tableno] = float(total)
        print("Remaining Bill: {}".format(tables[tableno]))


def billControl(file_name):

    try:
        file = open(file_name)
        datas = file.read()
        datas = datas.split("\n")
        datas.pop()
        file.close()
        flag = True

    except FileNotFoundError:
        file = open(file_name,"w")
        file.close()
        print("It started for the first time! File created!")
        flag = False

    if flag:
        for i in enumerate(datas):
            tables[i[0]] = float(i[1])

    else:
        pass

def uptaderecord():
    file = open("bill records.txt","w")
    for i in range(10):
        price = tables[i]
        price = str(price)
        file.write(price + "\n")
    file.close()


def main():
    billControl("bill records.txt")
    while True:
        print("""
[1] See the tables
[2] Add bill
[3] Pay bill
[q] Close
            """)

        choice = (input("Your transaction: "))

        if choice == "1":
            for i in range(10):
                print("Bill for table {}: {}".format(i, tables[i]))
            print("İşlem tamamlandı!. Ana menüye dönmek için entera basın")
            uptaderecord()
            input()


        elif choice == "2":
            addBill()
            print("Process completed!. Press enter to return to the main menu")
            uptaderecord()
            input()

        elif choice == "3":
            payBill()
            print("Process completed!. Press enter to return to the main menu")
            input()

        elif choice == "q" or choice == "Q":
            quit()


main()
