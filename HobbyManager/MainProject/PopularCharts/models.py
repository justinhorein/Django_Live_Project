from django.db import models
from django.forms import ModelForm

# Dropdown data choices

KEYS = (
('C', 'C'), ('C#', 'C#'), ('Db', 'Db'), ('D', 'D'), ('D#', 'D#'), ('Eb', 'Eb'), ('E', 'E'), ('F', 'F'),
('F#', 'F#'), ('Gb', 'Gb'), ('G', 'G'), ('G#', 'G#'), ('Ab', 'Ab'), ('A', 'A'), ('A#', 'A#'), ('Bb', 'Bb'),
('B', 'B'))

CAPO = (
('None', 'None'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'))

VERSIONS = (
('Ver 1', 'Ver 1'), ('Ver 2', 'Ver 2'), ('Ver 3', 'Ver 3'), ('Ver 4', 'Ver 4'), ('Ver 5', 'Ver 5'),
)

LEVELS = (
('Easy', 'Easy'), ('Intermediate', 'Intermediate'), ('Difficult', 'Difficult'), ('Advanced', 'Advanced'),
)


class Song(models.Model):
    version = models.CharField(max_length=10, choices=VERSIONS)
    level = models.CharField(max_length=25, choices = LEVELS)
    song = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    tab_by = models.CharField(max_length=100)
    tuning = models.CharField(max_length=50)
    original_key = models.CharField(max_length=10, choices=KEYS)
    transposed_key = models.CharField(max_length=10, choices=KEYS)
    guitar_capo = models.CharField(max_length=10, choices=CAPO)

    Songs = models.Manager()



    def __str__(self):
        return self.song