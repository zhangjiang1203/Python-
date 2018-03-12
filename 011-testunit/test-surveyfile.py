from surveyTest import AnonymousSurvey

question = "what language did you first learn to speak"
my_survey = AnonymousSurvey(question)
my_survey.show_question()

print("Enter 'q' to quit at any time")
while True:
    response = input("language:")
    if response == 'q':
        break;
    my_survey.store_response(response)

print("Thank you to everyont who participated in the survey!")
my_survey.show_results()