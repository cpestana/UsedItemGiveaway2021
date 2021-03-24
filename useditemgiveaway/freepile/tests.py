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
        self.type=Item(itemName='Shoes)
        self.user=User(username='cpestana')
    def test_string(self):
        self.assertEqual(str(self.type), 'Shoes')

    def test_table(self):
        self.assertEqual(str(Item._meta.db_table), 'Item')

class CommentTest(TestCase):
    def test_string(self):
        self.assertEqual(str(self.type), 'commentTitle')

    def test_table(self): 
        self.assertEqual(str(Comment._meta.db_table), 'Comment')

class NewItemForm(TestCase):
 #valid form data
 def test_itemform(self):
    data = {
        'itemName':'Shoes', 
        'itemLocation':'Please email for location in Seattle, WA', 
        'itemUserEmail':'clp@gmail.com', 
        'itemDescription':'Leather, size 8',
        'entryDate':'2021-03-21', 
     }
    form=ItemForm (data)
     self.assertTrue(form.is_valid)

class NewCommentForm(TestCase):
 #valid form data
 def test_commentform(self):
    data = {
        'commentTitle':'Shoes from clp@gmail.com', 
        'entryDate':'2021-03-21', 
        'commentText':'Great shoes from email user clp@gmail.com!', 
        'user':'self.u',
     }
    form=CommentForm (data)
     self.assertTrue(form.is_valid)

class New_Item_Authentication_Test(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username='cpestana', password='oliviA1686!')
        self.comment=Comment.objects.create(commentTitle='Shoes from clp@gmail.com'', entryDate='2021-03-21', commentText='Great shoes from email user clp@gmail.com!', user=self.test_user)

    def test_redirect_if_not_logged_in(self):
        response=self.client.get(reverse('newcomment'))
        self.assertRedirects(response, '/accounts/login?next=/freepile/newcomment/')
