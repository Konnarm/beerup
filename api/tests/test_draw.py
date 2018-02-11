import unittest
import random

class DrawTest(unittest.TestCase):
    def setUp(self):
        self.draw = Draw()

    def test_draw_method_returns_user(self):
        user_list = random.sample(xrange(100), 10)
        returned_user = self.draw(user_list)

if __name__ =='__main__':
    unittest.main()
