from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    """
    A single Blog post
    """
    
    price = models.DecimalField(max_digits=6, decimal_places=2, default=10)
    
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    
    SEO = 'SEO'
    SEM = 'SEM'
    SOCIAL = 'Social Media'
    OM_CATEGORY_CHOICES = [
        (SEO, 'SEO'),
        (SEM, 'SEM'),
        (SOCIAL, 'Social Media'),
    ]
    
    category = models.CharField(max_length=30, choices=OM_CATEGORY_CHOICES, null=True)
    
    BUG = 'Bug'
    FEATURE = 'Feature Request'
    TYPE_CHOICES = [
        (BUG, 'Bug'),
        (FEATURE, 'Feature Request'),
    ]
    
    type = models.CharField(max_length=30, choices=TYPE_CHOICES, null=True)
    
    image = models.ImageField(upload_to="img", blank=True, null=True)
    upvotes = models.IntegerField(default=0)
    
    TODO = 'To Do'
    DOING = 'Doing'
    DONE = 'Done'
    STATUS_CHOICES = [
        (TODO, 'To Do'),
        (DOING, 'Doing'),
        (DONE, 'Done'),
    ]
    
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="To Do")
    
    def __unicode__(self):
        return self.title
        
class Voter(models.Model):
    user = models.ForeignKey(User)
    post = models.ForeignKey(Post)