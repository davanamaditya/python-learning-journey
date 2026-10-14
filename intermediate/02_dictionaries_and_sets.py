# ==========================================
# DICTIONARIES & SETS: Key-value lookups & Unique items
# ==========================================

print("--- 1. DICTIONARIES (Key-Value Pairs) ---")
# Think of a dictionary like a real phone book or a profile card. 
# You look up a "key" to find its "value".

student_profile = {
    "name": "Aditya",
    "course": "Electronics & Communication",
    "year": 1,
    "is_coding": True
}

print(f"Student Name: {student_profile['name']}")
print(f"Branch: {student_profile['course']}")

# Adding a new key-value pair
student_profile["laptop"] = "Lenovo Yoga"
print(f"Updated Profile: {student_profile}")

# Safely getting a value using .get() (won't crash if the key doesn't exist)
grade = student_profile.get("gpa", "Grade not available yet")
print(f"GPA: {grade}")


print("\n--- 2. SETS (Unique collections) ---")
# Sets automatically get rid of duplicate items and don't care about order.

visited_cities = {"Delhi", "Mumbai", "Chennai", "Delhi", "Mumbai"}
print(f"Unique cities visited: {visited_cities}")  # Notice duplicates are removed automatically!