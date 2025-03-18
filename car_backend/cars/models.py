from django.db import models

# Create your models here.
class CarInfo(models.Model):
    id = models.AutoField(primary_key=True)  # 自动生成的主键
    brand = models.CharField(max_length=100)  # 品牌名称，最大长度100
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 价格，支持小数
    year = models.IntegerField()  # 生产年份
    image = models.ImageField(upload_to='car_images/')  # 图片，上传到car_images目录

    def __str__(self):
        return f"{self.brand} ({self.year})"