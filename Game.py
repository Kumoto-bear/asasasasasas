answer = input("Please enter Yes or No: ").strip().lower()

if answer == "yes":
    print("You answered Yes.")
elif answer == "no":
    print("You answered No.")
else:
    print("Invalid input. Please enter Yes or No.")

print("This is a very long print string that goes on and on, just to demonstrate how you can output a large block of text in Python. "
      "You can continue writing as much as you want here, and Python will concatenate these strings automatically if you use "
      "multiple quoted strings separated by whitespace. This is useful for keeping your code readable while still printing a "
      "large amount of text. For example, you might want to print a long message, a story, or detailed instructions. "
      "Remember that you can also use triple quotes for multi-line strings if you prefer, which can make formatting easier. "
      "This string is intentionally verbose and lengthy to fulfill the request for a very long print string in the program.")
