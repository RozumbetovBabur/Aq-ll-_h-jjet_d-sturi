from django.db import models

class Document(models.Model):
    file = models.FileField(upload_to='uploads/')
    title = models.CharField(max_length=255, blank=True)
    extracted_text = models.TextField(blank=True)
    label = models.CharField(max_length=128, blank=True)
    confidence = models.FloatField(null=True, blank=True)
    summary = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or f'Document {self.pk}'
