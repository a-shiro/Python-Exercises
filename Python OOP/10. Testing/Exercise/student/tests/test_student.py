from unittest import TestCase, main
from project import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student('Jeffrey', {'Python': ['p1', 'p2']})

    def test_initialize_when_course_is_given(self):
        self.assertEqual({'Python': ['p1', 'p2']}, self.student.courses)

    def test_initialize_when_course_is_not_given(self):
        student = Student('Jimmy')
        self.assertEqual({}, student.courses)

    def test_enroll_the_student_in_the_specified_course_without_notes(self):
        result = self.student.enroll('Java', ['j1', 'j2'], 'N')

        self.assertTrue('Java' in self.student.courses)
        self.assertEqual([], self.student.courses['Java'])
        self.assertEqual('Course has been added.', result)

    def test_enroll_the_student_in_a_course_and_add_notes_if_the_add_notes_parameter_is_empty_str_or_Y(self):
        for idx, add_notes_param in enumerate(['', 'Y']):
            result = self.student.enroll(f'JavaScript{idx}', ['js1', 'js2'], add_notes_param)

            self.assertTrue(f'JavaScript{idx}' in self.student.courses)
            self.assertEqual(['js1', 'js2'], self.student.courses[f'JavaScript{idx}'])
            self.assertEqual('Course and course notes have been added.', result)

    def test_enroll_when_the_student_is_already_enrolled_in_that_course_it_adds_notes_to_it(self):
        new_notes = ['p3', 'p4']
        result = self.student.enroll('Python', new_notes)

        self.assertEqual(['p1', 'p2', 'p3', 'p4'], self.student.courses['Python'])
        self.assertEqual('Course already added. Notes have been updated.', result)

    def test_student_tries_to_add_note_to_a_course_that_he_is_not_enrolled_in_raises_error(self):
        with self.assertRaises(Exception) as cm:
            self.student.add_notes('C#', ['c#1', 'c#2'])
        self.assertEqual('Cannot add notes. Course not found.', str(cm.exception))

    def test_student_adds_note_to_a_course_successfully(self):
        result = self.student.add_notes('Python', 'p3')

        self.assertEqual(['p1', 'p2', 'p3'], self.student.courses['Python'])
        self.assertEqual('Notes have been updated', result)

    def test_student_tries_to_leave_course_that_he_is_not_enrolled_in_raises_error(self):
        with self.assertRaises(Exception) as cm:
            self.student.leave_course('C#')
        self.assertEqual('Cannot remove course. Course not found.', str(cm.exception))

    def test_student_leaves_course_successfully(self):
        result = self.student.leave_course('Python')

        self.assertEqual({}, self.student.courses)
        self.assertEqual('Course has been removed', result)


if __name__ == '__main__':
    main()