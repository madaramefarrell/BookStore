from django.db import models
from django.contrib.auth.models import User
from catalog.models import Book


class Cart(models.Model):
    belong_to = models.ForeignKey(
        to=User,
        related_name='production_list',
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(
        to=Book,
        related_name='book',
        on_delete=models.CASCADE
    )
    number = models.PositiveSmallIntegerField(blank=False, default=1)
    created_time = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ['belong_to']


    def get_belong_id(self):
        return self.belong_to.id

    def get_belong(self):
        return self.belong_to.username

    def get_cost(self):
        return self.item.price * self.number
