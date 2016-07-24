from django.db import models
from django.core.validators import MaxValueValidator
from django.template.defaultfilters import slugify


from apps.courses.models import Course
# Create your models here.

class Note (models.Model):
	title = models.CharField(max_length = 140)
	slug = models.SlugField(editable = False,blank = True)
	description = models.TextField(blank = False)
	priority = models.PositiveIntegerField(default = 1, validators=[MaxValueValidator(10)])
	state = models.BooleanField(default = False)
	dateInitial = models.DateField(auto_now_add = True)
	dateEnd = models.DateField()
	course = models.ForeignKey(Course, null = True, on_delete = models.CASCADE)

	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.title)
		super(Note, self).save(*args, **kwargs)

	def __str__(self):
		return self.title
