# Define a function to calculate the number of chocolate bar and the change.
def chocolate(total_money, price):
    num = total_money // price
    change = total_money % price
    # Use if to change the plurality.
    if num < 2:
        print('You can buy 1 chocolate bars, and have %s dollar left over.' % change)
    if num >= 2:
        print('You can buy %s chocolate bars, and have %s dollar left over.' % (num, change))


# For instance, the user have 100 dollar and the price is 7 dollar.
# Type the total money first and price after it.
chocolate(100, 7)
# The output is: You can buy 14 chocolate bars, and have 2 left over.
