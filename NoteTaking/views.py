from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .models import Note

# Create your views here.


def Home(request):
    return render(request, 'home.html')


@login_required
def noteCreate(request):

    if request.method == 'POST':
        note_subject = request.POST['note_subject']
        note_details = request.POST['note_details']
        note = Note(user=request.user, note_sub=note_subject,
                    note_detail=note_details)
        note.save()
    return render(request, 'note_create.html')


@login_required
def noteView(request):
    note_list = Note.objects.filter(user=request.user)
    note_count = Note.objects.filter(user=request.user).count()
    return render(request, 'note_list.html', {'note_list': note_list, 'note_count': note_count})


def noteUpdate(request, id):
    if request.method == 'POST':
        updated_note_subject = request.POST['updated_note_subject']
        updated_note_details = request.POST['updated_note_details']
        note = Note(id=id, user=request.user,
                    note_sub=updated_note_subject, note_detail=updated_note_details)
        note.save()
        messages.info(request, message="Update Successful!!")
    note = Note.objects.get(id=id)
    return render(request, 'update.html', {'note': note})


def noteDelete(request, id):
    note = Note.objects.get(id=id)
    if request.method == 'POST':
        note.delete()
        return redirect('create_note:view')
    return render(request, 'note_delete.html')


def register(request):
    if request.method == "POST":
        user_name = request.POST['userName']
        email_id = request.POST['email_address']
        password1 = request.POST['typed_password']
        password2 = request.POST['re_typed_password']
        if User.objects.filter(username=user_name).exists():
            messages.info(
                request, message="User name already taken choose another!!")
        elif User.objects.filter(email=email_id).exists():
            messages.info(request, message="Email id already registered!!")
        elif password1 != password2:
            messages.info(request, message="Password did not match!!")
        else:
            user = User.objects.create_user(
                username=user_name, email=email_id, password=password1)
            user.save()
            return redirect('create_note:sign-in')
        return redirect('create_note:sign-up')
    else:
        return render(request, 'registration.html')


def loginView(request):
    if request.method == "POST":
        user_name = request.POST['userName']
        password = request.POST['typed_password']
        user = authenticate(username=user_name, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, message="Login Successful. Now You Can Create Your Note!!")
            return redirect('/')
        else:
            messages.info(request, message="Invalid Credentials!!")
            return redirect('create_note:sign-in')
    else:
        return render(request, 'login.html')


def logoutView(request):
    logout(request)
    return redirect("/")


def profileView(request):
    if request.user.is_authenticated:
        return render(request,'profile.html')
    else:
        return redirect('create_note:sign-in')

