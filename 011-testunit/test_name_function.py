import unittest

from name_function import get_formatted_name

# formatted_name1 = get_formatted_name("zhang","jiang")
# print(formatted_name1)

class NamesTestCase(unittest.TestCase):
    """测试name_function.py"""
    """测试name_function.py """

    def test_first_last_name(self):

          """能够正确地处理像Janis Joplin这样的姓名吗?"""
          formatted_name = get_formatted_name('janis', 'joplin')
          self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):

          """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗?"""
          formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
          self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


unittest.main()

"""
assertEqual(a,b) 核实 a==b
assertNotEqual(a,b) 核实a!=b
assertTrue(x) 核实x为true
assertFalse(x) 核实x为false
assertIn(item,list) 核实item在list中
assertNotIn(item,list) 核实item不在list中

"""