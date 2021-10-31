from django.db import models
from django.utils.translation import gettext_lazy as _
from accounts.models import UserAccount
# Create your models here.


class Dealer(models.Model):
    dealer_user = models.OneToOneField(
        UserAccount, on_delete=models.DO_NOTHING)
    dealer_name = models.CharField(max_length=30, unique=True)
    dealer_address = models.CharField(max_length=150)
    dealer_city = models.CharField(max_length=30)
    dealer_country = models.CharField(max_length=30)

    class Meta:
        verbose_name = _("Dealer")
        verbose_name_plural = _("dealers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Dealer_details", kwargs={"pk": self.pk})
