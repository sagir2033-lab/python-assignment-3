import os
import csv
import json
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    def check_file(self):
        print("Checking file...")
        if os.path.exists(self.filename):
            print(f"File found: {self.filename}")
            return True
        else:
            print(f"Error: {self.filename} not found")
            return False
    def create_output_folder(self, folder="output"):
        print("Checking output folder...")

        if not os.path.exists(folder):
            os.makedirs(folder)
            print(f"Output folder created: {folder}/")
        else:
            print(f"Output folder already exists: {folder}/")
            
class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.students = []
    def load(self):
        print("Loading data...")
        try:
            with open(self.filename, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                self.students = list(reader)
            print(f"Data loaded successfully: {len(self.students)} students")
            return self.students
        except FileNotFoundError:
            print("Error: file not found")
            return []
    def preview(self, n=5):
        print("First 5 rows:")
        print("______________________________")
        for s in self.students[:n]:
            print(f"{s['student_id']} | {s['age']} | {s['gender']} | {s['country']} | GPA: {s['GPA']}")

        print("______________________________")

class DataAnalyser:
    def __init__(self, students):
        self.students = students
        self.result = {}
    def analyse(self):
        country_counts = {}
        for s in self.students:
            country = s["country"]
            if country in country_counts:
                country_counts[country] += 1
            else:
                country_counts[country] = 1
        top_3 = sorted(country_counts.items(), key=lambda x: x[1], reverse=True)[:3]
        self.result = {
            "total_students": len(self.students),
            "total_countries": len(country_counts),
            "top_3": top_3,
            "all_countries": country_counts
        }
        return self.result
    def print_results(self):
        print("_____________________________")
        print("Country Analysis")
        print("_____________________________")
        print(f"Total countries : {self.result['total_countries']}")
        print("Top 3 Countries:")
        for i, (country, count) in enumerate(self.result["top_3"], 1):
            print(f"{i}. {country} : {count}")
        print("______________________________")

class ResultSaver:
    def __init__(self, result, output_path):
        self.result = result
        self.output_path = output_path
    def save_json(self):
        try:
            with open(self.output_path, "w", encoding="utf-8") as f:
                json.dump(self.result, f, indent=4)
            print("Result saved to output/result.json")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    fm = FileManager("C:/Users/Самир/Desktop/Python/students.csv")
    if not fm.check_file():
        print("Stopping program.")
        exit()
    fm.create_output_folder()
    dl = DataLoader("C:/Users/Самир/Desktop/Python/students.csv")
    dl.load()
    dl.preview()
    analyser = DataAnalyser(dl.students)
    analyser.analyse()
    analyser.print_results()
    saver = ResultSaver(analyser.result, "output/result.json")
    saver.save_json()

    print(" ")
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
print(" ")
print(" ")
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
print(" ")