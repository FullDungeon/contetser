from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Theme(models.Model):
    name = models.CharField(default='', max_length=40)
    order = models.IntegerField(default=0, unique=True)

    def getName(self):
        return self.name

    def __str__(self):
        return self.name

class Topic(models.Model):
    name  = models.CharField(default='', max_length=40)
    theme = ForeignKey(Theme, on_delete=models.PROTECT)

    def getName(self):
        return self.name

    def getNameWithTheme(self):
        return self.theme.getName() + ": " + self.name

    def __str__(self):
        return self.name

class Task(models.Model):
    PREFFIXES = (
        ('A', 'A'), 
        ('B', 'B'), 
        ('C', 'C'), 
        ('D', 'D'), 
        ('E', 'E'), 
        ('F', 'F'), 
        ('G', 'G'), 
        ('H', 'H'), 
        ('I', 'I'),
        ('J', 'J'),
        ('K', 'K'),
        ('L', 'L'),
        ('M', 'M'),
        ('N', 'N'),
        ('O', 'O'),
        ('P', 'P'),
        ('Q', 'Q'),
        ('R', 'R'),
        ('S', 'S'),
        ('T', 'T'),
        ('U', 'U'),
        ('V', 'V'),
        ('W', 'W'),
        ('X', 'X'),
        ('Y', 'Y'),
        ('Z', 'Z'), 
    )

    name        = models.CharField(default='', max_length=75)
    time        = models.FloatField(default=0.5)
    memory      = models.IntegerField(default=12)
    difficult   = models.IntegerField(default=0)
    text        = models.TextField(default='')
    input_text  = models.TextField(default='')
    output_text = models.TextField(default='')
    examples    = models.TextField(default='')

    preffix = models.CharField(default='', choices=PREFFIXES, max_length=2)
    topic   = ForeignKey(Topic, on_delete=models.PROTECT)

    def getFullName(self):
        if self.preffix != "":
            return self.preffix + ". " + self.name

        return self.name

    def getName(self):
        return self.name

    def __str__(self):
        return self.getFullName()

    class Meta:
        ordering = ['preffix', 'name']