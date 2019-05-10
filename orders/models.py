from django.db import models

class Order(models.Model):

    customer_name = models.CharField(max_length=64, blank=True, null=True,default=None)
    customer_email = models.EmailField(blank=True, null=True,default=None)
    customer_phone = models.CharField(max_length=48, blank=True, null=True,default=None)
    comments = models.TextField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    modified = models.DateTimeField(auto_now_add=False, auto_now=True)


    def __str__(self):
        return "Заказ %s" % self.id

    class Meta:
    verbose_name = 'Заказ'
    verbose_name_plural = 'Заказы'

    class ProductInOrder(models.Model):
        order = models.ForeignKey(Order, blank=True,null=True,default=None)
        product = models.ForeignKey(Product, blank=True, null=True, default=None)
        is_active = models.BooleanField(default=True)
        created = models.DateTimeField(auto_now_add=True, auto_now=False)
        modified = models.DateTimeField(auto_now_add=False, auto_now=True)


def __str__(self):
    return "%s" % self.product.name


class Meta:
    verbose_name = 'Товар'
    verbose_name_plural = 'Товары'