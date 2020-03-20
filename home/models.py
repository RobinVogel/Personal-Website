from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

# Create your models here.
class News(models.Model):
    """Small news for the homepage."""

    # Fields
    date = models.DateField(help_text="Month and year of the news item.")
    text = models.CharField(max_length=400, help_text="News item.")

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """Strings for representing the Model object."""
        return f'news {self.date}'


class Publications(models.Model):
    """Publications for the research page."""

    # Fields
    date = models.DateField(help_text="Year of the publication.")
    name = models.CharField(
        max_length=400, help_text="Name of the publication.", default="")
    authors = models.CharField(
        max_length=400, help_text="Authors of the publication.", default="")
    arxiv_link = models.CharField(
        max_length=400, help_text="ArXiV link.", default="")
    code_link = models.CharField(
        max_length=400, help_text="Code link.", default="")
    venue_name = models.CharField(
        max_length=400, help_text="Venue name.", default="")
    venue_link = models.CharField(
        max_length=400, help_text="Venue link.", default="")
    poster_filename = models.CharField(
        max_length=400, help_text="Poster file name.", default="",
        blank=True)
    slides_filename = models.CharField(
        max_length=400, help_text="Slides handout file name.", default="",
        blank=True)

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """Strings for representing the Model object."""
        return f'publi {self.name}'


class Talks(models.Model):
    """Publications for the research page."""

    # Fields
    date = models.DateField(help_text="Month and year of the talk.")
    location = models.CharField(max_length=400, help_text="Location.",
                                default="Unknown location")
    event_name = models.CharField(
        max_length=400, help_text="Name of the event.", default="")
    event_link = models.CharField(
        max_length=400, help_text="Event link.", default="")
    poster_filename = models.CharField(
        max_length=400, help_text="Poster file name.", default="",
        blank=True)
    slides_filename = models.CharField(
        max_length=400, help_text="Slides handout file name.", default="",
        blank=True)

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """Strings for representing the Model object."""
        return f'talk {self.event_name} {self.date}'


class Articles(models.Model):
    """Blog articles."""

    # Fields
    date = models.DateField(help_text="Date.")
    title = models.CharField(max_length=400, help_text="Title.", default="")
    subtitle = models.CharField(max_length=10000, help_text="Subtitle.", default="")
    summary = models.TextField(max_length=10000,
        help_text="Summary.", default="")
    main_text = models.TextField(help_text="Main text.", default="")
    main_picture = models.CharField(max_length=400,
                                    help_text="Main picture.",
                                    default="")
    url_name = models.CharField(max_length=400,
        help_text="Name that display in the url.", default="")

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        """Strings for representing the Model object."""
        return f'article {self.url_name}'
