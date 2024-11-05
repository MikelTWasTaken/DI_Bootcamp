#Daily_Challenge_3

# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples

# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }

# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }

# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}
word_dict={} #create a dictionary

word = input('Enter word: ') #ask for a word
for i, char in enumerate(word): #you need to loop through the word length and if there are any repeating letters so it needs to be enumerated.
    if char not in word_dict: #if the word is not inside you can add it to the dictionary
        word_dict[char] = [] #clarify the list
        word_dict[char].append(i) # Append the i to the list for this letter
print(word_dict)

# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

# Examples

# The key is the product, the value is the price

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

# wallet = "$300"

# ➞ ["Bread", "Fertilizer", "Water"]

#write a function: #A function should do one thing really well and a function should return something.
#functions can be combinesd and run together.
#make sure the loop removes the $ from the number and makes it an int.

shoppinggg = { 
    'chicken':'$40',
    'Wagyu Steak': '$400',
    'Chips':'$2',
    'Cheese': '$10',
    'Salami': '$15',
    'Headphones': '$150'
}

wallet = '$399' #wallet should be a string of numbers to compare with the other strings in the dict
def my_function(price):  
    price = price.replace("$", '')  # Remove the dollar sign
    return int(price)

def budget_for_items(check_items, wallet):  #A function should do one thing really well and a function should return something. - online lessons
    wallet_amount = my_function(wallet)  # Convert wallet amount to an integer. my_function already turns $ into int so I just run wallet in my_function.
    affordable_items = []  # List to store affordable items, to be turned into alphabetical order later.
    
    for item in check_items:  # for Loop for each item in the provided items aka shoppinggg
        price = check_items[item]  # Get the item price by definining what price is.
        item_price = my_function(price)  # Convert the item price to an integer using my function like in waller and value in dict.
        
        if item_price <= wallet_amount:  # Check if the item is affordable
            affordable_items.append(item)  # Add to the list if affordable
    
    affordable_items.sort()  # Sort affordable items alphabetically
    
    if affordable_items:  # If there are affordable items
        return affordable_items #a function modifies something in our program or returns something.

    else:
        return "Nothing"
print(budget_for_items(shoppinggg, wallet))




