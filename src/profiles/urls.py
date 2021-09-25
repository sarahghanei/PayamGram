from django.urls import path

from profiles.views import ProfileDetailView, profiles_list_view, ProfileListView

app_name = 'profiles'

urlpatterns = [
    path('', profiles_list_view, name='all-profiles-view'),
    path('listclass/', ProfileListView.as_view(), name='all-profiles-view'),
    path('<slug>/', ProfileDetailView.as_view(), name='profile-detail-view'),

]
