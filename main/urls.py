from django.urls import path
from .import views
urlpatterns=[




path("",views.home, name="home"),




path("home",views.home ,name="home"),
path("demon_slayer",views.demon_slayer,name="demon_slayer"),
path("demon_slayer_sc",views.demon_slayer_sc,name="demon_slayer_sc"),
path("demon_slayer_chr",views.demon_slayer_chr,name="demon_slayer_chr")
]


