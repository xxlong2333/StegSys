from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import ImageAnalysis
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import io
import json
from django.utils import timezone

@login_required
def index(request):
    analyses = ImageAnalysis.objects.filter(user=request.user)
    return render(request, 'index.html', {'analyses': analyses})

@login_required
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        analysis = ImageAnalysis.objects.create(
            user=request.user,
            image=image
        )
        return JsonResponse({'status': 'success', 'analysis_id': analysis.id})
    return JsonResponse({'status': 'error'}, status=400)

@login_required
def analyze_image(request, analysis_id):
    try:
        analysis = ImageAnalysis.objects.get(id=analysis_id, user=request.user)
        # TODO: 实现深度学习模型分析
        # 这里需要添加您的深度学习模型代码
        analysis.is_stego = False  # 示例结果
        analysis.confidence = 0.95  # 示例置信度
        analysis.result = {'details': '示例分析结果'}  # 示例详细结果
        analysis.analysis_time = timezone.now()
        analysis.save()
        return JsonResponse({
            'status': 'success',
            'is_stego': analysis.is_stego,
            'confidence': analysis.confidence,
            'result': analysis.result
        })
    except ImageAnalysis.DoesNotExist:
        return JsonResponse({'status': 'error'}, status=404)

@login_required
def get_analysis_history(request):
    analyses = ImageAnalysis.objects.filter(user=request.user)
    data = [{
        'id': analysis.id,
        'image_url': analysis.image.url,
        'upload_time': analysis.upload_time.strftime('%Y-%m-%d %H:%M:%S'),
        'is_stego': analysis.is_stego,
        'confidence': analysis.confidence
    } for analysis in analyses]
    return JsonResponse({'analyses': data})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 重定向到/home/路径
        else:
            messages.error(request, '用户名或密码错误')
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, '注册失败，请检查输入信息')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
