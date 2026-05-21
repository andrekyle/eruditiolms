Author outputs land in this folder. Each agent writes one file:
  l1_basics.py, l2_data_types.py, l3_operators.py, l4_arrays.py,
  l5_loops.py, l6_methods.py, l7_inheritance.py, l8_exceptions.py,
  l9_api_classes.py, final_exam.py

Each file MUST be valid Python and export:
  LESSON_HTML : str          (rich HTML lesson body; not required for final_exam.py)
  QUESTIONS   : list[tuple]  (quiz: 8 items; final_exam: 25 items)

Each QUESTIONS item is a 3-tuple:
  (question_html: str, options: list[(option_html, is_correct_bool) x 4], feedback: str)

Exactly one option must be is_correct=True. Use <code>, <pre>, <strong>
for Java syntax and emphasis. No external images.
