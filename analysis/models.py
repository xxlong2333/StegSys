from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=15, blank=True, null=True)
    organization = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"

class ImageAnalysis(models.Model):
    ANALYSIS_STATUS = (
        ('pending', '待分析'),
        ('processing', '分析中'),
        ('completed', '已完成'),
        ('failed', '分析失败'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='analyses')
    image = models.ImageField(upload_to='analysis_images/%Y/%m/%d/')
    original_filename = models.CharField(max_length=255)
    file_size = models.IntegerField()  # 文件大小（字节）
    image_width = models.IntegerField(null=True, blank=True)
    image_height = models.IntegerField(null=True, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=ANALYSIS_STATUS, default='pending')
    is_stego = models.BooleanField(default=False)
    confidence = models.FloatField(null=True, blank=True)
    analysis_time = models.DateTimeField(null=True, blank=True)
    result = models.JSONField(null=True, blank=True)
    error_message = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-upload_time']
        indexes = [
            models.Index(fields=['user', 'upload_time']),
            models.Index(fields=['status']),
            models.Index(fields=['is_stego']),
        ]

    def __str__(self):
        return f"Analysis {self.id} - {self.original_filename}"

class AnalysisResult(models.Model):
    analysis = models.OneToOneField(ImageAnalysis, on_delete=models.CASCADE, related_name='detailed_result')
    stego_type = models.CharField(max_length=50, null=True, blank=True)  # 隐写类型
    embedding_rate = models.FloatField(null=True, blank=True)  # 嵌入率
    payload_size = models.IntegerField(null=True, blank=True)  # 有效载荷大小
    detection_method = models.CharField(max_length=100)  # 检测方法
    confidence_score = models.FloatField()  # 置信度分数
    analysis_duration = models.FloatField()  # 分析持续时间（秒）
    created_at = models.DateTimeField(auto_now_add=True)
    details = models.JSONField(null=True, blank=True)  # 详细分析结果

    def __str__(self):
        return f"Result for {self.analysis}"

class SystemLog(models.Model):
    LOG_LEVEL = (
        ('info', '信息'),
        ('warning', '警告'),
        ('error', '错误'),
    )

    timestamp = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10, choices=LOG_LEVEL)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    details = models.JSONField(null=True, blank=True)

    class Meta:
        ordering = ['-timestamp']
        indexes = [
            models.Index(fields=['timestamp']),
            models.Index(fields=['level']),
        ]

    def __str__(self):
        return f"{self.timestamp} - {self.level}: {self.message[:50]}"
