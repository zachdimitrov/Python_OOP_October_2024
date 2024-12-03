from unittest import TestCase, main
from project.student import Student


class StudentTests(TestCase):
    def setUp(self):
        self.s = Student("Test")

    def test_init(self):
        self.assertEqual(self.s.name, "Test")
        self.assertEqual(self.s.courses, {})

    def test_enroll_course_added(self):
        self.s.courses = {"test": ["1", "2", "3"]}
        notes = ["4", "5"]
        result = self.s.enroll("test", notes)
        self.assertEqual(self.s.courses, {"test": ["1", "2", "3", "4", "5"]})
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_enroll_no_course_notes(self):
        self.assertEqual(self.s.courses, {})
        result = self.s.enroll("test", ["1", "2", "3"])
        self.assertEqual(self.s.courses, {"test": ["1", "2", "3"]})
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_no_course_note_y(self):
        self.assertEqual(self.s.courses, {})
        result = self.s.enroll("test", ["1", "2", "3"], "Y")
        self.assertEqual(self.s.courses, {"test": ["1", "2", "3"]})
        self.assertEqual(result, "Course and course notes have been added.")

    def test_enroll_no_course_no_notes(self):
        self.assertEqual(self.s.courses, {})
        result = self.s.enroll("test", ["1", "2", "3"], "N")
        self.assertEqual(self.s.courses, {"test": []})
        self.assertEqual(result, "Course has been added.")

    def test_add_notes_no_course_raises(self):
        self.assertEqual(self.s.courses, {})
        with self.assertRaises(Exception) as ex:
            result = self.s.add_notes("test", ["1", "2", "3"])
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")
        self.assertEqual(self.s.courses, {})

    def test_add_notes(self):
        self.s.courses = {"test": ["1", "2", "3"]}
        result = self.s.add_notes("test", "4")
        self.assertEqual(self.s.courses, {"test": ["1", "2", "3", "4"]})
        self.assertEqual(result, "Notes have been updated")

    def test_leave_course_not_found_raises(self):
        self.assertEqual(self.s.courses, {})
        with self.assertRaises(Exception) as ex:
            result = self.s.leave_course("test")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")
        self.assertEqual(self.s.courses, {})

    def test_leave_course(self):
        self.s.courses = {"test": ["1", "2", "3"]}
        result = self.s.leave_course("test")
        self.assertEqual(self.s.courses, {})
        self.assertEqual(result, "Course has been removed")


if __name__ == "__main__":
    main()
