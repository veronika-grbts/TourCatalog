from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    country = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tour_type = models.CharField(
        max_length=50,
        choices=[
            ('beach', 'Пляжний'),
            ('excursion', 'Екскурсійний'),
            ('ski', 'Гірськолижний'),
            ('adventure', 'Пригодницький'),
            ('cruise', 'Круїзний'),
            ('wellness', 'Оздоровчий'),
            ('safari', 'Сафарі'),
            ('culinary', 'Гастрономічний'),
            ('cultural', 'Культурний'),
            ('ecotourism', 'Екотуризм'),
        ]
    )
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        default=0.0
    )

    image = models.ImageField(upload_to='main/tours/', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_display_for_tour_type(self):
        return dict(self._meta.get_field('tour_type').choices).get(self.tour_type)

    def get_previous_url(self):
        previous_tour = Tour.objects.filter(id__lt=self.id).last()
        if previous_tour:
            return reverse('tour_detail', args=[previous_tour.id])
        return None

    def get_next_url(self):
        next_tour = Tour.objects.filter(id__gt=self.id).first()
        if next_tour:
            return reverse('tour_detail', args=[next_tour.id])
        return None

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Тури'