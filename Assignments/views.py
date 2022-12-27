from ast import Delete
from code import compile_command
from datetime import datetime
from time import strftime, strptime
from django.shortcuts import render
from django.http import Http404, HttpRequest, HttpResponseRedirect, JsonResponse
from .models import Assignment, Company
from .forms import AssignmentForm, InterpreterForm, SignupInterpreterForm, CompanyForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
import xlwt
import datetime


class AssignmentsListView(LoginRequiredMixin, ListView):
    model = Assignment
    context_object_name = "assignments"
    template_name = "assignments/assignments_list.html"
    login_url = "/login"

    def get_context_data(self, **kwargs):
        context = super(AssignmentsListView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['companies'] = Company.objects.all()
        return context

    def get_queryset(self):
        queryset = Assignment.objects.all().order_by('-date')
        filter_date = self.request.GET.get('date')
        filter_company = self.request.GET.get('company')
        
        if filter_date is not None and filter_company is not None:
            queryset = queryset.filter(date__icontains=filter_date).filter(company=filter_company)
        elif filter_date is not None:
            queryset = queryset.filter(date__icontains=filter_date)
        elif filter_company is not None:
            queryset = queryset.filter(company=filter_company)
        return queryset

def export_excel(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="assignments_workbook.xls"'

    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Appointments')
    columns = ['Date', 'Company', 'Language', 'Patient', 'Po_num', 'Type', 'Hours', 'Hourly_rate', 'Miles',
                'Mileage_rate', 'Address', 'Flat_rate', 'Parking', 'Total']
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    for col_num in range(len(columns)):
        worksheet.write(0, col_num, columns[col_num], font_style)

    rows = Assignment.objects.all().order_by('company','-date').values_list('date', 'company', 'language', 'patient', 'po_num', 'type', 'hours', 'hourly_rate', 'miles',
                'mileage_rate', 'address', 'flat_rate', 'parking', 'total')
    font_style = xlwt.XFStyle()
    row_num = 0
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            if col_num == 0:
                worksheet.write(row_num, col_num, row[col_num].strftime("%m/%d/%Y %H:%M %p"), font_style)
            else:
                worksheet.write(row_num, col_num, row[col_num], font_style)

    workbook.save(response)
    return response



class AssignmentsUpdateView(UpdateView):
    model = Assignment
    success_url = ''
    template_name = 'assignments/assignment_form.html'
    form_class = AssignmentForm

    def get_success_url(self):
        return '/'

class AssignmentInterpreterUpdateView(UpdateView):
    model = Assignment
    success_url = ''
    form_class = InterpreterForm

    def get_success_url(self):
        return '/'

class AssignmentCreateView(CreateView):
    model = Assignment
    success_url = ''
    template_name = 'assignments/assignment_form.html'
    form_class = AssignmentForm

    def get_success_url(self):
        return '/'

class AssignmentDeleteclass(DeleteView):
    model = Assignment
    success_url = ''
    template_name = 'assignments/assignment_delete.html'

    def get_success_url(self):
        return '/'

class LoginInterfaceView(LoginView):
    template_name = 'assignments/login.html'

    def get_success_url(self):
        return '/'

class LogoutInterfaceView(LogoutView):
    def get_success_url(self):
        return '/login'

class AssignmentOffersView(LoginRequiredMixin, ListView):
    model = Assignment
    context_object_name = "assignments"
    template_name = "assignments/assignments_offers.html"
    login_url = "/login"

    def get_context_data(self, **kwargs):
        context = super(AssignmentOffersView, self).get_context_data(**kwargs)
        context['users'] = User.objects.all()
        context['companies'] = Company.objects.all()
        return context

class HomePageView(TemplateView):
    template_name = "assignments/home.html"

class SignupView(CreateView):
    form_class = SignupInterpreterForm
    template_name = 'assignments/register.html'
    #success_url = '/'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect('assignments')
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return '/'

class CompanySignup(CreateView):
    form_class = CompanyForm
    template_name = 'assignments/company_register.html'
    #success_url = '/'

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_superuser:
            return redirect('assignments')
        return super().get(request, *args, **kwargs)

    def get_success_url(self):
        return '/'

def accept_assignment(request, pk, user, email):
    assignment_object = Assignment.objects.get(pk=pk)
    assignment_object.interpreter = request.user.username
    assignment_object.offered_to = ''
    assignment_object.save()

    offer_date = assignment_object.date.strftime("%B %d, %Y")
    offer_patient = assignment_object.patient
    offer_address = assignment_object.address
    offer_pay = assignment_object.interpreter_payment

    send_mail(
        ("Appointment Authorization for " + str(offer_date)),
        ("Hi " + user + ",\nHere are the details for your upcoming appointment: \n" + offer_date + "\n" + offer_patient + "\n" + offer_address + 
        "\nIf you have any questions visit the vendor portal at: http://127.0.0.1:8000/ or reach out through email at ajhinterpretations@gmail.com" +
        "\n\n\n Thank You, \n AJH Interpretations LLC"),
        "ajhinterpretations@gmail.com",
        [email],
        fail_silently=False,
    )

    return HttpResponseRedirect("/offers")

def deny_assignment(request, pk):
    assignment_object = Assignment.objects.get(pk=pk)
    assignment_object.offered_to = assignment_object.offered_to.replace(request.user.username,"")
    assignment_object.save()
    print(request.user.username)
    print(assignment_object.offered_to)

    return HttpResponseRedirect("/offers")

def offer_assignment(request, pk, user, email):
    assignment_object = Assignment.objects.get(pk=pk)
    assignment_object.offered_to = assignment_object.offered_to + user
    assignment_object.save()
    print(assignment_object.offered_to + ": " + email)

    offer_date = assignment_object.date.strftime("%B %d, %Y")
    offer_patient = assignment_object.patient
    offer_address = assignment_object.address
    offer_pay = assignment_object.interpreter_payment
    send_mail(
        ("Appointment Request DOS: " + str(offer_date)),
        ("Hi " + user + ",\nAppointment Request for: \n" + offer_date + "\n" + offer_patient + "\n" + offer_address + 
        "\nFlat Rate: $" + str(offer_pay) + "\n\nClick the link below" +
        " to be transferred to the vendor portal to accept or deny the assignment.\nWe appreciate your timely response as " +
        "multiple vendors may have been notified. \n http://127.0.0.1:8000/ \n \n \n" +
        "Thank You, \n AJH Interpretations LLC"),
        "ajhinterpretations@gmail.com",
        [email],
        fail_silently=False,
    )
    return HttpResponseRedirect("/")





