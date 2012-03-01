from django.db import models

# Create your models here.
class Zombie(models.Model):
	name = models.CharField(max_length=50)
	graveyard = models.CharField(max_length=25)

	def __unicode__(self):
		return 'Zombie: %s - %s' % (self.pk, self.name,)

class Tweet(models.Model):
	zombie = models.ForeignKey('Zombie', related_name='tweets')
	status = models.CharField(max_length=140)
	created_at = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return 'Tweet: %s - %s' % (self.pk, self.status,)
