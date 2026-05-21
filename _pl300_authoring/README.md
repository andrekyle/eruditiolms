# PL-300 authoring workspace

Each topic lesson lives in its own `lN_xxx.py` file exposing:

```python
LESSON_HTML = """<h2>...</h2>..."""  # rich HTML, 4000-12000 chars

QUESTIONS = [
    (question_html, [(option_html, is_correct_bool)*4], feedback_str),
    # ... 8 items
]
```

`final_exam.py` exposes only `QUESTIONS` of length 25.
`about.py` exposes `ABOUT_HTML`.
`_spec.py` exposes `LESSONS` (list of dicts).

Strict escaping rules: only triple-quoted Python strings, single-quotes for HTML
attributes, HTML-escape `<>&` inside `<pre><code>` blocks, no `\u` escapes
anywhere (use `&#x...;` or literal `\\u` if needed).
