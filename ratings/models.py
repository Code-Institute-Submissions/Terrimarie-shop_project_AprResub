from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# my ratings code

class Rating(models.Model):
    image = models.ImageField(upload_to='media/')
    score = models.IntegerField(default=0, 
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return str(self.pk)
        