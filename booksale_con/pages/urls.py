from django.urls import path
from pages.views import DiscoverView, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('discover.html', DiscoverView.as_view(), name="discover"),
]