import unittest
from surveyTest import AnonymousSurvey

class TestSurvey(unittest.TestCase):

    def setUp(self):
        #创建测试中的全局的一个对象供所有测试方法使用
        question = "what language did you fitst learn to speak"
        self.my_survey = AnonymousSurvey(question)


    def test_store_single_response(self):
        """测试单个答案被存储"""
        self.my_survey.store_response("English")
        self.assertIn("English1",self.my_survey.store_response)

    def test_store_response(self):
        self.my_survey.store_response(["wanger","lisi"])
        self.assertIn("lisi",self.my_survey.store_response)

unittest.main()