
# from django.contrib import admin
#from django.urls import path,include
#from . import views
#urlpatterns = [
 #   path('', views.home, name='home'),
  #  path('home', views.home, name='home'),
   # path('signup', views.signup, name='signup'),
    #path('signin', views.signin, name='signin'),
  #  path('signout', views.signout, name='signout'),
   # path('temp', views.temp, name='temp'),
    #path('heap', views.heap, name='heap'),
    #path('trade', views.trade, name='trade'),

#]


from django.urls import path
from . import views
from django.http import HttpResponseRedirect




urlpatterns = [
    path('', views.home, name='home'), # Maps to the home view (likely your homepage)
    path('home', views.home, name='home'),      # Maps to the home view (alternative route)
    path('signup', views.signup, name='signup'),  # Maps to the signup view
    path('signin', views.signin, name='signin'),  # Maps to the signin view (login page)
    path('signout', views.signout, name='signout'),  # Maps to the signout view (logout action)
    path('temp', views.temp, name='temp'),      # Maps to the temp view (possibly a temporary page)
    path('heap', views.heap, name='heap'),      # Maps to the heap view (custom page)
    path('trade', views.trade, name='trade'),   # Maps to the trade view (custom page)
    path('wheat/', views.wheat, name='wheat'),
    path('paddy/', views.paddy, name='paddy'),
    path('barley/', views.barley, name='barley'),
    path('maize/', views.maize, name='maize'),
    path('millet/', views.millet, name='millet'),
    path('sorghum/', views.sorghum, name='sorghum'),
    path('flask/', lambda request: HttpResponseRedirect('http://127.0.0.1:5000'), name='flask_url'),

]
 




