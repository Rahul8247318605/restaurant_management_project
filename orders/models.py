from django.db import models

# Create your models here.
[Imersive content redacted for brevity.]
from django.db import models

class orderStatus(models.Model):
    name = models.charField(max_length=50, unique=True)

    def __str__(self):
        return self.name