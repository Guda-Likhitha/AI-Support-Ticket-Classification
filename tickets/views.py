from django.shortcuts import render,redirect

# Create your views here.
from .forms import TicketForm
from .models import Ticket

from .ml_utils import classify_ticket

def home(request):
    return render(request,'home.html')

def create_ticket(request):

    form = TicketForm()

    if request.method == 'POST':

        form = TicketForm(request.POST)

        if form.is_valid():

            ticket = form.save(commit=False)

            prediction = classify_ticket(
                ticket.description
            )

            ticket.category = prediction

            text = ticket.description.lower()

            if (
                'urgent' in text or
                'failed' in text or
                'crash' in text
            ):
                ticket.priority = "High"
            else:
                ticket.priority = "Low"

            ticket.save()

            return redirect('dashboard')

    context = {'form': form}

    return render(
        request,
        'create_ticket.html',
        context
    )

def dashboard(request):

    tickets = Ticket.objects.all()

    return render(
        request,
        'dashboard.html',
        {'tickets': tickets}
    )
