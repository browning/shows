from django.db import models


class Genre(models.Model):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length=100)

class Venue(models.Model):
	def __unicode__(self):
		return self.name
	name = models.CharField(max_length=150)
	address = models.CharField(max_length=300)

class Show(models.Model):
	def __unicode__(self):
		return self.acts
	acts = models.CharField(max_length=500)
	venue = models.ForeignKey(Venue)
	genre = models.ForeignKey(Genre)
	datetime = models.DateTimeField()
	hype = models.IntegerField()

	def iterableHype(self):
		return range(self.hype)
