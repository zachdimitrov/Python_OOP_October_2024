from unittest import TestCase, main

from project.social_media import SocialMedia


class SocialMediaTests(TestCase):
    def setUp(self):
        self.s = SocialMedia("Test", "Twitter", 10, "any")

    def test_init(self):
        self.assertEqual("Test", self.s._username)
        self.assertEqual("Twitter", self.s.platform)
        self.assertEqual(10, self.s.followers)
        self.assertEqual("any", self.s._content_type)
        self.assertEqual([], self.s._posts)

    def test_platform_setter(self):
        self.assertEqual("Twitter", self.s.platform)
        self.s.platform = "Instagram"
        self.assertEqual("Instagram", self.s.platform)

    def test_wrong_platform_raises(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as ex:
            self.s.platform = "Til-Tok"
        self.assertEqual(f"Platform should be one of {allowed_platforms}", str(ex.exception))

    def test_followers_setter(self):
        self.assertEqual(10, self.s.followers)
        self.s.followers = 15
        self.assertEqual(15, self.s.followers)

    def test_negative_followers_raises(self):
        self.assertEqual(10, self.s.followers)
        with self.assertRaises(ValueError) as ex:
            self.s.followers = -1
        self.assertEqual("Followers cannot be negative.", str(ex.exception))

    def test_create_post_returns_message(self):
        result = self.s.create_post("Test content")
        expected = "New any post created by Test on Twitter."
        self.assertEqual(expected, result)
        self.assertEqual(1, len(self.s._posts))
        self.assertEqual([{'content': "Test content", 'likes': 0, 'comments': []}], self.s._posts)

    def test_like_post_not_found(self):
        self.assertEqual([], self.s._posts)
        result = self.s.like_post(0)
        self.assertEqual("Invalid post index.", result)

    def test_like_post_reached_limit(self):
        self.s.create_post("Test content")
        self.assertEqual([{'content': "Test content", 'likes': 0, 'comments': []}], self.s._posts)
        for i in range(10):
            self.s.like_post(0)
        self.assertEqual(10, self.s._posts[0]["likes"])
        result = self.s.like_post(0)
        self.assertEqual("Post has reached the maximum number of likes.", result)
        self.assertEqual(10, self.s._posts[0]["likes"])

    def test_like_post(self):
        self.s.create_post("Test content")
        self.assertEqual([{'content': "Test content", 'likes': 0, 'comments': []}], self.s._posts)
        self.assertEqual(0, self.s._posts[0]["likes"])
        result = self.s.like_post(0)
        self.assertEqual("Post liked by Test.", result)
        self.assertEqual(1, self.s._posts[0]["likes"])

    def test_post_comment_short(self):
        self.s.create_post("Test content")
        self.assertEqual([{'content': "Test content", 'likes': 0, 'comments': []}], self.s._posts)
        result = self.s.comment_on_post(0, "hi")
        self.assertEqual("Comment should be more than 10 characters.", result)

    def test_post_comment_returns(self):
        self.s.create_post("Test content")
        self.assertEqual([{'content': "Test content", 'likes': 0, 'comments': []}], self.s._posts)
        result = self.s.comment_on_post(0, "Very nice post!")
        self.assertEqual("Comment added by Test on the post.", result)
        self.assertEqual({'user': "Test", 'comment': "Very nice post!"}, self.s._posts[0]["comments"][0])


if __name__ == "__main__":
    main()
