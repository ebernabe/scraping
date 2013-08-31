from django.db import models

# Create your models here.

class Chat(models.Model):
	usuario_twitter = models.CharField(max_length=250)
	url_twitter = models.CharField(max_length=255)
	def __unicode__(self):
		return self.usuario_twitter
