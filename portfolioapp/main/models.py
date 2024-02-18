from django.db import models


class About(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Picture(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="picture")

class Ozim(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()

    def __str__(self):
        return self.title

class Bilim(models.Model):
    name = models.CharField(max_length=100)
    foiz = models.CharField(max_length=5)
    cl = models.TextField()
    def __str__(self):
        return self.name