from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductCategory(models.Model):
    title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان')
    url_title = models.CharField(max_length=300, db_index=True, verbose_name='عنوان در url')
    is_active = models.BooleanField(verbose_name="فعال/غیر فعال")
    is_delete = models.BooleanField(verbose_name="حذف شده/حذف نشده", null=True)
    def __str__(self):
        return f'({self.title} - {self.url_title})'


class Product(models.Model):
    category = models.ManyToManyField(ProductCategory,
                                      null=True,
                                      verbose_name='دسته بندی ها',
                                      related_name='products_category')
    title = models.CharField(max_length=300)
    price = models.IntegerField(verbose_name="قیمت")
    short_description = models.CharField(max_length=200, db_index=True, null=True, verbose_name="توضیجات کوتاه")
    description = models.CharField(max_length=200, null=True, verbose_name="توضیجات اصلی")
    slug = models.SlugField(default="", null=False, blank=True, db_index=True, max_length=200, unique=True)
    is_active = models.BooleanField(default=False, verbose_name="فعال/غیرفعال")
    is_delete = models.BooleanField(verbose_name="حذف شده/حذف نشده")

    def get_absolute_url(self):
        return reverse('products_detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} ({self.price})"


class ProductTag(models.Model):
    tag = models.CharField(max_length=300, verbose_name="عنوان")
    product = models.ForeignKey(Product, related_name="product_tags", on_delete=models.CASCADE)

