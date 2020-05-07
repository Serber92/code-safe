from django.urls import path
from . import views

urlpatterns = [
  path('', views.login),
  path('login', views.login),
  path('signup', views.signup),
  path('signup_processing', views.signup_processing),
  path('login_processing', views.login_processing),
  path('dashboard', views.dashboard),
  path('create', views.create),
  path('create_processing', views.create_processing),
  path('edit/<int:id>', views.edit),
  path('edit_processing/<int:id>', views.edit_processing),
  path('logout', views.logout),
  path('users', views.users),
  path('bugs_ideas', views.bugs_ideas),
  path('bugs_ideads_processing', views.bugs_ideads_processing),
  path('bugs_ideads_comment_processing/<int:id>', views.bugs_ideads_comment_processing),
]