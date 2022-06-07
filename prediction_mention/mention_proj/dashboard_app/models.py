from unicodedata import name
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from sklearn.tree import DecisionTreeClassifier
import joblib


class Data(models.Model):
    name = models.CharField(max_length=100, null=True)
    maths = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], null=True)
    français = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], null=True)
    philosophie = models.PositiveBigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)], null=True)
    physique = models.PositiveBigIntegerField(null=True)
    mention = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ml_model_lib/ml_mention_model.joblib')
        self.mention = ml_model.predict([[self.maths, self.français, self.philosophie, self.physique]])
        return super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.name