from django.db import models
from django.contrib.auth.models import User




class Story(models.Model):
    header = models.CharField(max_length=200)
    strong_text = models.TextField(null=True, blank=True)
    text = models.TextField()
    text2 = models.TextField()
    sing_img = models.ImageField(upload_to='media/')
    img = models.ImageField(upload_to='media/')
    video = models.URLField()


    def __str__(self):
        return self.header





class Product(models.Model):
    TYPE = (
            ('sale', 'sale'),
            ('new', 'new'),
        )

    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200, null=True, blank=True)
    img = models.ImageField(upload_to='media/')
    info_name = models.CharField(max_length=200)
    status = models.CharField(max_length=50, choices=TYPE, null=True, blank=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(null=True, blank=True)
    pro_quantity = models.PositiveIntegerField(default=1)
    description = models.TextField()
    category = models.CharField(max_length=100, null=True, blank=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.img.url
        except:
            url = ''
        return url


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)



class Shipping(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField()
    note = models.TextField()





class News(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='media/')
    date = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.name


class Inst_img(models.Model):
    img = models.ImageField(upload_to='media/')

class Post(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    img = models.ImageField(upload_to='media/')
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=200)
    type_of_job = models.CharField(max_length=100)
    img = models.ImageField(upload_to='media/')
    info = models.TextField()
    face_link = models.CharField(max_length=200, null=True, blank=True)
    inst_link = models.CharField(max_length=200, null=True, blank=True)
    twitter_link = models.CharField(max_length=200, null=True, blank=True)


    def __str__(self):
        return self.name




class Comment(models.Model):
    comment = models.TextField()
    email = models.EmailField(null=True, blank=True)
    name = models.CharField(max_length=100)
    img = models.ImageField(default='images/blog-single-author2.png')
    date = models.DateTimeField(auto_now_add=True)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.IntegerField()
    subject = models.TextField(null=True, blank=True)
    message = models.TextField()




