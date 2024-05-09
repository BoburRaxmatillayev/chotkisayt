# from django.shortcuts import render
# from django.contrib import messages
# from .models import Bot,Project,Attachment

# def home_view(request):
#     bots = Bot.objects.all()
#     context = {"bots":bots}
#     projects = Project.objects.all()
#     context = {"projects":projects}
#     return render(request, "index.html" ,context=context)

from django.shortcuts import render
from django.contrib import messages
from .models import Bot, Project, Attachment

def home_view(request):
    # Fetch all Bot and Project objects from the database
    bots = Bot.objects.all()
    projects = Project.objects.all()
    attachments = Attachment.objects.all()
    
    # Combine the data into the context dictionary
    context = {
        "bots": bots,
        "projects": projects,
        "attachments":attachments
    }
    
    # Render the template with the context
    return render(request, "index.html", context)
