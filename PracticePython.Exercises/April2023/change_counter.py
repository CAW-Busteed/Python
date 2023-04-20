change = int(input('Change owed: '))
quarters = 0
dimes = 0
nickels = 0
pennies = 0

while change <= 100 and change >1:
    # if change >= 25:
        quarters = change // 25
        change = change - (quarters*25)
    # elif change >= 10 and change <25:
        dimes = change//10
        change = change - (dimes*10)
    # elif change >=5 and change <10:
        nickels = change//5
        change = change - (nickels*5)
    # elif change <5:
        pennies = change
        change = 0

total_coins = quarters+dimes+nickels+pennies

print(f"You return {total_coins} coins: {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.")
