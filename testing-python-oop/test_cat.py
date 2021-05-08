from unittest import TestCase, main


class TestCat(TestCase):
    name = 'Bruss'
    fed = False
    sleepy = False
    size = 0

    def setUp(self):
        self.cat = Cat(self.name)

    def test_cat_size_increase_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.size + 1, self.cat.size)

    def test_cat_is_fed_after_eat(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_can_not_eat_after_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception):
            self.cat.eat()

    def test_cat_can_not_sleep_if_not_fed(self):
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()

# Tested code
# class Cat:
#
#   def __init__(self, name):
#     self.name = name
#     self.fed = False
#     self.sleepy = False
#     self.size = 0
#
#   def eat(self):
#     if self.fed:
#       raise Exception('Already fed.')
#
#     self.fed = True
#     self.sleepy = True
#     self.size += 1
#
#   def sleep(self):
#     if not self.fed:
#       raise Exception('Cannot sleep while hungry')
#
#     self.sleepy = False
