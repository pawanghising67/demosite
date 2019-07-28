from django.db import models


class menu(models.Model):
    type = models.CharField(max_length=100)

    def get_menu(self):
        return self.menu


class menuType(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    ingredients = models.CharField(max_length=300)

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_ingredients(self):
        return self.ingredients

    class Meta(object):
        abstract = True


class Dinner(menuType):
    pass

    class Meta(object):
        abstract = True


class Dessert(menuType):
    pass

    class Meta(object):
        abstract = True


class BeverageProgram(menuType):
    pass

    class Meta(object):
        abstract = True
