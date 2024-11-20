from flask import Blueprint, render_template, request, jsonify
from ai_option import AIOption
from computing_option import ComputingOption
from typing import List, Dict
import re

Course = Dict[str, str]

def parse_courses(text: str) -> List[Course]:
    lines = text.split("\n")
    courses: List[Course] = []
    course_pattern = re.compile(r"^(.*?)\t([A-Z]+\s\d+[A-Z]*)\t.*$")

    for line in lines:
        match = course_pattern.match(line)
        if match:
            course_code = match.group(2).strip()
            discipline, code = course_code.split()
            courses.append({
                "discipline": discipline,
                "code": code
            })

    return courses
# Create a Blueprint for routes
bp = Blueprint('routes', __name__)

# Initialize instances
ai_option = AIOption()
computing_option = ComputingOption()

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/check-ai-requirements', methods=['POST'])
def check_ai_requirements():
    try:
        data = request.json
        text = data.get('text', '')
        if not text:
            return jsonify({"error": "Course data is required"}), 400

        # Parse courses
        courses = parse_courses(text)

        # Check AI Option requirements
        result = ai_option.check_requirements(courses)
        return jsonify({"meets_requirements": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@bp.route('/check-computing-requirements', methods=['POST'])
def check_computing_requirements():
    try:
        data = request.json
        text = data.get('text', '')
        if not text:
            return jsonify({"error": "Course data is required"}), 400

        # Parse courses
        courses = parse_courses(text)

        # Check Computing Option requirements
        result = computing_option.check_requirements(courses)
        return jsonify({"meets_requirements": result}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500