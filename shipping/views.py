from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required,permission_required
from .forms import FeedbackForm
from .models import Feedback

def index(request):
    return render(request,'shipping/home.html')

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'shipping/feedback_list.html', {'feedbacks': feedbacks})

def feedback_detail(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    return render(request, 'shipping/feedback_detail.html', {'feedback': feedback})

def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'shipping/feedback_form.html', {'form': form})

@login_required
@permission_required('feedback.delete_feedback', raise_exception=True)
def feedback_update(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, 'shipping/feedback_form.html', {'form': form})

@login_required
@permission_required('feedback.delete_feedback', raise_exception=True)
def feedback_delete(request, pk):
    feedback = get_object_or_404(Feedback, pk=pk)
    if request.method == 'POST':
        feedback.delete()
        return redirect('feedback_list')
    return render(request, 'shipping/feedback_confirm_delete.html', {'feedback': feedback})

