import os

from django.db import models
# Create your models here.
class CarInfo(models.Model):
    id = models.AutoField(primary_key=True)  # 自动生成的主键
    brand = models.CharField(max_length=100)  # 品牌名称，最大长度100
    model = models.CharField(max_length=100)  # 型号，最大长度100
    price = models.DecimalField(max_digits=10, decimal_places=2)  # 价格，支持小数
    age = models.IntegerField()  # 生产年份
    image = models.ImageField(upload_to='car_image/')  # 图片，上传到car_images目录

    def __str__(self):
        return f"{self.brand} ({self.age})"
    
    def delete(self, *args, **kwargs):
        # 删除关联的图片文件
        if self.image and os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)