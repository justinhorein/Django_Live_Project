from django.db import models

# Create your models here.

# List of all the grading options
COMIC_GRADING = (
    ('10.0 GM Gem Mint', '10.0 GM Gem Mint'), ('9.9 M Mint', '9.9 M Mint'),
    ('9.8 NM/M Near Mint/Mint', '9.8 NM/M Near Mint/Mint'), ('9.6 NM+ Near Mint+', '9.6 NM+ Near Mint+'),
    ('9.4 NM Near Mint', '9.4 NM Near Mint'), ('9.2 NM- Near Mint-', '9.2 NM- Near Mint-'),
    ('9.0 VF/NM Very Fine/Near Mint', '9.0 VF/NM Very Fine/Near Mint'), ('8.5 VF+ Very Fine+', '8.5 VF+ Very Fine+'),
    ('8.0 VF Very Fine', '8.0 VF Very Fine'), ('7.5 VF- Very Fine-', '7.5 VF- Very Fine-'),
    ('7.0 FN/VF Fine/Very Fine', '7.0 FN/VF Fine/Very Fine'), ('6.5 FN+ Fine+', '6.5 FN+ Fine+'),
    ('6.0 FN Fine', '6.0 FN Fine'), ('5.5 FN- Fine-', '5.5 FN- Fine-'),
    ('5.0 VG/FN Very Good/Fine', '5.0 VG/FN Very Good/Fine'), ('4.5 VG+ Very Good+', '4.5 VG+ Very Good+'),
    ('4.0 VG Very Good', '4.0 VG Very Good'), ('3.5 VG- Very Good-', '3.5 VG- Very Good-'),
    ('3.0 GD/VG Good/Very Good', '3.0 GD/VG Good/Very Good'), ('2.5 GD+ Good+', '2.5 GD+ Good+'),
    ('2.0 GD Good', '2.0 GD Good'), ('1.8 GD- Good-', '1.8 GD- Good-'),
    ('1.5 FR/GD Fair/Good', '1.5 FR/GD Fair/Good'), ('1.0 FR Fair', '1.0 FR Fair'),
    ('0.5 PR Poor', '0.5 PR Poor'))

# Allows for the user to pick which code they're putting in the ISBN field
ISBN_BARCODE = (
    ('ISBN', 'ISBN'), ('Barcode', 'Barcode')
)


class Books(models.Model):
    # Series name (Batman, etc.)
    series = models.CharField(max_length=200)
    # Issue number:
    issue = models.PositiveSmallIntegerField()
    # Specific issue title:
    title = models.CharField(max_length=200, null=True)
    # year published:
    year = models.PositiveIntegerField(null=True)
    publisher = models.CharField(max_length=200, null=True)
    isbn_or_Barcode = models.PositiveIntegerField(null=True)
    # Allows the option for the isbn field to be either an isbn or barcode. The isbn_choice differentiates
    isbn_choice = models.CharField(choices=ISBN_BARCODE, null=True, max_length=7)
    grade = models.CharField(choices=COMIC_GRADING, null=True, max_length=100)
    # Additional notes about the book - long length for all the notes needed
    notes = models.CharField(max_length=1000, null=True)

    Book = models.Manager()

    def __str__(self):
        return self.series
