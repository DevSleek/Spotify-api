from django.db import models


class Song(models.Model):
    album = models.ForeignKey('music.Album', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=150, blank=False, null=False)
    picture = models.URLField(blank=True)
    source = models.URLField(blank=False, null=False)

    listened = models.BigIntegerField(default=0)

    def __str__(self):
        return self.title