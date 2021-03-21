from django.test import TestCase
from django.test import TestCase
from django.config.models import user 
from .models import Item, Comment
import datetime
import .forms ItemForm, CommentForm
import django.urls import reverse_lazy, reverse 
# Create your tests here.

class ItemTest(TestCase): 
    def setUp(self):
        self.type=Meeting(itemName='Shoes)
        self.user=User(username='cpestana')
    def test_string(self):
        self.assertEqual(str(self.type), 'Shoes')

    def test_table(self):
        self.assertEqual(str(Meeting._meta.db_table), 'Item')

class CommentTest(TestCase):
    def test_string(self):
        self.assertEqual(str(self.type), 'commentTitle')

    def test_table(self): 
        self.assertEqual(str(Resource._meta.db_table), 'Comment')
