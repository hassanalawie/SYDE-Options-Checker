from typing import List, TypedDict
class Course(TypedDict):
    discipline: str
    code: str

departmentCourseCodes = {
    "engineering":["SYDE", "ECE", "MSE", "MSCI", "MTE", "CHE", "AE", "BME", "CIVE", "ENVE", "GEOE", "ME", "NE", "SE"],
    "math":["CO", "CS", "STAT"]
}

requiredCourses = {
    "SYDE":[
        {"discipline": "SYDE", "code": "101"},
        {"discipline": "SYDE", "code": "101L"},
        {"discipline": "SYDE", "code": "111"},
        {"discipline": "SYDE", "code": "113"},
        {"discipline": "SYDE", "code": "121"},
        {"discipline": "SYDE", "code": "161"},
        {"discipline": "SYDE", "code": "181"},
        {"discipline": "SYDE", "code": "102"},
        {"discipline": "SYDE", "code": "112"},
        {"discipline": "SYDE", "code": "114"},
        {"discipline": "SYDE", "code": "162"},
        {"discipline": "SYDE", "code": "192"},
        {"discipline": "SYDE", "code": "192L"},
        {"discipline": "SYDE", "code": "223"},
        {"discipline": "SYDE", "code": "182"},
        {"discipline": "SYDE", "code": "201"},
        {"discipline": "SYDE", "code": "211"},
        {"discipline": "SYDE", "code": "261"},
        {"discipline": "SYDE", "code": "263"},
        {"discipline": "SYDE", "code": "283"},
        {"discipline": "SYDE", "code": "285"},
        {"discipline": "SYDE", "code": "202"},
        {"discipline": "SYDE", "code": "212"},
        {"discipline": "SYDE", "code": "252"},
        {"discipline": "SYDE", "code": "262"},
        {"discipline": "SYDE", "code": "286"},
        {"discipline": "SYDE", "code": "292"},
        {"discipline": "SYDE", "code": "292L"},
        {"discipline": "SYDE", "code": "301"},
        {"discipline": "SYDE", "code": "312"},
        {"discipline": "SYDE", "code": "351"},
        {"discipline": "SYDE", "code": "361"},
        {"discipline": "SYDE", "code": "381"},
        {"discipline": "SYDE", "code": "383"},
        {"discipline": "SYDE", "code": "300"},
        {"discipline": "SYDE", "code": "302"},
        {"discipline": "SYDE", "code": "352"},
        {"discipline": "SYDE", "code": "352L"},
        {"discipline": "SYDE", "code": "362"},
        {"discipline": "SYDE", "code": "411"},
        {"discipline": "SYDE", "code": "401"},
        {"discipline": "SYDE", "code": "461"},
        {"discipline": "SYDE", "code": "532"},
        {"discipline": "SYDE", "code": "402"},
        {"discipline": "SYDE", "code": "462"}
    ]
}

class AIOption:
    list_1: List[Course]
    list_2: List[Course]
    list_3: List[Course]
    def __init__(self):
        self.list_1 = [
            {"discipline": "HIST", "code": "212"},
            {"discipline": "MSE", "code": "442"},
            {"discipline": "MSCI", "code": "442"},
            {"discipline": "STV", "code": "205"},
            {"discipline": "STV", "code": "208"},
            {"discipline": "STV", "code": "210"},
        ]

        self.list_2 = [
            {"discipline": "CS", "code": "480"},
            {"discipline": "CS", "code": "485"},
            {"discipline": "CS", "code": "486"},
            {"discipline": "ECE", "code": "457"},
            {"discipline": "ECE", "code": "457"},
            {"discipline": "ECE", "code": "457"},
            {"discipline": "MSE", "code": "435"},
            {"discipline": "MSE", "code": "446"},
            {"discipline": "MSCI", "code": "435"},
            {"discipline": "MSCI", "code": "446"},
            {"discipline": "SYDE", "code": "522"},
        ]

        self.list_3 = self.list_2 + [
            {"discipline": "BIOL", "code": "487"},
            {"discipline": "CHE", "code": "521"},
            {"discipline": "CHE", "code": "522"},
            {"discipline": "CHE", "code": "524"},
            {"discipline": "CO", "code": "367"},
            {"discipline": "CO", "code": "456"},
            {"discipline": "CO", "code": "463"},
            {"discipline": "CO", "code": "466"},
            {"discipline": "CS", "code": "452"},
            {"discipline": "CS", "code": "479"},
            {"discipline": "CS", "code": "484"},
            {"discipline": "ECE", "code": "423"},
            {"discipline": "ECE", "code": "455"},
            {"discipline": "ECE", "code": "481"},
            {"discipline": "ECE", "code": "484"},
            {"discipline": "ECE", "code": "486"},
            {"discipline": "ECE", "code": "488"},
            {"discipline": "ECE", "code": "495"},
            {"discipline": "MSE", "code": "546"},
            {"discipline": "MTE", "code": "544"},
            {"discipline": "MTE", "code": "546"},
            {"discipline": "STAT", "code": "341"},
            {"discipline": "STAT", "code": "440"},
            {"discipline": "STAT", "code": "441"},
            {"discipline": "STAT", "code": "444"},
            {"discipline": "SYDE", "code": "552"},
            {"discipline": "SYDE", "code": "556"},
            {"discipline": "SYDE", "code": "572"},
        ]
    
    def check_requirements(self, courses: List[Course]) -> bool:
        def extract_matches(target_list: List[Course], input_courses: List[Course], required_courses:int) -> List[Course]:
            matches = [course for course in input_courses if course in target_list]
            for match in matches[:required_courses]:
                input_courses.remove(match)
            return matches
        def check_department_coverage(option_courses: List[Course], coursesTaken: List[Course]) -> bool:
            union: List[Course] = []
            for course in coursesTaken:
                if course in option_courses:
                    union.append(course)
            hasMath = False
            hasEng = False
            for course in union:
                if course["discipline"] in departmentCourseCodes["math"]:
                    hasMath = True
                if course["discipline"] in departmentCourseCodes["engineering"]:
                    hasEng = True
            return hasEng and hasMath

        def check_elective_coverage(option_courses: List[Course], coursesTaken: List[Course]) -> bool:
            union: List[Course] = []
            for course in coursesTaken:
                if course in option_courses:
                    union.append(course)
            nonElectiveCourses = []
            for course in union:
                if course not in requiredCourses["SYDE"]:
                    nonElectiveCourses.append(course)
            return len(nonElectiveCourses) >= 5
        
        remaining_courses = courses.copy()

        list_1_matches = extract_matches(self.list_1, remaining_courses, 1)
        meets_list_1 = len(list_1_matches) >= 1

        list_2_matches = extract_matches(self.list_2, remaining_courses, 2)
        print(remaining_courses)
        meets_list_2 = len(list_2_matches) >= 2

        list_3_matches = extract_matches(self.list_3, remaining_courses, 3)
        meets_list_3 = len(list_3_matches) >= 3

        option_courses = self.list_1 + self.list_2 + self.list_3

        meets_department_coverage = check_department_coverage(option_courses, courses)

        meets_elective_coverage = check_elective_coverage(option_courses, courses)
        if not (meets_list_1 and meets_list_2 and meets_list_3):
            print("List-based requirements not met.")
        if not meets_department_coverage:
            print("Department coverage requirements not met.")
        if not meets_elective_coverage:
            print("Elective course requirement not met.")
        return meets_list_1 and meets_list_2 and meets_list_3 and meets_department_coverage and meets_elective_coverage