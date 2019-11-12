#The Trip
no_of_studs = int(input())
expenses, exchanges = [], []
for i in range(no_of_studs):
    expenses.append(float(input()))
for i in expenses:
        if ((sum(expenses) / no_of_studs) - i) > 0:
                exchanges.append((sum(expenses) / no_of_studs) - i)
print(exchanges)
print(sum(exchanges))