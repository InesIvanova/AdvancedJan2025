from project3.gallery import Gallery
from unittest import TestCase, main


class TestGallery(TestCase):
    def setUp(self):
        self.g = Gallery("test", "Sofia", 120.5, False)

    def test_init_with_open_o_public(self):
        self.assertEqual("test", self.g.gallery_name)
        self.assertEqual("Sofia", self.g.city)
        self.assertEqual(120.5, self.g.area_sq_m)
        self.assertFalse(self.g.open_to_public)
        self.assertEqual({}, self.g.exhibitions)

    def test_init_withou_open_to_public(self):
        gallery = Gallery("test", "Sofia", 120.5)

        self.assertEqual("test", gallery.gallery_name)
        self.assertEqual("Sofia", gallery.city)
        self.assertEqual(120.5, gallery.area_sq_m)
        self.assertTrue(gallery.open_to_public)
        self.assertEqual({}, gallery.exhibitions)

    def test_incorrect_name_raises(self):
        self.assertEqual("test", self.g.gallery_name)
        with self.assertRaises(ValueError) as ex:
            self.g.gallery_name = "test 4"

        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))
        self.assertEqual("test", self.g.gallery_name)

    def test_gallery_name_stripped(self):
        pass

    def test_incorrect_city_raises(self):
        self.assertEqual("Sofia", self.g.city)
        with self.assertRaises(ValueError) as ex:
            self.g.city = ""
        self.assertEqual("City name must start with a letter!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.g.city = "1Pernik"

        self.assertEqual("City name must start with a letter!", str(ex.exception))
        self.assertEqual("Sofia", self.g.city)

    def test_incorrect_sq_m_raises(self):
        self.assertEqual(120.5, self.g.area_sq_m)
        with self.assertRaises(ValueError) as ex:
            self.g.area_sq_m = 0
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

        with self.assertRaises(ValueError) as ex:
            self.g.area_sq_m = -1

        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))
        self.assertEqual(120.5, self.g.area_sq_m)

    def test_add_exhibition_already_exists_raises(self):
        self.g.exhibitions["a"] = 2025
        result = self.g.add_exhibition("a", 2014)
        self.assertEqual('Exhibition "a" already exists.', result)
        self.assertEqual(2025,  self.g.exhibitions["a"])

    def test_add_new_exhibition(self):
        self.g.exhibitions["a"] = 2025
        result = self.g.add_exhibition("b", 2014)
        self.assertEqual('Exhibition "b" added for the year 2014.', result)
        self.assertEqual(2, len(self.g.exhibitions))

    def test_remove_exhibition_does_not_exist_raises(self):
        self.assertEqual(0, len(self.g.exhibitions))

        result = self.g.remove_exhibition("a")
        self.assertEqual('Exhibition "a" not found.', result)

    def test_remove_exhibition(self):
        self.g.exhibitions["a"] = 2025
        self.g.exhibitions["b"] = 2014

        result = self.g.remove_exhibition("b")
        self.assertEqual('Exhibition "b" removed.', result)
        self.assertEqual(1, len(self.g.exhibitions))
        self.assertEqual(2025, self.g.exhibitions['a'])

    def test_list_exhibitions_not_open_to_public(self):
        self.assertFalse(self.g.open_to_public)
        result = self.g.list_exhibitions()
        self.assertEqual("Gallery test is currently closed for public! Check for updates later on.", result)

    def test_list_exhibitions_open_to_public(self):
        self.g.open_to_public = True
        self.g.exhibitions["a"] =2025
        self.g.exhibitions["b"] = 2014
        self.assertTrue(self.g.open_to_public)

        result = self.g.list_exhibitions()
        expected_result = "a: 2025\nb: 2014"
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()