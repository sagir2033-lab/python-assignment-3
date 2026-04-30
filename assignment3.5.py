import os
import csv
import json
print("Practice 5")
print("Task1")
def check_files():
    print("Checking file...")
    if not os.path.exists("C:/Users/Самир/Desktop/Python/students.csv"):
        print("Error: students.csv not found. Please download the file from LMS.")
        return False

    print("File found: students.csv")
    print("Checking output folder...")

    if not os.path.exists("output"):
        os.makedirs("output")
        print("Output folder created: output/")
    else:
        print("Output folder already exists: output/")

    return True
def load_data(filename):
    print("Loading data...")

    with open(filename, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)

    print(f"Data loaded successfully: {len(data)} students")
    return data
def preview_data(students, n=5):
    print(f"First {n} rows:")
    print("_____________________________")
    for s in students[:n]:
        print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

    print("_____________________________")

if check_files():
    students = load_data("C:/Users/Самир/Desktop/Python/students.csv")
    preview_data(students, 5)
print(" ")
print("Task2")
def analyse_countries(students):
    country_counts = {}
    for s in students:
        country = s["country"]
        if country in country_counts:
            country_counts[country] += 1
        else:
            country_counts[country] = 1
    top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]
    result = {
        "total_students": len(students),
        "total_countries": len(country_counts),
        "top_3": top_3,
        "all_countries": country_counts
    }

    return result
print(" ")
print("_____________________________")
print("Country Analysis")
print("_____________________________")
result = analyse_countries(students)
print(f"Total students : {result['total_students']}")
print(f"Total countries : {result['total_countries']}")
print("_____________________________")
print("Top 3 Countries:")

for i, (country, count) in enumerate(result["top_3"], 1):
    print(f"{i}. {country} : {count}")
print("_____________________________")
print(" ")
print("Task3")
def lambda_analysis(students):
    high_gpa = list(filter(lambda s: float(s['GPA']) > 3.5, students))
    gpa_values = list(map(lambda s: float(s['GPA']), students))
    good_attendance = list(
        filter(lambda s: float(s.get('class_attendance_percent', 0)) > 90, students)
    )
    print("Lambda / Map / Filter")
    print("_____________________________")
    print(f"GPA > 3.5 : {len(high_gpa)}")
    print(f"GPA values (first 5) : {gpa_values[:5]}")
    print(f"class_attendance_percent > 90 : {len(good_attendance)}")
    print("_____________________________")
lambda_analysis(students)
print(" ")
print('Task4')
def main():
    if not check_files():
        return
    try:
        students = load_data(file_path)
        preview_data(students, 5)
        result = analyse_countries(students)

        print("Country Analysis")
        print("______________________________")
        print(f"Total students : {result['total_students']}")
        print(f"Total countries : {result['total_countries']}")
        print("______________________________")
        print("Top 3 Countries:")

        for i, (country, count) in enumerate(result["top_3"], 1):
            print(f"{i}. {country} : {count}")

        print("______________________________")
        lambda_analysis(students)
        output_path = "output/result.json"
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(result, f, indent=4, ensure_ascii=False)
        print("______________________________")
        print("Result saved to output/result.json")
        print("______________________________")
    except FileNotFoundError:
        print("Error: File not found. Please check filename.")
    except Exception as e:
        print(f"General error: {e}")
main()