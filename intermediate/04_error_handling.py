# ==========================================
# ERROR HANDLING: Keeping your app from crashing
# ==========================================

# When something goes wrong (like dividing by zero or bad user input), 
# 'try' and 'except' let your program handle it gracefully instead of crashing.

print("--- Safe Division Calculator ---")

try:
    num1 = int(input("Enter a number to divide: "))
    num2 = int(input("Enter the divisor: "))
    
    result = num1 / num2
    print(f"Result: {result}")

except ZeroDivisionError:
    print("⚠️ Oops! You cannot divide a number by zero.")
    
except ValueError:
    print("⚠️ Invalid input! Please enter numbers only, not text.")
    
finally:
    print("✨ Thank you for using our safe calculator tool!")
    