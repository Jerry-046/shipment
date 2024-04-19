from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required,permission_required
from .forms import FeedbackForm,FromForm,ToForm
from .models import Feedback,Shipment
from  django.contrib.auth.models import User

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

@login_required
def from_form(request):
    if request.method == 'POST':
        form = FromForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.user = request.user  # Set the owner of the shipment
            shipment.save()
            return redirect('to_form', shipment_id=shipment.id)
    else:
        form = FromForm()
    return render(request, 'shipping/from_form.html', {'form': form})

@login_required
def to_form(request, shipment_id):
    shipment = get_object_or_404(Shipment, id=shipment_id)
    if request.user == shipment.user or request.user.is_superuser:
        if request.method == 'POST':
            form = ToForm(request.POST, instance=shipment)
            if form.is_valid():
                form.save()
                return redirect('shipment_list')
        else:
            form = ToForm(instance=shipment)
        return render(request, 'shipping/to_form.html', {'form': form})
    else:
        return redirect('shipment_list')

@login_required
def shipment_list(request):
    if request.user.is_superuser:
        shipments = Shipment.objects.all()
    else:
        shipments = Shipment.objects.filter(user=request.user)
    return render(request, 'shipping/shipment_list.html', {'shipments': shipments})

@login_required
def shipment_detail(request, shipment_id):
    shipment = get_object_or_404(Shipment, id=shipment_id)
    if request.user == shipment.user or request.user.is_superuser:
        userd={'user_firstname': shipment.user.first_name,'user_lastname':shipment.user.last_name,'user_email':shipment.user.email}
        return render(request, 'shipping/shipment_detail.html', {'shipment': shipment,'userdetails':userd})
    else:
        return redirect('shipment_list')

@login_required
def update_shipment(request, shipment_id):
    shipment = get_object_or_404(Shipment, id=shipment_id)
    if request.user == shipment.user or request.user.is_superuser:
        if request.method == 'POST':
            form = ToForm(request.POST, instance=shipment)
            if form.is_valid():
                form.save()
                return redirect('shipment_detail', shipment_id=shipment.id)
        else:
            form = ToForm(instance=shipment)
        return render(request, 'shipping/update_shipment.html', {'form': form, 'shipment': shipment})
    else:
        return redirect('shipment_list')

@login_required
def delete_shipment(request, shipment_id):
    shipment = get_object_or_404(Shipment, id=shipment_id)
    if request.user == shipment.user or request.user.is_superuser:
        if request.method == 'POST':
            shipment.delete()
            return redirect('shipment_list')
        return render(request, 'shipping/delete_shipment.html', {'shipment': shipment})
    else:
        return redirect('shipment_list')