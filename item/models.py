from django.db import models
from user.models import *
from django.core.validators import MinValueValidator


class Category(models.Model):
    category_name = models.CharField(max_length=50, blank=False)
    category = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="+", blank=True, null=True
    )

    def __str__(self):
        return self.category_name

class Item(models.Model):
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        default=0,
        related_name="seller",
    )
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, blank=False, null=False
    )
    item_name = models.CharField(max_length=50, blank=False)
    price = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock = models.PositiveIntegerField(blank=True, null=True)
    sold = models.PositiveIntegerField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    image = models.URLField(blank=True, null=True, max_length=1000)

    def __str__(self):
        return self.item_name

    def manage_stock(self, old_stock):
        #used to reduce Item stock
        new_stock = self.stock - int(old_stock)
        self.stock = new_stock
        self.save()


    def check_stock(self, qty):
        #used to check if order quantity exceeds stock levels
        if int(qty) > self.stock:
            return False
        return True

    def place_order(self, user):
        return


class Cart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name="customer")

    @property
    def total_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.total_item_cost for item in cartitems])
        return total

    def __str__(self):
        return "cart of " + str(self.customer)

class cartItem(models.Model):
    class meta:
        constraints = [
            models.UniqueConstraint(
                fields=["cart", "item"], name="unique_item_in_cart"
            )
        ]

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cartitems")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=0)

    @property
    def total_item_cost(self):
        return self.item.price * self.quantity
    def __str__(self):
        return "cart item of cart number " + str(self.cart.pk) + " of customer " + str(self.cart.customer)  