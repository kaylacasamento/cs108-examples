from django.shortcuts import render

# Create your views here.

from .models import Profile, StatusMessage
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CreateProfileForm, UpdateProfileForm, CreateStatusMessageForm
from django.shortcuts import redirect
from django.urls import reverse

class ShowAllProfilesView(ListView):
    '''Create a subclass of ListView to display all profiles.'''

    model = Profile # retrieve objects of type Facebook from the database
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profile_list'

class ShowProfilePageView(DetailView):
    '''Create a class-based view to obtain data for one Profile record'''
    model = Profile
    template_name = 'mini_fb/show_profile_page.html'
    context_object_name = 'show_profile_page'

    def get_context_data(self, **kwargs):
        '''Return the context data (a dictionary) to be used in the template.'''

        # obtain the default context data (a dictionary) from the superclass;
        # this will include the Profile record for this page view
        context = super(ShowProfilePageView, self).get_context_data(**kwargs)
        # create a new CreateStatusMessageForm, and add it into the context dictionary
        form = CreateStatusMessageForm()
        context['create_status_form'] = form
        # return this context dictionary
        return context

class CreateProfileView(CreateView):
    '''A view to create a new profile.'''

    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

class UpdateProfileView(UpdateView):
    '''A view to update a profile and save it to the database.'''

    form_class = UpdateProfileForm
    template_name = 'mini_fb/update_profile_form.html'
    queryset = Profile.objects.all()

def create_status_message(request, pk):
        '''Process a form submission to post a new status message.'''
        # find the profile that matches the 'pk' in the URL
        profile = Profile.objects.get(pk=pk)
        form = CreateStatusMessageForm(request.POST or None, request.FILES or None)

        # if and only if we are processing a POST request, try to read the data
        if request.method == 'POST' or request.method == 'FILES':

            # read the data from this form submission
            message = request.POST['message']
            image_file = request.FILES.get('image')

            # save the new status message object to the database
            if message or image_file:

                sm = StatusMessage()
                sm.profile = profile
                sm.message = message
                image = form.save(commit=False)
                image.profile = profile
                image.save()
                
        return redirect(reverse('show_profile_page', kwargs={'pk':pk}))
                
class DeleteStatusMessageView(DeleteView):
    '''Delete a status message'''

    template_name = 'mini_fb/delete_status_form.html'
    queryset = StatusMessage.objects.all()

    def get_context_data(self, **kwargs):
        '''Override the get_context_data method'''
        context = super(DeleteStatusMessageView, self).get_context_data(**kwargs)
        st_msg = StatusMessage.objects.get(pk=self.kwargs['status_pk'])
        context['st_msg'] = st_msg
        return context

    def get_object(self):
        '''Read URL data values'''
        profile_pk = self.kwargs['profile_pk']
        status_pk = self.kwargs['status_pk']
        st_msg = StatusMessage.objects.get(pk=status_pk)
        return st_msg

    def get_success_url(self):
        '''Get success URL'''
        profile_pk = self.kwargs['profile_pk']
        # status_pk = self.kwargs['status_pk']
        # status = Profile.objects.filter(pk=status_pk).first()
        return reverse('show_profile_page', kwargs={'pk':profile_pk})