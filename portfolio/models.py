from django.db import models

# Create your models here.
class Project(models.Model):
    models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,
        verbose_name="Título")
    subtitle = models.CharField(max_length=511,
        verbose_name="Subtítulo")
    description = models.TextField(
        verbose_name="Descripción")
    image = models.ImageField(upload_to="projects",
        verbose_name="Imagen")
    link = models.URLField(null=True, blank=True,
        verbose_name="Enlace Web")
    created = models.DateTimeField(auto_now_add=True,
        verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"
        ordering = ["-created"]

    def __str__(self):
        return self.title
