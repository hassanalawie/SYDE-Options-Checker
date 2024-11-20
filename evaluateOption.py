from typing import List, Dict, TypedDict
import re

from ai_option import AIOption
from computing_option import ComputingOption


class Course(TypedDict):
    discipline: str
    code: str


def parse_courses(text: str) -> List[Course]:

    lines = text.split("\n")
    courses: List[Course] = []
    term = None

    course_pattern = re.compile(r"^(.*?)\t([A-Z]+\s\d+[A-Z]*)\t.*$")

    for line in lines:
        if line.startswith("Term"):
            term = line.strip()
        match = course_pattern.match(line)
        if match:
            course_name = match.group(1).strip()
            course_code = match.group(2).strip()
            discipline, code = course_code.split()
            courses.append({
                "discipline": discipline,
                "code": code
            })

    return courses

def main():
    print("Paste your copied course data below and press Enter twice when done:")
    user_input = []
    while True:
        line = input()
        if line.strip() == "":
            break
        user_input.append(line)
    input_text = "\n".join(user_input)

    parsed_courses = parse_courses(input_text)
    ai_option = AIOption()
    option = ai_option.check_requirements(parsed_courses)
    print("AI Option" if option else "No AI Option")

    computing_option = ComputingOption()
    option = computing_option.check_requirements(parsed_courses)
    print("Computing Option" if option else "No Computing Option")


main()