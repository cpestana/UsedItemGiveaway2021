from django.db import models
from  django.contrib.auth.models import User

# Create your models here.
# Each model will become a table in the database
class Items(models.Model):
    itemName = models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    itemLocation=models.TextField()
    itemUserEmail=models.TextField()
    itemDescription=models.CharField(max_length=255)
    entryDate=models.DateField()

    def __str__(self):
        return self.itemName
    
    class Meta:
        db_table='item'
    
class Comments(models.Model):
    commentTitle=models.CharField(max_length=255)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    entryDate=models.DateField()
    user=models.ManyToManyField(User)
    commentText=models.TextField()

    def __str__(self):
        return self.commentTitle
    
    class Meta:
        db_table='comments'


