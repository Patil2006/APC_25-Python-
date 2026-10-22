prices = (120, 250, 80, 450, 150)

total = sum(prices)
average = total / len(prices)

highest = prices[0]
lowest = prices[0]

for price in prices:
    if price > highest:
        highest = price
    if price < lowest:
        lowest = price

print("Item prices:", prices)
print("Total bill:", total)
print("Average price:", average)
print("Highest-priced item:", highest)
print("Lowest-priced item:", lowest)