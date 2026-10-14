# ==========================================
# FUNCTIONS: Reusable blocks of code
# ==========================================

# Instead of writing the same code 10 times, you write it once inside a 
# function and "call" it whenever you need it.

print("--- 1. BASIC FUNCTION ---")

def greet_user():
    print("Hey there! Welcome back to your Python journey.")

# Calling the function
greet_user()
greet_user()  # We can call it as many times as we want!


print("\n--- 2. FUNCTIONS WITH PARAMETERS & RETURN VALUES ---")
# Parameters let you pass data *into* the function.
# 'return' lets the function send a result *back out*.

def calculate_total_price(price, tax_rate):
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total

# Let's use our function
laptop_price = 50000
final_price = calculate_total_price(laptop_price, 0.18) # 18% tax
print(f"The final price with tax is: ₹{final_price}")


print("\n--- 3. DEFAULT ARGUMENTS ---")
# Sometimes you want a default value just in case the user doesn't provide one.

def make_coffee(drink_type="Cappuccino"):
    print(f"Brewing a nice cup of {drink_type} for you! ☕")

make_coffee("Espresso")  # Uses the one we provided
make_coffee()            # Falls back to the default ("Cappuccino")
