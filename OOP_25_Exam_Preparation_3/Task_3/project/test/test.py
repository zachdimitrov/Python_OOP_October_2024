from unittest import TestCase, main

from project.social_media import SocialMedia


class SocialMediaTests(TestCase):
    def setUp(self):
        self.s = SocialMedia("Test", "Twitter", 10, "any")
    def test_init(self):
        self.assertEqual("Test")

if __name__ == "__main__":
    main()