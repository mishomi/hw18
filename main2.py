def sakomisio(func):
    def wrapper(balance, money):
        if balance < 1:
            raise ValueError ("საკომისიო გადასახადისთვის არასაკმარისი თანხა")
        else:
            return func(balance - 1, money)
    return wrapper

@sakomisio
def transaction(balance, money):
    if balance >= money:
        return balance - money
    else:
        raise ValueError ("არასაკმარისი თანხა")
try:
    balance = 10
    money_to_pay = 5
    new_balance = transaction(balance, money_to_pay)
    print("ბალანსი ტრანზაქციის შემდეგ:", new_balance)
except ValueError as v:
    print("შეცდომა დაფიქსირდა: ", v)
try:
    balance = 0
    money_to_pay = 5
    new_balance = transaction(balance, money_to_pay)
    print("ბალანსი ტრანზაქციის შემდეგ:", new_balance)
except ValueError as v:
    print("შეცდომა დაფიქსირდა: ", v)

try:
    balance = 2
    money_to_pay = 5
    new_balance = transaction(balance, money_to_pay)
    print("ბალანსი ტრანზაქციის შემდეგ:", new_balance)
except ValueError as v:
    print("შეცდომა დაფიქსირდა: ", v)