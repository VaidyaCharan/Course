try:
    file_data = open('sample.txt', 'r')
    read_txt = file_data.read()
    print(f"Reading file contents:\n{read_txt}")

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")

