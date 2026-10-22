# Create a dictionary of programming languages and their creators.
# Display each key and value using a loop.

languages = {
    "Python": "Guido van Rossum",
    "Java": "James Gosling",
    "C++": "Bjarne Stroustrup",
    "JavaScript": "Brendan Eich"
}

for key, value in languages.items():
    print(key, ":", value)