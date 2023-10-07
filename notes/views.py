from django.shortcuts import get_object_or_404, render, redirect
from .models import Note, ChatConversation
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
import openai

def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})

def create_note(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Note.objects.create(user=request.user, title=title, content=content)
        return redirect('note_list')

    return render(request, 'notes/create_note.html')

def view_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, 'notes/note.html', {'note': note})

def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        note.title = title
        note.content = content
        note.save()
        return redirect('note_list')
    
    return render(request, 'notes/edit_note.html', {'note': note})

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    
    if request.method == 'POST':
        note.delete()
        return redirect('note_list')
    
    return render(request, 'notes/delete_note.html', {'note': note})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('note_list')
    else:
        form = RegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('note_list')
    else:
        form = AuthenticationForm()
    
    return render(request, 'registration/login.html', {'form': form})

openai.api_key = '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'

def chat_view(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=user_input,
            max_tokens=50,  # Adjust as needed
            stop=None,  # Customize stop words if needed
        )
        chat_response = response.choices[0].text

        conversation = ChatConversation(user_input=user_input, gpt_response=chat_response)
        conversation.save()
    else:
        user_input = ""
        chat_response = ""

    return render(request, 'notes/chat.html', {'user_input': user_input, 'chat_response': chat_response})