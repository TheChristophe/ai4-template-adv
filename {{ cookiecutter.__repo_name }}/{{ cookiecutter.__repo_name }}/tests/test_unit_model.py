# -*- coding: utf-8 -*-
import unittest
import {{ cookiecutter.__repo_name }}.models.api as api

class TestModelMethods(unittest.TestCase):

    def setUp(self):
        self.meta = deep_api.get_metadata()

    def test_model_metadata_type(self):
        """
        Test that get_metadata() returns dict
        """
        self.assertTrue(type(self.meta) is dict)

    def test_model_metadata_values(self):
        """
        Test that get_metadata() returns right values (subset)
        """
        self.assertEqual(self.meta['name'].lower().replace('-','_'),
                        '{{ cookiecutter.__repo_name }}'.lower().replace('-','_'))
        self.assertEqual(self.meta['author'].lower(),
                         '{{ cookiecutter.author_name }}'.lower())
        self.assertEqual(self.meta['license'].lower(),
                         '{{ cookiecutter.open_source_license }}'.lower())


if __name__ == '__main__':
    unittest.main()
