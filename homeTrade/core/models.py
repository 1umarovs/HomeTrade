from django.db import models

# Create your models here.


class House(models.Model):
    id  = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    img = models.ImageField(upload_to='houses/')
    type = models.CharField(max_length=50, choices=[
        ('apartment', 'Apartment'),
        ('house', 'House'),
    ])
    Purpose = models.CharField(max_length=50, choices=[
        ('rent', 'Rent'),
        ('sale', 'Sale'),
    ])
    home_type = models.CharField(max_length=50, choices=[
        ('residential', 'Residential'),
        ('commercial', 'Commercial'),
        ('land', 'Land'),
        ('industrial', 'Industrial'),
        ('other', 'Other'),
    ])
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rooms = models.PositiveIntegerField()
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    sqft = models.PositiveIntegerField() 
    parking = models.BooleanField(default=False)
    elevator = models.BooleanField(default=False)
    wifi = models.BooleanField(default=False)
    address = models.URLField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'House'
        verbose_name_plural = 'Houses'
        ordering = ['-created_at']


class houseGallery(models.Model):
    house = models.ForeignKey(House, related_name='gallery', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='house_gallery/')

    def __str__(self):
        return f"Gallery for {self.house.title}"
    
    class Meta:
        verbose_name = 'House Gallery'
        verbose_name_plural = 'House Galleries'
        ordering = ['house']


class houseFeature(models.Model):
    house = models.ForeignKey(House, related_name='features', on_delete=models.CASCADE)
    airconditioning = models.BooleanField(default=False)
    outdoor_kitchen = models.BooleanField(default=False)
    basketball = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    modern_kitchen = models.BooleanField(default=False)
    balcony = models.BooleanField(default=False)
    barbecue = models.BooleanField(default=False)
    fireplace = models.BooleanField(default=False)
    tennis_court = models.BooleanField(default=False)
    refrigerator = models.BooleanField(default=False)
    garage = models.BooleanField(default=False)
    recration = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    network = models.BooleanField(default=False)
    window_covering = models.BooleanField(default=False)
    landscaping = models.BooleanField(default=False)
    microwave = models.BooleanField(default=False)
    indoor_game = models.BooleanField(default=False)
    jacuzzi = models.BooleanField(default=False)
    washer = models.BooleanField(default=False)

    def __str__(self):
        return f"Feature for {self.house.title}"
    
    class Meta:
        verbose_name = 'House Feature'
        verbose_name_plural = 'House Features'
        ordering = ['house']

class Inquiry(models.Model):
    house = models.ForeignKey(House, related_name='inquiries', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Inquiry for {self.house.title} by {self.name}"

    class Meta:
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Inquiries'
        ordering = ['-created_at']