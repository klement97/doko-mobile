from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DeleteView, UpdateView

from mobile.forms import EmailForm
from mobile.models import Email


def register(request):
    template_name = 'mobile/index.html'
    form_class = EmailForm

    form = form_class

    data = {
        'registered': True,
        'message': 'You have been subscribed successfully'
    }

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse(data=data)
        else:
            return JsonResponse(data=form.errors)
    else:
        return render(request, template_name)


def validate_email(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': Email.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = "Hey you have already been registered. Great!"
    else:
        data['success'] = "Email available"
    return JsonResponse(data)


def read(request):
    id = request.GET.get('id', None)
    email = Email.objects.get(id=id)
    email.is_read = True
    data = {
        'sent': True,
        'success': 'You have been successfully subscribed!',
        'error': 'Could not connect to the server. Check your internet please!'
    }

    return JsonResponse(data)


class ManagerPageView(LoginRequiredMixin, ListView):
    template_name = 'mobile/manager.html'
    model = Email

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['unread_emails'] = Email.objects.filter(is_read=False)
        context['emails'] = Email.objects.all()
        return context


class EmailDeleteView(LoginRequiredMixin, DeleteView):
    model = Email
    template_name = 'mobile/email_delete.html'
    success_url = reverse_lazy('manager')


class EmailUpdateView(LoginRequiredMixin, UpdateView):
    model = Email
    template_name = 'mobile/email_update.html'
    success_url = reverse_lazy('manager')
    form_class = EmailForm
