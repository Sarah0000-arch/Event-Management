from django.shortcuts import render, redirect
from django.http import HttpResponse
from events.forms import EventModelForm, CategoryModelForm, ParticipantModelForm
from events.models import Event, Category, Participant
from datetime import date
from django.db.models import Count, Q
from django.contrib import messages

def dashboard(request):
    type = request.GET.get('type', 'all')
    counts = Event.objects.aggregate(
        total=Count('id', distinct=True),
        upcoming=Count('id', filter=Q(date__gt=date.today()), distinct=True),
        past=Count('id', filter=Q(date__lt=date.today()), distinct=True),
        today=Count('id', filter=Q(date=date.today()),distinct=True),
        participants=Count('participants', distinct=True)
    )

    base_query = Event.objects.select_related('category').prefetch_related('participants')
    if type == 'upcoming':
        events = base_query.filter(date__gt=date.today())
    elif type == 'past':
        events = base_query.filter(date__lt=date.today())
    elif type == 'total':
        events = base_query.all()
    else:
        events = base_query.filter(date=date.today())
    
    context = {
        "events": events,
        "counts": counts
    }
    return render(request, "events.html", context)


def create_event(request):
    event_form = EventModelForm()

    if request.method == "POST":
        event_form = EventModelForm(request.POST)
        if event_form.is_valid():
            event = event_form.save()
            messages.success(request, "Event Created Successfully")
            return redirect('create-event')

    context = {"event_form": event_form}
    return render(request, "forms/event_form.html", context)

def update_event(request, id):
    event = Event.objects.get(id=id)
    event_form = EventModelForm(instance=event)

    if request.method == "POST":
        event_form = EventModelForm(request.POST, instance=event)
        if event_form.is_valid():
            event_form.save()
            messages.success(request, "Event Updated Successfully")
            return redirect('update-event', id)

    context = {"event_form": event_form}
    return render(request, "forms/event_form.html", context)

def delete_event(request, id):
    if request.method == 'POST':
        event = Event.objects.get(id=id)
        event.delete()
        messages.success(request, "Event Deleted Successfully")
        return redirect('home')
    else:
        messages.error(request, "Something went wrong")
        return redirect('home')
    
def event_search(request):
    search = request.GET.get("s")
    events = Event.objects.filter(
        Q(name__icontains=search) | Q(location__icontains=search)
    )
    if search:
        messages.success(request, f"{events.count()} search results found.")
    counts = Event.objects.aggregate(
        total=Count('id',distinct=True),
        upcoming=Count('id', filter=Q(date__gt=date.today()),distinct=True),
        past=Count('id', filter=Q(date__lt=date.today()),distinct=True),
        participants=Count('participants', distinct=True)
    )
    context= {
        "events": events,
        "counts": counts
    }
    return render(request, "events.html", context)

def show_event(request, id):
    event = Event.objects.get(id=id)
    if not event:
        messages.error(request, "Something went wrong")
        return redirect('home')
    return render(request, 'show_event.html', {'event': event})
    
def participant_list(request):
    participants = Participant.objects.all()
    return render(request, 'participant_list.html', {'participants': participants})
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def create_category(request):
    category_form = CategoryModelForm()

    if request.method == "POST":
        category_form = CategoryModelForm(request.POST)
        if category_form.is_valid():
            category = category_form.save()
            messages.success(request, "Category Created Successfully")
            return redirect('create-category')

    context = {"category_form": category_form}
    return render(request, "forms/category_form.html", context)

def update_category(request, id):
    category = Category.objects.get(id=id)
    category_form = CategoryModelForm(instance=category)

    if request.method == "POST":
        category_form = CategoryModelForm(request.POST, instance=category)
        if category_form.is_valid():
            category_form.save()
            messages.success(request, "Category Updated Successfully")
            return redirect('update-category', id)

    context = {"category_form": category_form}
    return render(request, "forms/category_form.html", context)
def delete_category(request, id):
    if request.method == 'POST':
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request, "Category Deleted Successfully")
        return redirect('category-list')
    else:
        messages.error(request, "Something went wrong")
        return redirect('category-list')


def create_participant(request):
    participant_form = ParticipantModelForm()
    if request.method == "POST":
        participant_form = ParticipantModelForm(request.POST)
        if participant_form.is_valid():
            participant = participant_form.save()
        messages.success(request, "Participant Created Successfully")
        return redirect('create-participant')
    context = {"participant_form": participant_form}
    return render(request, 'forms/participant_form.html',context)

def update_participant(request, id):
    participant = Participant.objects.get(id=id)
    participant_form = ParticipantModelForm(instance=participant)

    if request.method == "POST":
        participant_form = ParticipantModelForm(request.POST, instance=participant)
        if participant_form.is_valid():
            participant_form.save()
            messages.success(request, "Participant Information Updated Successfully")
            return redirect('update-participant', id)

    context = {"participant_form": participant_form}
    return render(request, "forms/participant_form.html", context)

def delete_participant(request, id):
    if request.method == 'POST':
        participant = Participant.objects.get(id=id)
        participant.delete()
        messages.success(request, "Participant Deleted Successfully")
        return redirect('participant-list')
    else:
        messages.error(request, "Something went wrong")
        return redirect('participant-list')