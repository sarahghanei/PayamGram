from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from profiles.models import Profile, Relationship


@login_required
def profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)

    context = {'qs': qs}

    return render(request, 'profiles/profile_list.html', context)


class ProfileListView(LoginRequiredMixin, ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'

    # context_object_name = 'qs'

    def get_queryset(self):
        qs = Profile.objects.get_all_profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        context['is_empty'] = False
        if len(self.get_queryset()) == 0:
            context['is_empty'] = True

        return context



    class ProfileListView(LoginRequiredMixin, ListView):
        model = Profile
        template_name = 'profiles/profile_list.html'

        # context_object_name = 'qs'

        def get_queryset(self):
            qs = Profile.objects.get_all_profiles(self.request.user)
            return qs

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user = User.objects.get(username__iexact=self.request.user)
            profile = Profile.objects.get(user=user)
            rel_r = Relationship.objects.filter(sender=profile)
            rel_s = Relationship.objects.filter(receiver=profile)
            rel_receiver = []
            rel_sender = []
            for item in rel_r:
                rel_receiver.append(item.receiver.user)
            for item in rel_s:
                rel_sender.append(item.sender.user)
            context["rel_receiver"] = rel_receiver
            context["rel_sender"] = rel_sender
            context['is_empty'] = False
            if len(self.get_queryset()) == 0:
                context['is_empty'] = True

            return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = Profile.objects.get(user=user)
        rel_r = Relationship.objects.filter(sender=profile)
        rel_s = Relationship.objects.filter(receiver=profile)
        rel_receiver = []
        rel_sender = []
        for item in rel_r:
            rel_receiver.append(item.receiver.user)
        for item in rel_s:
            rel_sender.append(item.sender.user)
        context["rel_receiver"] = rel_receiver
        context["rel_sender"] = rel_sender
        context['posts'] = self.get_object().get_all_authors_posts()
        context['len_posts'] = True if len(self.get_object().get_all_authors_posts()) > 0 else False
        return context
