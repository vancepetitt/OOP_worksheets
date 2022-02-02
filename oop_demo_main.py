from oop_demo_person import Person
from oop_demo_wallet import Wallet

person_one_wallet = Wallet('Black', True)
person_one = Person('Vance', 'Brown', person_one_wallet)

print(person_one.name)

print(person_one.wallet.cash)

person_one.wallet.put_cash_in_wallet(100)

print(person_one.wallet.cash)

