from django.test import TestCase

class ExampleTestCase(TestCase):
    def test_one_equal_another(self):
        self.assertEqual(1,1)

    def test_not_equal(self):
        self.assertNotEqual(2,1)
    
    def test_true(self):
        self.assertTrue('a' in 'hello')
