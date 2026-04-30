import os
import csv
import json
print("Practice 4")
print("Task1")
print("Checking file...")
file_path = "C:/Users/Самир/Desktop/Python/students.csv"

if not os.path.exists(file_path):
    print("Error: students.csv not found. Please download the file from LMS.")
    exit()
print("File found: students.csv")
print("Checking output folder...")

if not os.path.exists("output"):
    os.makedirs("output")
    print("Output folder created: output/")
else:
    print("Output folder already exists")
print("_______________________________")
print("Task2")
with open(file_path, encoding="utf-8") as f:
    reader = csv.DictReader(f)
    students = list(reader)

print(f"Total students: {len(students)}")
print("First 5 rows:")
print("_______________________________")
for s in students[:5]:
    print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")
print("_______________________________")
print(" ")
print("_______________________________")
print("Task3")
country_counts = {}

for s in students:
    country = s["country"]
    if country in country_counts:
        country_counts[country] += 1
    else:
        country_counts[country] = 1

print("Students by Country :")
print("_______________________________")
for country, count in country_counts.items():
    print(f"{country} : {count}")
print("_______________________________")
top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]
print(" ")
print("_______________________________")
print("Top 3 Countries:")

for i, (country, count) in enumerate(top_3, 1):
    print(f"{i}. {country} : {count}")
print("_______________________________")
print(" ")
print("Task4")
result = {
    "analysis": "Country Analysis",
    "total_students": len(students),
    "total_countries": len(country_counts),
    "top_3_countries": [
        {"country": c, "count": n} for c, n in top_3
    ],
    "all_countries": country_counts
}

with open("output/result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print("______________________________")
print("ANALYSIS RESULT")
print("______________________________")
print("Analysis : Country Analysis")
print(f"Total students : {len(students)}")
print(f"Total countries : {len(country_counts)}")

print("______________________________")
print("Top 3 Countries:")

for i, (country, count) in enumerate(top_3, 1):
    print(f"{i}. {country} : {count}")

print("______________________________")
print("Result saved to output/result.json")