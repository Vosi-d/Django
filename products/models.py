from django.db import models
# pip install Pillow
class CategoryModel(models.Model):
    title = models.CharField(max_length=70)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
class ProductModel(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(default=0)
    image = models.FileField(upload_to='product')
    descriptions = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Все продукты'

