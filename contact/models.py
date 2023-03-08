from django.db import models
from phone_field import PhoneField
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Contact(models.Model):
    """ Contact page content """
    verbose_name = 'Treść strony'

    VsiibleSatus = (
        ('Y', 'Tak'),
        ('N', 'Nie'),
    )

    visible = models.CharField(
        choices=VsiibleSatus, max_length=1, null=False, blank=False)
    title = models.CharField(verbose_name='Tytuł strony', max_length=256,
                             null=False, blank=True, help_text='Maksymalna ilość znaków: 256')
    paragraph = models.CharField(verbose_name='Opis', max_length=512,
                                 null=False, blank=True, help_text='Maksymalna ilość znaków: 512, opis widoczny pod tytułem strony')

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CompanyInfo(models.Model):
    """" Company information """
    verbose_name = "Informacje o Firmie"

    VsiibleSatus = (
        ('Y', 'Tak'),
        ('N', 'Nie'),
    )

    visible = models.CharField(
        choices=VsiibleSatus, max_length=1, null=False, blank=False)
    name = models.CharField(verbose_name='Nazwa firmy', max_length=256,
                            null=False, blank=False, help_text='Maksymalna ilość znaków: 256')
    street = models.CharField(verbose_name='Ulica', max_length=128, null=False, blank=False,
                              help_text='Maksymala ilość znaków 128, przedrostek "ul" dodawany jest automatycznie')
    building = models.CharField(verbose_name='Numer budynku', max_length=6,
                                null=False, blank=False, help_text='Maksymalna ilość znaków: 6')
    flat = models.CharField(verbose_name='Numer mieszkania', max_length=6,
                            null=True, blank=True, help_text='Maksymalna ilość znaków: 6')
    phone = PhoneField(verbose_name='Numer telefonu', null=True, blank=True,
                       help_text='Maksymalna ilość znaków: 9, cyfry od 0 do 9, ext. nie jest potrzebny', validators=[MaxValueValidator(9), MinValueValidator(9)])
    email = models.EmailField(verbose_name='Adres e-mail', max_length=256, null=True,
                              blank=True, help_text='Maksymalna ilość znaków: 256, np. janusz.kowalski@email.pl,')
    nip = models.CharField(verbose_name='NIP', max_length=10, null=False, blank=False,
                           help_text='Maksymalna ilość znaków: 10, bez "-"', validators=[MaxValueValidator(10), MinValueValidator(10)])
    regon = models.CharField(verbose_name='REGON', max_length=9, null=False, blank=False,
                             help_text='Maksymalna ilość znaków: 9', validators=[MaxValueValidator(9), MinValueValidator(9)])
    account = models.CharField(verbose_name='Kont bankowe', max_length=28, null=True, blank=True,
                               help_text='Numer konta bankowego musi mieć 28 znaków', validators=[MaxValueValidator(28), MinValueValidator(28)])

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
