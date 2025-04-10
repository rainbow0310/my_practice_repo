# Start with a shopping cart
cart = ["apples", "bananas", "cherries"]

# Adding items to the cart
cart.append("donuts")
cart.append("eggs")
cart.append("flour")

print("Cart after adding items:", cart)

# Removing items from the cart
cart.remove("cherries") 
cart.pop(2)  # Forgot you already have "donuts" at home
print("Cart after removing itemssss:", cart)

cart.pop()  # Decided you don't need "flour"
print("Cart after deciding not to buy flour:", cart)

# Sorting the cart
cart.sort()
print("Cart after sorting alphabetically:", cart)

# Reversing the cart (just for fun)
cart.reverse()
print("Cart after reversing order:", cart)

# Adding more fruit
cart.append("bananas")
cart.append("grapes")
cart.append("oranges")
print("Cart with new fruit", cart)

# Slicing: Picking last three items added for a "fruit basket"
fruit_basket = cart[3:]
print("Fruit basket:", fruit_basket)

# Counting occurrences of "banana"
num_bananas = cart.count("bananas")
print("Number of bananas in the cart:", num_bananas)

# Copying the cart
cart_copy = cart[:]
cart_copy.append("grapes")
print("Original cart:", cart)
print("Copied cart with 'grapes' added:", cart_copy)

# Create new list of squares
squares=[]
for i in range(1,10):
    squares.append(i*i)
print(squares)

# Use comprehension
squares=[x*x for x in range(1,10)]
print(squares)

# Filtering using a loop: Only keep items that start with 'b'
b_items = []
for item in cart:
    if item.startswith("b"):
        b_items.append(item)
print("Items starting with 'b' (using loop):", b_items)

# Filtering using list comprehension
b_items_comp = [item for item in cart if item.startswith("b")]
print("Items starting with 'b' (using comprehension):", b_items_comp)

# Generating a list of prices for items from $1 to $9
prices = []
for price in range(1, 10):
    prices.append(price)
print("Item prices:", prices)

# Using comprehension: Generating squares of even prices
even_price_squares = [price ** 2 for price in range(1, 10) if price ** 2 % 2 == 0]
print("Squares of even prices:", even_price_squares)

inventory=[]
# Creating an inventory with default quantities
inventory = [0] * 10  # 10 slots in inventory
inventory[0] = 5  # You have 5 of item 0
inventory[5] = 3  # You have 3 of item 5
print("Inventory:", inventory)

# Sets: Organizing unique book genres
book_genres = {"mystery", "science fiction", "fantasy"}
print("Initial book genres:", book_genres)

# Adding genres (no duplicates allowed)
book_genres.add("non-fiction")
book_genres.add("fantasy")  # "fantasy" already exists, so it won't be added again
print("Book genres after adding:", book_genres)

# Removing duplicates from a list of borrowed book genres
borrowed_books = ["fantasy", "mystery", "mystery", "science fiction", "romance", "romance", "romance"]
unique_borrowed_books = set(borrowed_books)
print("Unique borrowed book genres:", unique_borrowed_books)

# Converting back to a list for further processing
borrowed_books_list = list(unique_borrowed_books)
print("Borrowed books list:", borrowed_books_list)

# Dictionaries: Favorite snacks of a study group
fav_snacks = {
    "Kathleen": "chips", 
    "Wade": "popcorn", 
    "Lucas": "chocolate", 
    "Zaynah": "gummy bears"
}

# Accessing a value
kathleen_snack = fav_snacks["Kathleen"]
print("Kathleen's favorite snack is:", kathleen_snack)

# Looping through the dictionary: Displaying favorite snacks
# For loop returns the key of the dictionary and assigns it to the
# variable person
print("Study group snack preferences:")
for person in fav_snacks:
    print(f"{person} loves {fav_snacks[person]}")
# An f-string (formatted string) in Python allows you to embed variables 
# and even expressions directly into a string by prefixing it with the 
# letter f and enclosing the variables or expressions in curly braces {}. 
# It's a concise and readable way to format strings.

# Using items() to loop through key-value pairs
print("Snack preferences (using items()):")
for person, snack in fav_snacks.items():
    print(f"{person} prefersssss {snack}")

# Adding a new member's favorite snack
if "Bob" in fav_snacks:
    print("Bob's favorite snack is:", fav_snacks["Bob"])
else:
    fav_snacks["Bob"] = "pretzels"
    print("Added Bob's favorite snack:", fav_snacks["Bob"])

# Checking for a snack
if "gummy bears" in fav_snacks.values():
    print("Someone loves gummy bears!")

# Creating an empty dictionary for later use
empty_snacks = {}

# Updating the dictionary
fav_snacks["Lucas"] = "ice cream sandwiches"  # Lucas changed his mind
print("Updated snack preferences:", fav_snacks)

# Sorting keys and values in dictionary
print(sorted(fav_snacks.keys()))
print(sorted(fav_snacks.values()))
