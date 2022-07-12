from django.urls import path
from . import views

urlpatterns = [
    path('', views.AssignmentsListView.as_view(), name='assignments'),
    path('<int:pk>/edit', views.AssignmentsUpdateView.as_view(), name="assignments.edit"),
    path('<int:pk>/edit/lim', views.AssignmentInterpreterUpdateView.as_view(), name="assignments.limited_edit"),
    path('create', views.AssignmentCreateView.as_view(), name="assignments.create"),
    path('<int:pk>/delete', views.AssignmentDeleteclass.as_view(), name="assignments.delete"),
    path('login', views.LoginInterfaceView.as_view(), name='login'),
    path('logout', views.LogoutInterfaceView.as_view(), name='logout'),
    path('offers', views.AssignmentOffersView.as_view(), name='assignments.offers'),
    path('<int:pk>/<str:user>/<str:email>/accept', views.accept_assignment, name='assignments.accept'),
    path('<int:pk>/deny', views.deny_assignment, name='assignments.deny'),
    path('<int:pk>/<str:user>/<str:email>/offer', views.offer_assignment, name='offer.assignment'),
    path('home', views.HomePageView.as_view(), name='home'),
    path('register', views.SignupView.as_view(), name='interpreter.register'),
    path('export', views.export_excel, name='assignments.export'),
    path('add_company', views.CompanySignup.as_view(), name='company.register')

]