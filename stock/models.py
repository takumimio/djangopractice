from django.db import models

class Price(models.Model):
	symbol = models.CharField(max_length=6)
	date = models.DateField()
	#time = models.TimeField()
	open = models.DecimalField(max_digits=18,decimal_places=4)
	high = models.DecimalField(max_digits=18,decimal_places=4)
	low = models.DecimalField(max_digits=18,decimal_places=4)
	close = models.DecimalField(max_digits=18,decimal_places=4)
	volume = models.BigIntegerField()

	def __str__(self):
		return self.symbol


