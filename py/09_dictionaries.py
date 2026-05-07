students = [
    {"name": "Alice",
     "age": 20,
     "grade": "A",
     "courses": ["History", "Art"]
    },
    {
    "name": "Charlie",
    "age": 23,
    "grade": "C",
    "courses": ["Biology", "Chemistry"]
    },
    {
    "name": "Lol",
    "age": 23,
    "grade": "C",
    "courses": ["Biology", "Chemistry"]
    }
]

print(students[1]["name"])


student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science, Biology",
        "grades": [85, 92, 78]
    },

    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    }
}

print(student_records["student_001"]["name"], student_records["student_002"]["major"])