from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class QuizLevel(models.Model):
    level_title = models.CharField(max_length=150)

    def __str__(self):
        return self.level_title


class QuizMeta(models.Model):
    quiz_banner_url = models.URLField(default="https://source.unsplash.com/.../1151x180")

    def __str__(self):
        return self.quiz_banner_url


class Quiz(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    summary = models.TextField(max_length=300)
    score = models.IntegerField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(auto_now_add=True)
    level_id = models.ForeignKey(QuizLevel, on_delete=models.PROTECT, null=True)
    img_url_id = models.ForeignKey(QuizMeta, on_delete=models.CASCADE, null=True)

    def publish(self):
        self.published_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class QuizType(models.Model):
    type_title = models.CharField(max_length=150)

    def __str__(self):
        return self.type_title


class QuizQuestion(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE, null=True)
    type_id = models.ForeignKey(QuizType, on_delete=models.PROTECT, null=True)
    content = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.quiz_id.title}: {self.content}"


class QuizAnswer(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.PROTECT, null=True)
    question_id = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, null=True)
    correct = models.BooleanField(default=False)
    content = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.quiz_id.title}: {self.content}"


class Take(models.Model):
    STATUS_CHOICES = (
        ('started', 'STARTED'),
        ('paused', 'PAUSED'),
        ('finished', 'FINISHED'),
    )
    user_id = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    quiz_id = models.ForeignKey(Quiz, on_delete=models.PROTECT, null=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    score = models.PositiveSmallIntegerField(default=0)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)


class TakeAnswer(models.Model):
    take_id = models.ForeignKey(Take, on_delete=models.PROTECT, null=True)
    answer_id = models.ForeignKey(QuizAnswer, on_delete=models.PROTECT, null=True)
    selected = models.BooleanField(default=False)
