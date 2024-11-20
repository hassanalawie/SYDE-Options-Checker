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
    
    def check_requirements(self, courses: List[Course]) -> dict:
        def extract_matches(target_list: List[Course], input_courses: List[Course], required_courses: int) -> List[Course]:
            matches = [course for course in input_courses if course in target_list]
            for match in matches[:required_courses]:
                input_courses.remove(match)
            return matches

        def check_department_coverage(option_courses: List[Course], coursesTaken: List[Course]) -> bool:
            union: List[Course] = []
            for course in coursesTaken:
                if course in option_courses:
                    union.append(course)
            hasMath = any(course["discipline"] in departmentCourseCodes["math"] for course in union)
            hasEng = any(course["discipline"] in departmentCourseCodes["engineering"] for course in union)
            return hasEng and hasMath

        def check_elective_coverage(option_courses: List[Course], coursesTaken: List[Course]) -> bool:
            union: List[Course] = []
            for course in coursesTaken:
                if course in option_courses:
                    union.append(course)
            nonElectiveCourses = [course for course in union if course not in requiredCourses["SYDE"]]
            return len(nonElectiveCourses) >= 5

        # Initialize results
        results = {
            "meets_list_1": False,
            "meets_list_2": False,
            "meets_list_3": False,
            "meets_department_coverage": False,
            "meets_elective_coverage": False,
            "missing_requirements": []
        }

        remaining_courses = courses.copy()

        # Check List 1 requirement
        list_1_matches = extract_matches(self.list_1, remaining_courses, 1)
        results["meets_list_1"] = len(list_1_matches) >= 1
        if not results["meets_list_1"]:
            results["missing_requirements"].append("List 1 requirement not met (at least 1 course).")

        # Check List 2 requirement
        list_2_matches = extract_matches(self.list_2, remaining_courses, 2)
        results["meets_list_2"] = len(list_2_matches) >= 2
        if not results["meets_list_2"]:
            results["missing_requirements"].append("List 2 requirement not met (at least 2 courses).")

        # Check List 3 requirement
        list_3_matches = extract_matches(self.list_3, remaining_courses, 3)
        results["meets_list_3"] = len(list_3_matches) >= 3
        if not results["meets_list_3"]:
            results["missing_requirements"].append("List 3 requirement not met (at least 3 courses).")

        # Check department coverage
        option_courses = self.list_1 + self.list_2 + self.list_3
        results["meets_department_coverage"] = check_department_coverage(option_courses, courses)
        if not results["meets_department_coverage"]:
            results["missing_requirements"].append("Department coverage requirement not met (at least one Math and one Engineering course).")

        # Check elective coverage
        results["meets_elective_coverage"] = check_elective_coverage(option_courses, courses)
        if not results["meets_elective_coverage"]:
            results["missing_requirements"].append("Elective requirement not met (at least 5 elective courses).")

        # Overall result
        results["meets_requirements"] = all([
            results["meets_list_1"],
            results["meets_list_2"],
            results["meets_list_3"],
            results["meets_department_coverage"],
            results["meets_elective_coverage"]
        ])

        return results
