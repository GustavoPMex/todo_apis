from django.test import TestCase
from .models import Todo

class TodoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # This is an object created for testing in the model "Todo"
        Todo.objects.create(title='kjask', body='a body')
    
    def test_title_content(self):
        # This testing the title of the object created above
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.title}'
        self.assert_(expected_object_name.isalpha(), 'Only strings')

    def test_body_content(self):
        # This testing the body of the object created above
        todo = Todo.objects.get(id=1)
        expected_object_name = f'{todo.body}'
        self.assertEqual(expected_object_name, 'a body')