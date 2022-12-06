from django.shortcuts import reverse, render , redirect
from django.views.generic import (ListView, CreateView, DeleteView, UpdateView)
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from users.models import Patients, Doctors
from multiprocessing import context
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


# This decorator is used to ensure that a user can only visit a given page having logged in
# The decorator extends the functionality of the function profile
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # This saves the user that has been created
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' Your Account  has been created Successfully. Login to view the site {username} !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# This will ensure that one can only visit this page having logged in
@login_required
def profile(request):
    # The instance in this case populates the Update Post wuth initial details of the User.
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('profile')
    else:  
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)      
    context = {
            'u_form': u_form,
            'p_form' : p_form

    }
    return render(request, 'users/profile.html', context)


# ----------------------------------------------------------------------------------------------------------------------------
# Patients Views

class PatientsCreateView(CreateView):
    # it will act on the database table "Patients"
    model = Patients
    # It will require the following fields
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'username']
    # It will display the user creation form generated by the view on the "user_detail.html"
    template_name = 'users/user_detail.html'

    # The url to be redirected to after a new patient is successfully added
    def get_success_url(self):
        # redirect user back to the page displaying a list of courses
        return reverse('patients-list')

    # data is passed to the HTML/templates page in a context
    # override this method to get access to the context
    # and its data
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # add/create a new context variable called "table_title"
        # this variable can then be accessed on the template
        context['table_title'] = 'Add New Patient'
        return context


# The view to display the list of patients, it will inherit from the django built in ListView
# it will get its data from the Patients database table and display the data to the users_list.html
# page and data will be accessed on the page using the "object_list" variable object
class PatientsListView(ListView):
    model = Patients
    template_name = 'users/users_list.html'

    # overrides this method so as to add custom data to the context object that will be pushed to the
    # HTML page displaying the data
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Patients'
        context['objects_update'] = 'patients-update'
        context['objects_delete'] = 'patients-delete'
        return context


# The view to be used to delete a patient, it will accept the "pk" as the variable holding the user_id
# it will inherit from the django built in DeleteView, it will perform the operation on the Patients
# database table and will request a user to confirm the deletion operation on the confirm_delete.html
# It will finally state the url where a user is redirected after a successful deletion
class PatientsDeleteView(DeleteView):
    model = Patients
    success_url = '/users/patients'
    template_name = 'users/confirm_delete.html'

    # overrides this method so as to add custom data to the context object that will be pushed to the
    # HTML page displaying the data
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Patient'
        name = Patients.objects.get(pk=self.kwargs.get('pk')).get_full_name()
        context['message'] = f'Are you sure you want to delete the patient "{name}"'
        context['cancel_url'] = 'patients-list'
        return context


# This view will be used to update the patient details
class PatientsUpdateView(UpdateView):
    model = Patients
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'username']
    template_name = 'users/user_detail.html'

    def get_success_url(self):
        return reverse('patients-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Update Patient'
        return context


# Doctors Views
# -----------------------------------------------------------------------------------------------------------------------------------------

# The view to create a patient, it will inherit from the django built in CreateView
class DoctorsCreateView(CreateView):
    model = Doctors
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'username']
    template_name = 'users/user_detail.html'

    def get_success_url(self):
        return reverse('doctors-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Add New Doctor'
        return context

class DoctorsListView(ListView):
    model = Doctors
    template_name = 'users/users_list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Doctors'
        context['objects_update'] = 'doctors-update'
        context['objects_delete'] = 'doctors-delete'
        return context


class DoctorsDeleteView(DeleteView):
    model = Doctors
    template_name = 'users/confirm_delete.html'

    def get_success_url(self):
        return reverse('doctors-list')

    # overrides this method so as to add custom data to the context object that will be pushed to the
    # HTML page displaying the data
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['title'] = 'Delete Doctor'
        name = Doctors.objects.get(pk=self.kwargs.get('pk')).get_full_name()
        context['message'] = f'Are you sure you want to delete the doctor "{name}"'
        context['cancel_url'] = 'doctors-list'
        return context


class DoctorsUpdateView(UpdateView):
    model = Doctors
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'username']
    template_name = 'users/user_detail.html'

    def get_success_url(self):
        return reverse('doctors-list')

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['table_title'] = 'Update Doctor'
        return context
