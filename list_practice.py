# Step 1: Create a Grocery List and print the first and last element
grocery_list = ["apples", "oranges", "strawberries"]
print (grocery_list[0])
print (grocery_list [2])



# Step 2: Adding and Removing Items
# Add bananas
# Add yogurt
# Remove bread
grocery_list.append("bananas")
grocery_list.append ("yogurt")
grocery_list.remove("apples")
print("Updated Grocery List:", grocery_list)

# Step 3: Finding and Updating Items
# Find index of milk
# Replace with almond milk
index = grocery_list.index("strawberries")
grocery_list[index] = "blueberries"

print("After Replacement:", grocery_list)

# Step 4: Sorting and Counting Items
grocery_list.sort()  # Sort list alphabetically
grocery_list.sort(reverse=True)
apple_count = grocery_list.count("apples")  # Count apples
print("Sorted Grocery List:", grocery_list)
print("Number of apples in stock:", apple_count)
