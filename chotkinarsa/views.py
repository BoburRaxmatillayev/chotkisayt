# from django.shortcuts import render
# from django.contrib import messages
# from .models import Bot,Project,Attachment

# def home_view(request):
#     bots = Bot.objects.all()
#     context = {"bots":bots}
#     projects = Project.objects.all()
#     context = {"projects":projects}
#     return render(request, "index.html" ,context=context)

from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse  # new
from .models import Bot, Project, Attachment,Contact
from .forms import ContactForm
from .bot import send_message

def home_view(request):
    # Fetch all Bot and Project objects from the database
    bots = Bot.objects.all()
    projects = Project.objects.all()
    attachments = Attachment.objects.all()
    if request.method == "GET":
        form = ContactForm()
    else:
        # contact = Contact.objects.all()
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone_number = form.cleaned_data["phone_number"]
            description = form.cleaned_data["description"]

            send_message(name,email,phone_number,description)
            form.save()
            form = ContactForm()
            messages.success(request, '🥳 Murojatingiz adminga yuborildi...') 
            return HttpResponseRedirect(reverse('home-page'))
        else:
            messages.error(request, 'Formani qaytadan to\'ldiring')
    # Combine the data into the context dictionary
    context = {
        "bots": bots,
        "projects": projects,
        "attachments":attachments,
        "form":form
    }
    
    # Render the template with the context
    return render(request, "index.html", context)
