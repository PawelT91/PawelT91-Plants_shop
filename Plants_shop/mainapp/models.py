from django.db import models

# В семействе кактусовые 3 подсемейства


class CactusSubfamily(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=16, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    image = models.ImageField(upload_to='cactus_plants', verbose_name='Картинка', blank=True)

    def __str__(self):
        return self.name
# В каждом подсемействе есть Роды


class CactusGenus(models.Model):
    name = models.CharField(verbose_name=u'Название', max_length=16, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)
    subfamily = models.ForeignKey(CactusSubfamily, verbose_name='Подсемейство', null=True)

    def __str__(self):
        return self.name
# В каждом роде есть виды

class ViewCactus(models.Model):
    type = models.CharField(verbose_name=u'Название', max_length=32, unique=True)
    genus = models.ForeignKey(CactusGenus, verbose_name='Род', null=True)
    image = models.ImageField(verbose_name='Картинка', blank=True)
    complexity_of_cultivation = models.CharField(verbose_name='Сложность выращивания', max_length=16)
    price = models.FloatField(verbose_name='Цена', blank=True)
    area = models.CharField(verbose_name=u'Меcто прозизрастания', max_length=32, unique=True)
    diametr = models.CharField(verbose_name=u'Диаметр сеянцев(мм)', max_length=32, unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name