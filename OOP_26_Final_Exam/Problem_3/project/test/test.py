from project.senior_student import SeniorStudent
from unittest import TestCase, main


class SeniorStudentTests(TestCase):
    def setUp(self):
        self.s = SeniorStudent("1234", "Test", 5.2)

    def test_init(self):
        self.assertEqual("1234", self.s.student_id)
        self.assertEqual("Test", self.s.name)
        self.assertEqual(5.2, self.s.student_gpa)
        self.assertEqual(set(), self.s.colleges)

    def test_id_bad_length_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.s.student_id = "123"
        self.assertEqual("Student ID must be at least 4 digits long!", str(ex.exception))

    def test_id_setter(self):
        self.assertEqual("1234", self.s.student_id)
        self.s.student_id = "6789"
        self.assertEqual("6789", self.s.student_id)

    def test_name_empty_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.s.name = "   "
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

    def test_name_null_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.s.name = ""
        self.assertEqual("Student name cannot be null or empty!", str(ex.exception))

    def test_name_setter(self):
        self.assertEqual("Test", self.s.name)
        self.s.name = "Gosho"
        self.assertEqual("Gosho", self.s.name)

    def test_gpa_less_than_one_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.s.student_gpa = 0.5
        self.assertEqual("Student GPA must be more than 1.0!", str(ex.exception))

    def test_gpa_setter(self):
        self.assertEqual(5.2, self.s.student_gpa)
        self.s.student_gpa = 1.5
        self.assertEqual(1.5, self.s.student_gpa)

    def test_apply_to_college_not_enough_gpa(self):
        self.s.student_gpa = 1.5
        gpa_required = 4
        result = self.s.apply_to_college(gpa_required, "TestCollege")
        self.assertEqual("Application failed!", result)

    def test_apply_to_college_enough_gpa(self):
        self.assertEqual(5.2, self.s.student_gpa)
        gpa_required = 4
        result = self.s.apply_to_college(gpa_required, "TestCollege")
        self.assertEqual("Test successfully applied to TestCollege.", result)
        self.assertEqual({"TESTCOLLEGE"}, self.s.colleges)

    def test_update_gpa_too_low(self):
        self.assertEqual(5.2, self.s.student_gpa)
        result = self.s.update_gpa(0.5)
        self.assertEqual("The GPA has not been changed!", result)
        self.assertEqual(5.2, self.s.student_gpa)

    def test_update_gpa(self):
        self.assertEqual(5.2, self.s.student_gpa)
        result = self.s.update_gpa(1.5)
        self.assertEqual("Student GPA was successfully updated.", result)
        self.assertEqual(1.5, self.s.student_gpa)

    def test_eq(self):
        other = SeniorStudent("5678", "Other", 5.2)
        result = self.s == other
        self.assertEqual(True, result)
        other.student_gpa = 4
        result = self.s == other
        self.assertEqual(False, result)


if __name__ == "__main__":
    main()
