from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "polls"
urlpatterns = [
    path("",views.IndexView.as_view(),name = "index"),
    path("<int:pk>/",views.DetailView.as_view(),name = "detail"),
    path("<int:pk>/results/",views.ResultsView.as_view(),name = "results"),
    path("<int:question_id>/vote/",views.vote,name = "vote"),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)