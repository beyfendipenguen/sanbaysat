from django.db import models
from accounts.models import UserAccount
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Customer(models.Model):
    customer_user = models.OneToOneField(UserAccount, on_delete=models.CASCADE)
    customer_address = models.CharField(max_length=150)
    customer_city = models.CharField(max_length=30)
    customer_country = models.CharField(max_length=30)

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Customer_detail", kwargs={"pk": self.pk})
