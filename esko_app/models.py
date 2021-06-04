from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

from django.urls import reverse

# from taggit.managers import TaggableManager
# Create your models here.



class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('/esko_app/home/')


# class Post(models.Model):

# 	CATEGORIES = [
# 		('sell', 'sell'),
# 		('find', 'find'),
# 		('services/rent', 'services/rent'),
# 		('swap', 'swap'),
# 	]
	
# 	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
# 	category = models.CharField(max_length=13,choices=CATEGORIES)
# 	description = models.TextField(max_length=250)
# 	# tags = models.CharField(max_length=100)
# 	post_image = models.ImageField(upload_to='post_pics',null=True,blank=True)
# 	date = models.DateTimeField(auto_now_add=True)
# 	likes = models.ManyToManyField(User, related_name='user_posts')
# 	tags = TaggableManager()


# 	def total_likes(self):
# 		return self.likes.count()

# 	def __str__(self):
# 		return self.category

# 	def get_absolute_url(self):
# 		return reverse('esko_app:post-detail', kwargs={'pk':self.pk})
		
class Post(models.Model):

	CATEGORIES = [
		('sell', 'sell'),
		('find', 'find'),
		('services/rent', 'services/rent'),
		('swap', 'swap'),
	]
	
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	category = models.CharField(max_length=13,choices=CATEGORIES)
	description = models.TextField(max_length=250)
	tags = models.CharField(max_length=100)
	post_image = models.ImageField(upload_to='post_pics',null=True,blank=True)
	date = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User, related_name='user_posts')
	# tags = TaggableManager()

	def tag_list(self):
		
		return self.tags.split(',')


	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.category

	def get_absolute_url(self):
		return reverse('esko_app:post-detail', kwargs={'pk':self.pk})

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics', blank=True)
	year_level = models.CharField(max_length=30, blank=True)
	phone_number = models.IntegerField(null=True,blank=True)
	sns_account = models.URLField(max_length = 200,blank=True)
	bio = models.CharField(max_length=200, blank=True)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile,self).save(*args, **kwargs)

		img = Image.open(self.profile_pic.path)

		if img.height > 400 or img.width > 400:
			output_size = (400,400)
			img.thumbnail(output_size)
			img.save(self.profile_pic.path)


class Comment(models.Model):
	post = models.ForeignKey(Post,related_name="comments",on_delete=models.CASCADE)
	commenter = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	body = models.TextField()
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return '%s - %s' % (self.post.category, self.commenter)

class Report(models.Model):
	PROBLEMS = [
 		('hate speech', 'hate speech'),
 		('violence', 'violence'),
 		('harassment', 'harassment'),
 		('nudity', 'nudity'),
 		('false information', 'false information'),
 		('spam', 'spam'),
 		('others', 'others')
 	]

	reporter = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	post = models.ForeignKey(Post,related_name="reports",on_delete=models.CASCADE)
	date_reported = models.DateTimeField(auto_now_add=True)
	problem = models.CharField(max_length=50,choices=PROBLEMS)
	notes = models.TextField(null=True,blank=True)

	def __str__(self):
		return '%s - %s' % (self.problem, self.reporter)



