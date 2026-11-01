# Self-Assessment
# 1. The first bug I spotted was from reading the traceback. This shows that I can
# use error messages to narrow down where a problem is happening.
#
# 2. apply_discount(price, tier) takes a price and a discount tier. It checks
# whether the tier is gold, silver, bronze, or something else, applies the
# appropriate discount, and returns the discounted price. A colleague could
# use it without reading the function body because the inputs and purpose are
# clear from the function name and parameters.
#
# 3. I used AI to help understand and fix the bugs in Exercise 5.

# --- Exercise 1 ---

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")


# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

price = 200

print(f"gold:   ${apply_discount(price, 'gold'):.2f}")
print(f"silver: ${apply_discount(price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(price, 'bronze'):.2f}")
print(f"none:   ${apply_discount(price, 'none'):.2f}")


# --- Exercise 3 ---

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
final = discounted + tax

print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${final:.2f}")


def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 'gold', 0.07) = ${final_price(200, 'gold', 0.07):.2f}")


# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# --- Exercise 5 ---

sales = [120, 80, 250, 175, 90]

total = 0

for sale in sales:
    # The total must accumulate each sale instead of replacing the previous total.
    total += sale

print(f"Total: ${total}")

count = 0

for sale in sales:
    count += 1

print(f"Count: {count}")

i = 0

while i < len(sales):
    print(sales[i])
    i += 1


# --- Exercise 6 ---

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)

# Scope explanation:
# The x outside the function is a global variable.
# The x inside double_it() is a local variable.
# The local x does not change the global x.