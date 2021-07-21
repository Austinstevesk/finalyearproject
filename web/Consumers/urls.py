from . import views

urlpatterns = [
	path('mygaslevels/', views.mygaslevels, name='mygaslevels')
]