from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from analysis.models import UserProfile, SystemLog
from django.utils import timezone

class Command(BaseCommand):
    help = '初始化系统数据'

    def handle(self, *args, **kwargs):
        # 创建系统管理员
        admin, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin.set_password('admin123')
            admin.save()
            self.stdout.write(self.style.SUCCESS('成功创建管理员账号'))

        # 创建管理员档案
        UserProfile.objects.get_or_create(
            user=admin,
            defaults={
                'organization': '系统管理',
                'phone': '13800138000'
            }
        )

        # 创建系统日志
        SystemLog.objects.create(
            level='info',
            message='系统初始化完成',
            details={'version': '1.0.0'}
        )

        self.stdout.write(self.style.SUCCESS('数据初始化完成')) 