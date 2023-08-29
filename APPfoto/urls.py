from django.urls import path
from . import views

app_name = "APPfoto"

urlpatterns = [
    path("", views.home_view, name="home"),
    path("ricerca/", views.search, name="cercaFoto"),
    path("ricerca/<str:sstring>/<str:where>", views.FotoRicercaView.as_view(), name="ricerca_risultati"),
    path("crea_foto/", views.CreateFotoView.as_view(), name="creafoto")

]