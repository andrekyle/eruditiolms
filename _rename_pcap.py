from app import app, db, Lesson, Quiz
RENAMES = {
    4:  ('Lesson 3: Modules and Packages',
         'Lesson 3 Quiz \u2014 Modules and Packages'),
    6:  ('Lesson 4: Exceptions',
         'Lesson 4 Quiz \u2014 Exceptions'),
    8:  ('Lesson 5: Strings',
         'Lesson 5 Quiz \u2014 Strings'),
    10: ('Lesson 6: Object-Oriented Programming \u2014 Classes, Inheritance, Polymorphism',
         'Lesson 6 Quiz \u2014 OOP: Classes, Inheritance, Polymorphism'),
    12: ('Lesson 7: OOP \u2014 Special Methods, Introspection, and Exceptions as Classes',
         'Lesson 7 Quiz \u2014 OOP: Special Methods, Introspection, and Exceptions as Classes'),
    14: ('Lesson 8: Miscellaneous \u2014 Generators, Closures, Files, and the Standard Library',
         'Lesson 8 Quiz \u2014 Generators, Closures, Files, and the Standard Library'),
}
with app.app_context():
    for order, (new_lt, new_qt) in RENAMES.items():
        L = Lesson.query.filter_by(course_id=1, order=order).first()
        old = L.title
        L.title = new_lt
        print('L%d: %r -> %r' % (order, old, new_lt))
        EX = Lesson.query.filter_by(course_id=1, order=order+1).first()
        if EX and EX.quiz_id:
            Q = db.session.get(Quiz, EX.quiz_id)
            oldq = Q.title
            Q.title = new_qt
            EX.title = new_qt
            print('  quiz#%d: %r -> %r' % (Q.id, oldq, new_qt))
    db.session.commit()
    print('done')
