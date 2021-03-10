from django.db import models

# Create your models here.
CATEGORY_CHOICES = (
    ('T', 'Tshirt'),
    ('S', 'Shirt'),
    ('J', 'Jeans')
)
class Men_Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    image = models.ImageField(upload_to="gallery", default='Gallery/T2.jpg')
    description = models.CharField(max_length=500)


    def __str__(self):
        return self.title

