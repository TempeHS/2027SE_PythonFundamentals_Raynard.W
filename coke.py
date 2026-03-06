amount_due = 50
amount_inserted = 0
while amount_inserted < amount_due:
    coin = int(input("Insert coin"))

    if coin in [1, 5, 10, 25]:
        amount_inserted += coin
        print(f"Amount due: {amount_due - amount_inserted}")
change = amount_inserted - amount_due
print(f"Change owed: {change} cents")
