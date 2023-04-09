from django.db import models
from django.contrib.auth.models import User


def user_directory_path(instance, filename):
    return "blog/{0}/{1}".format(instance.author.id, filename)

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta: # To fix the class name in admin dashboard when its are plural
        verbose_name_plural = "Categories"

    def __str__(self): # To prevent it's content appearing as "Category object" in admin dashboard
        return self.name 


class Post(models.Model):
    OPTIONS = (
        ('d', 'Draft'), # (database_log_name, user_shown_name)
        ('p', 'Published'),
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=user_directory_path, default='default_post_image.jpg')
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=OPTIONS, default='d')
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title
    
    def comment_count(self):
        """
        Comment is 1-1 and has 'post' key that we want to count and that is from Post class.
        So we need to count 'post' in Comment class.
        Thnx to orm structure of django, we can access this with using '_set.all()'.
        classname should be written in lowercase:
        classname_set.all() gives us all that classname has from this class.
        """  
        return self.comment_set.all().count()
    
    def view_count(self):
        return self.postview_set.all().count()    
    
    def like_count(self):
        return self.like_set.all().count()
    
    def comments(self):
        return self.comment_set.all()    

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # to delete the comment if user is deleted
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.user.username  # to return username on browser when comment is called
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
"""
CASCADE :  (ex:) delete comment if user deleted
PROTECT :  prevent deleting (ex:) a Category
"""