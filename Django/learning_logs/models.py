from django.db import models

class Topic(models.Model):
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self) -> str:
        return self.text
    
class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
class Meta:
    verbose_name_plural = 'entries'
    def __str__(self):
        """Return a simple string representing the entry."""
        return f"{self.text[:50]}..."