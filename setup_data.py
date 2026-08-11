from django.contrib.auth.models import User
from onlinecourse.models import Course, Question, Choice
u = User.objects.get(username='admin')
u.set_password('admin')
u.save()

# Let's also add a dummy course, question, and choices to test the exam
course = Course.objects.create(name='Test Course', description='Test Description')
q1 = Question.objects.create(course=course, question_text='What is Django?', grade=50)
Choice.objects.create(question=q1, choice_text='A web framework', is_correct=True)
Choice.objects.create(question=q1, choice_text='A database', is_correct=False)
Choice.objects.create(question=q1, choice_text='A programming language', is_correct=False)

q2 = Question.objects.create(course=course, question_text='What is Python?', grade=50)
Choice.objects.create(question=q2, choice_text='A snake', is_correct=False)
Choice.objects.create(question=q2, choice_text='A programming language', is_correct=True)
Choice.objects.create(question=q2, choice_text='A database', is_correct=False)
