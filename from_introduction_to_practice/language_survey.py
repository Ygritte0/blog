#-*-coding:utf-8-*-
from survey import AnonymousSurvey

# 定义一个问题， 并创建一个表示调查的AnonymousSurvey对象
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' to quit.")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_responses(response)

# 显示调查结果
print("Thank you to everyone who participate in the survey!")
my_survey.show_results()