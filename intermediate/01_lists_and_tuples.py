# ==========================================
# LISTS & TUPLES: Organizing collections of data
# ==========================================

print("--- 1. LISTS (Mutable / Changeable) ---")
# Lists are like physical shopping lists. You can add, remove, and change things.

favorite_games = ["Minecraft", "Valorant", "GTA V"]
print(f"My original games: {favorite_games}")

# Add a new game
favorite_games.append("Cyberpunk 2077")
print(f"After adding one: {favorite_games}")

# Accessing items by index (Python starts counting at 0!)
print(f"My absolute favorite game is: {favorite_games[0]}")
print(f"The last game on my list is: {favorite_games[-1]}") # -1 grabs the very last item

# Removing an item
favorite_games.remove("Valorant")
print(f"After removing Valorant: {favorite_games}")


print("\n--- 2. TUPLES (Immutable / Unchangeable) ---")
# Tuples are locked down lists. Once you create them, you cannot change, 
# add, or remove items. Great for coordinates, settings, or fixed data.

screen_resolution = (1920, 1080)
print(f"Screen Width: {screen_resolution[0]}")
print(f"Screen Height: {screen_resolution[1]}")

# screen_resolution[0] = 1280  # This would crash! Tuples cannot be modified.