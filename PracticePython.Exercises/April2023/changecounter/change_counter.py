change = int(input('Change owed: '))


def coin_count(value):
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0
    while value >1:
        quarters = value // 25
        value = value - (quarters*25)
        dimes = value//10
        value = value - (dimes*10)
        nickels = value//5
        value = value - (nickels*5)
        pennies = value
        value = 0

    total_coins = quarters+dimes+nickels+pennies
    return total_coins

    #print(f"You return {total_coins} coins: {quarters} quarters, {dimes} dimes, {nickels} nickels, and {pennies} pennies.")

print(f"You give back {coin_count(change)} coins")