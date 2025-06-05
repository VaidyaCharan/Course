dictnoary = {
    "Alice": 85,
    "Magnus": 10,
    "Gukesh": 90,
    "Mike": 20,
}

inputname = input("Enter the student's name: ")

try:
    studentdetail = dictnoary[inputname]
    print(f"{inputname}'s marks: {studentdetail}")
except KeyError:
    print("Student not found")
