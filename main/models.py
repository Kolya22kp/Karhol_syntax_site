from django.db import models

# Create your models here.

class News(models.Model):
    title = models.TextField()
    date = models.TextField()
    description = models.TextField()

class Works(models.Model):
    name = models.TextField()
    image = models.URLField()


class Catalog(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    old_price = models.IntegerField()
    estimated_time = models.TextField()
    description = models.TextField()


class Reviews(models.Model):
    name = models.TextField()
    estimation = models.TextField()
    description = models.TextField()

class System_contacts(models.Model):
    name = models.TextField()
    email = models.EmailField()
    login = models.TextField()
    message = models.TextField()
    system = models.TextField()

class System_redirects_tg(models.Model):
    ip = models.TextField()
    user_agent = models.TextField()
    referer = models.TextField()
    host = models.TextField()
    method = models.TextField()
    server_name = models.TextField()
    server_port = models.TextField()
    server_host = models.TextField()
    date = models.TextField()

class Documents(models.Model):
    name = models.TextField()
    title = models.TextField()
    content = models.TextField()