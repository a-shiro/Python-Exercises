from project import StudentReportCard
from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.card = StudentReportCard('Johnny', 5)

    def test_constructor(self):
        self.assertEqual('Johnny', self.card.student_name)
        self.assertEqual(5, self.card.school_year)
        self.assertEqual({}, self.card.grades_by_subject)

    def test_student_name_getter(self):
        res = self.card.student_name
        self.assertEqual('Johnny', res)

    def test_student_name_setter_raises_error_if_name_is_empty_str(self):
        with self.assertRaises(ValueError) as cm:
            self.card.student_name = ''
        self.assertEqual('Student Name cannot be an empty string!', str(cm.exception))

    def test_student_name_setter_sets_name_correctly(self):
        self.card.student_name = 'Kiro'
        self.assertEqual('Kiro', self.card.student_name)

    def test_student_year_getter(self):
        res = self.card.school_year
        self.assertEqual(5, res)

    def test_school_year_setter_raises_error_if_given_year_that_is_not_between_1_and_12(self):
        with self.assertRaises(ValueError) as cm:
            self.card.school_year = -1
        self.assertEqual('School Year must be between 1 and 12!', str(cm.exception))

    def test_school_year_setter_sets_year_correctly_floor_case(self):
        self.card.school_year = 1
        self.assertEqual(1, self.card.school_year)

    def test_school_year_setter_sets_year_correctly_ceiling_case(self):
        self.card.school_year = 12
        self.assertEqual(12, self.card.school_year)

    def test_add_grade_when_the_subject_is_not_present_adds_the_subject_and_creates_a_list_with_the_first_grade(self):
        self.card.add_grade('Math', 4)
        self.assertEqual({'Math': [4]}, self.card.grades_by_subject)

    def test_add_grade_when_the_subject_is_present_adds_the_grade_to_the_existing_list(self):
        self.card.grades_by_subject = {'Math': [3]}
        self.card.add_grade('Math', 4)
        self.assertEqual({'Math': [3, 4]}, self.card.grades_by_subject)

    def test_get_average_grade_with_only_one_subject_returns_average_successfully(self):
        self.card.grades_by_subject = {'Math': [4]}

        result = self.card.average_grade_by_subject()
        self.assertEqual('Math: 4.00', result)

    def test_get_average_grade_with_two_subjects_returns_average_successfully(self):
        self.card.grades_by_subject = {'Math': [4], 'English': [6]}

        result = self.card.average_grade_by_subject()
        self.assertEqual('Math: 4.00\nEnglish: 6.00', result)

    def test_get_average_grade_with_more_than_two_subjects_returns_average_successfully(self):
        self.card.grades_by_subject = {'Math': [4, 4], 'English': [6, 6], 'Biology': [5]}

        result = self.card.average_grade_by_subject()
        self.assertEqual('Math: 4.00\nEnglish: 6.00\nBiology: 5.00', result)

    def test_average_grade_for_all_subjects_returns_average_successfully(self):
        self.card.grades_by_subject = {'Math': [4], 'English': [6]}

        result = self.card.average_grade_for_all_subjects()
        self.assertEqual('Average Grade: 5.00', result)

    def test_repr_return_correct_str(self):
        self.card.grades_by_subject = {'Math': [4], 'English': [6]}

        result = repr(self.card)
        self.assertEqual(f"Name: {self.card.student_name}\nYear: {self.card.school_year}\n----------\n{self.card.average_grade_by_subject()}\n----------\n{self.card.average_grade_for_all_subjects()}", result)


if __name__ == '__name__':
    main()
