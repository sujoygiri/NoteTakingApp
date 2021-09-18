from django.urls import path
from . import views
app_name = 'create_note'
urlpatterns = [
    path('',views.Home,name='home'),
    path('create-note/',views.noteCreate,name='create'),
    path('note-view/',views.noteView,name='view'),
    path('profile/',views.profileView,name='profile'),
    path('note-update/<int:id>/',views.noteUpdate,name='update'),
    path('note-delete/<int:id>/',views.noteDelete,name='delete'),
    path('accounts/sign-up/',views.register,name='sign-up'),
    path('accounts/login/',views.loginView,name='sign-in'),
    path('accounts/sign-out/',views.logoutView,name='sign-out'),

]