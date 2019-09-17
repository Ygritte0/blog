#-*-coding:utf-8-*-
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """针对AnonymousSurvey 类的测试"""

    def setUp(self):
        """创建一个调查对象和一组答案，供使用的测试的方法使用"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English','Spanish','Mandarin']

    def test_store_single_response(self):
        """测试单个答案会被妥善的存储"""
        # question = "What language did you first learn to speak?"
        self.my_survey.store_responses(self.responses[0])
        # my_survey.store_responses('English')
        self.assertIn('English', self.my_survey.responses)

    def test_store_three_responses(self):
        """测试三个答案会被妥善的存储"""
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        responses = ['English','Spanish','Mandarin']
        for response in responses:
            my_survey.store_responses(response)

        for response in responses:
            self.assertIn(response,my_survey.responses)