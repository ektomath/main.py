# Jag bekräftar härmed att jag inte kommunicerar med andra personer än kursens lärare under tentans gång.
# Jag är medveten om att fusk i tentan kan leda till disciplinåtgärder.

############################## UPPGIFT 1 ##########################################################################
def norway_pandemic():
    region = input("Hvor er du bosatt?")
    if region.startswith("V"):
        print("Velkommen til Norge!")
    else:
        vaccine = input("Er du fullvaksinert?")
        if vaccine == "ja":
            print("Velkommen til Norge!")
        else:
            covid = input("Har du gjennomgått koronasykdom de siste seks månedene?")
            if covid == "ja":
                print("Velkommen til Norge!")
            else:
                print("Velkommen til Norge, men du må teste deg och sitte i karantene.")


############################## UPPGIFT 2 ##########################################################################

def alter(string):
    newstr = ""

    if len(string) % 2 == 1:
        for i in range(0, len(string)-1, 2):
            a, b = string[i], string[i+1]
            newstr += b
            newstr += a
        return newstr + string[len(string)-1]

    else:
        for i in range(0, len(string), 2):
            a, b = string[i], string[i+1]
            newstr += b
            newstr += a
        return newstr


def scramble(string):
    first = string[0]
    last = string[len(string)-1]
    if len(string) == 1:
        return first
    else:
        return first + alter(string[1:len(string)-1]) + last


def scrambles(text):
    list = text.split(' ')
    newtext = ""
    for item in list:
        newtext += scramble(item) + " "
    return newtext

############################## UPPGIFT 3 ##########################################################################


class Account:
    def __init__(self, nr, balance):
        self.nr = nr
        self.balance = balance

    def getBalance(self):
            print(self.balance)

    def setBalance(self, b):
        self.balance = b


def transfer(account1, account2, amount):
    if account1.balance < amount:
        print("Not enough money")
    else:
        account1.setBalance(account1.balance - amount)
        account2.setBalance(account2.balance + amount)
        print("OK")

acc1 = Account('0010', 2000)
acc2 = Account('0201', 2000)
