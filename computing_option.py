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
class ComputingOption:
    list_1: List[Course]
    list_2: List[Course]
    def MSE_MSCI_fix(self, list: List[Course]) -> List[Course]:
        newCourses:List[Course] = []
        for course in list:
            if course['discipline'] == "MSE":
                newCourses.append({"discipline":"MSCI", "code":course["code"]})
            elif course["discipline"] == "MSCI":
                newCourses.append({"discipline":"MSE", "code":course["code"]})
        return list + newCourses
    def __init__(self):
        self.list_1 = [
            {"discipline": "AE", "code": "121"},
            {"discipline": "BME", "code": "121"},
            {"discipline": "CHE", "code": "120"},
            {"discipline": "CIVE", "code": "121"},
            {"discipline": "CS", "code": "115"},
            {"discipline": "CS", "code": "116"},
            {"discipline": "CS", "code": "135"},
            {"discipline": "CS", "code": "137"},
            {"discipline": "CS", "code": "145"},
            {"discipline": "ECE", "code": "150"},
            {"discipline": "ENVE", "code": "121"},
            {"discipline": "GEOE", "code": "121"},
            {"discipline": "ME", "code": "101"},
            {"discipline": "MSE", "code": "121"},
            {"discipline": "MTE", "code": "121"},
            {"discipline": "NE", "code": "111"},
            {"discipline": "SYDE", "code": "121"},
        ]

        self.list_2 = [
            {"discipline": "BME", "code": "122"},
            {"discipline": "CS", "code": "136"},
            {"discipline": "CS", "code": "138"},
            {"discipline": "CS", "code": "146"},
            {"discipline": "CS", "code": "231"},
            {"discipline": "CS", "code": "234"},
            {"discipline": "ECE", "code": "250"},
            {"discipline": "ECE", "code": "406"},
            {"discipline": "MSE", "code": "240"},
            {"discipline": "MTE", "code": "140"},
            {"discipline": "SYDE", "code": "223"},
        ]
        
        self.list_3 = [
            {"discipline": "BIOL", "code": "487"},
            {"discipline": "BME", "code": "393"},
            {"discipline": "BME", "code": "411"},
            {"discipline": "CHE", "code": "322"},
            {"discipline": "CIVE", "code": "422"},
            {"discipline": "EARTH", "code": "456"},
            {"discipline": "ENVE", "code": "225"},
            {"discipline": "NE", "code": "336"},
            {"discipline": "CS", "code": "230"},
            {"discipline": "CS", "code": "245"},
            {"discipline": "CS", "code": "338"},
            {"discipline": "CS", "code": "445"},
            {"discipline": "CS", "code": "446"},
            {"discipline": "CS", "code": "447"},
            {"discipline": "ECE", "code": "124"},
            {"discipline": "ECE", "code": "204"},
            {"discipline": "ECE", "code": "208"},
            {"discipline": "ECE", "code": "222"},
            {"discipline": "ECE", "code": "224"},
            {"discipline": "ECE", "code": "252"},
            {"discipline": "ECE", "code": "320"},
            {"discipline": "ECE", "code": "327"},
            {"discipline": "ECE", "code": "350"},
            {"discipline": "ECE", "code": "351"},
            {"discipline": "ECE", "code": "356"},
            {"discipline": "ECE", "code": "358"},
            {"discipline": "ECE", "code": "409"},
            {"discipline": "ECE", "code": "417"},
            {"discipline": "ECE", "code": "423"},
            {"discipline": "ECE", "code": "451"},
            {"discipline": "ECE", "code": "452"},
            {"discipline": "ECE", "code": "453"},
            {"discipline": "ECE", "code": "454"},
            {"discipline": "ECE", "code": "455"},
            {"discipline": "ECE", "code": "457A"},
            {"discipline": "ECE", "code": "457B"},
            {"discipline": "ECE", "code": "457C"},
            {"discipline": "ECE", "code": "458"},
            {"discipline": "ECE", "code": "459"},
            {"discipline": "ME", "code": "262"},
            {"discipline": "ME", "code": "559"},
            {"discipline": "ME", "code": "566"},
            {"discipline": "MSE", "code": "245"},
            {"discipline": "MSE", "code": "342"},
            {"discipline": "MSE", "code": "343"},
            {"discipline": "MSE", "code": "436"},
            {"discipline": "MSE", "code": "446"},
            {"discipline": "MSE", "code": "541"},
            {"discipline": "MSE", "code": "543"},
            {"discipline": "MSE", "code": "546"},
            {"discipline": "MTE", "code": "204"},
            {"discipline": "MTE", "code": "241"},
            {"discipline": "MTE", "code": "262"},
            {"discipline": "MTE", "code": "325"},
            {"discipline": "MTE", "code": "544"},
            {"discipline": "MTE", "code": "546"},
            {"discipline": "SE", "code": "212"},
            {"discipline": "SE", "code": "350"},
            {"discipline": "SE", "code": "463"},
            {"discipline": "SE", "code": "464"},
            {"discipline": "SE", "code": "465"},
            {"discipline": "SYDE", "code": "192"},
            {"discipline": "SYDE", "code": "411"},
            {"discipline": "SYDE", "code": "522"},
            {"discipline": "SYDE", "code": "542"},
            {"discipline": "SYDE", "code": "543"},
            {"discipline": "SYDE", "code": "548"},
            {"discipline": "SYDE", "code": "552"},
            {"discipline": "SYDE", "code": "556"},
            {"discipline": "SYDE", "code": "572"},
            {"discipline": "SYDE", "code": "575"},
        ]
        self.list_1 = self.MSE_MSCI_fix(self.list_1)
        self.list_2 = self.MSE_MSCI_fix(self.list_2)
        self.list_3 = self.MSE_MSCI_fix(self.list_3)
    def check_requirements(self, courses: List[Course]) -> bool:
        def extract_matches(target_list: List[Course], input_courses: List[Course], required_courses: int) -> List[Course]:
            matches = [course for course in input_courses if course in target_list]
            for match in matches[:required_courses]:
                input_courses.remove(match)
            return matches
        def check_elective_coverage(option_courses: List[Course], coursesTaken: List[Course]) -> bool:
            union: List[Course] = []
            for course in coursesTaken:
                if course in option_courses:
                    union.append(course)
            nonElectiveCourses = []
            for course in union:
                if course not in requiredCourses["SYDE"]:
                    nonElectiveCourses.append(course)
            return len(nonElectiveCourses) >= 3
        remaining_courses = courses.copy()
        list_1_matches = extract_matches(self.list_1, remaining_courses, 1)
        meets_list_1 = len(list_1_matches) >= 1
        list_2_matches = extract_matches(self.list_2, remaining_courses, 1)
        meets_list_2 = len(list_2_matches) >= 1
        list_3_matches = extract_matches(self.list_3, remaining_courses, 2)
        meets_list_3 = len(list_3_matches) >= 2
        additional_matches = extract_matches(self.list_1 + self.list_2 + self.list_3, remaining_courses, 2)
        meets_additional_courses = len(additional_matches) >= 2
        option_courses = self.list_1 + self.list_2 + self.list_3
        meets_elective_requirements = check_elective_coverage(option_courses, courses)
        if not (meets_list_1 and meets_list_2 and meets_list_3 and meets_additional_courses):
            print("Overall requirements not satisfied.")
        elif not meets_elective_requirements:
            print("Elective requirements not satisfied.")
        return meets_list_1 and meets_list_2 and meets_list_3 and meets_additional_courses and meets_elective_requirements