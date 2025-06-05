line1 = input("Enter text to write to the file: ")

with open('output.txt', 'w') as file:
    file.write(f"{line1}\n")
    print("Data successfully written to output.txt")

line2 = input("Enter additional text to append: ")

with open('output.txt', 'a') as file:
    file.write(f"{line2}\n")
    print("Data successfully appended")

with open('output.txt', 'r') as file:
    fileread = file.read()
    print(f"\nFinal content of Output.txt:\n{fileread}\n")