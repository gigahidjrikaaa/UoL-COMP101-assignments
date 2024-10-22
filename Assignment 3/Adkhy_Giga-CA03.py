# Adkhy_Giga 201847335  October2024 CA-03.py
# Calculating the age of a cat in human years.

print(
    "Main Menu",
    "\nA. Junior Cat age in months (8, 12, 18, 24)",
    "\nB. Prime Cat age in years 3, 4, 5, 6",
    "\nC. Cat age articles",
    "\nX. Exit Program"
)

prompt = input("Prompt: ")
print("===================================================")
# valid_prompts = ['A', 'a', 'B', 'b', 'C', 'c', 'X', 'x']
invalid_message = "Choice invalid. Exiting..."
about = "Cat age calculator is used to find the equivalent of cat age in human years.\nThere are different calculations for each life stage of a cat. They are:\n1. Kitten: 0 - 7 months\n2. Junior: 8 - 24 months\n3. Prime: 3 - 6 years\n4.Mature: 7 - 10 years\n5. Senior: 11 - 14 years\n6. Geriatric: 15 - 18 years.\n"
references_list = "Further reading can be seen here:\n1. "

if prompt == 'A' or prompt == 'a':
    age = int(input("Age in months (8, 12, 18, or 24): "))
    if age == 8 or age == 12 or age == 18 or age == 24:
        print("Age of the cat is equivalent to", age + 3, "human years.")
    else:
        print(invalid_message)
elif prompt == 'B' or prompt == 'b':
    age = int(input("Age in years (3, 4, 5, or 6): "))
    if age == 3 or age == 4 or age == 5 or age == 6:
        print("Age of the cat is equivalent to", (age - 3) * 4 + 28, "human years.")
    else:
        print(invalid_message)
elif prompt == 'C' or prompt == 'c':
    print(about)
    print(references_list)
elif prompt == 'X' or prompt == 'x':
    print("Exiting... Have a good day.")
else:
    print(invalid_message)

print("Goodbye!")