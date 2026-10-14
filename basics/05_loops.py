# ==========================================
# LOOPS: Doing things over and over again
# ==========================================

print("--- 1. THE FOR LOOP (Counting / Iterating) ---")
# Perfect when you know how many times you want to do something, 
# or when you want to look at every item in a list.

shopping_list = ["apples", "milk", "bread", "eggs"]

print("Here is your shopping list:")
for item in shopping_list:
    print(f"- {item}")


print("\n--- 2. THE RANGE() FUNCTION ---")
# If you just want to repeat something a specific number of times:
print("Countdown starting:")
for number in range(3, 0, -1):  # Starts at 3, stops before 0, counts down by -1
    print(number)
print("Liftoff! 🚀")


print("\n--- 3. THE WHILE LOOP (Condition-based) ---")
# Great when you don't know *when* something will happen, 
# you just know you want it to keep going until a condition changes.

battery_level = 3

while battery_level > 0:
    print(f"Battery at {battery_level}%. Running smoothly...")
    battery_level -= 1  # Drain 1% each loop

print("Battery dead! 🪫 Please plug in your charger.")


print("\n--- 4. BREAK AND CONTINUE ---")
# 'break' stops a loop completely. 
# 'continue' skips the current step and jumps to the next one.

print("Searching through files...")
for file_num in range(1, 6):
    if file_num == 3:
        print(f"-> Skipped corrupted file {file_num} (using continue)")
        continue
    
    if file_num == 5:
        print(f"-> Critical error found at file {file_num}! Stopping search (using break)")
        break
        
    print(f"Successfully processed file {file_num}")
