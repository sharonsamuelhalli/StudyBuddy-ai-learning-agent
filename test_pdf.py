from src.syllabus_analyzer import SyllabusAnalyzer

analyzer = SyllabusAnalyzer()

syllabus_text = """
Introduction to Algorithms
Topics include asymptotic analysis, divide and conquer,
greedy algorithms, and dynamic programming.
"""

result = analyzer.analyze_syllabus(syllabus_text)

print(result)