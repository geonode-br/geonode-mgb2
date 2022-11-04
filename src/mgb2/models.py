from django.db import models
from geonode.layers.models import Layer


# Create your models here.
class RecursoMGB2(models.Model):
    """
    """
    layer = models.OneToOneField(
        Layer,
        on_delete=models.CASCADE,
        related_name="metadado_mgb2",
        related_query_name="metadado_mgb2",
        primary_key=True
    )

    character_encoding = models.CharField(
        max_length=10,
        choices=(
            ("UTF-8", "UTF-8"),
            ("LATIN1", "LATIN1"),
        )
    )

    publicar = models.BooleanField(
        default=False
    )

    def __str__(self) -> str:
        return str(self.layer)