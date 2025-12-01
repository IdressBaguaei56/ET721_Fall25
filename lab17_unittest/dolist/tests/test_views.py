import django.test import TestCase
from django.url import reverse
from .models import Todolist
from .forms import Todolistform
from .views import addTodoitem, completedTodo, deletecompleted, deleteAll

class TodoviewsTestCase(TestCase):
    def setUp(self):
        # create initial dtat for testing 
        self.task1 = Todolist.objects.create(text = "Task1 ", completed = False)
        self.task1 = Todolist.objects.create(text = "Task2 ", completed = False)
        self.task1 = Todolist.objects.create(text = "Task3 ", completed = True)

    def test_index_view(self):
        # test the index view render the correct context and template 
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'index.html')
        