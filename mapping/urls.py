from django.conf.urls import url
from mapping import views
urlpatterns=[
url(r'^$',views.index),
url(r'^onetoone/$',views.one2one),
url(r'^onetooneinsertoptions/$',views.one2oneinsertoptions),
url(r'^onetooneextractoptions/$',views.one2oneextractoptions),
url(r'^onetomany/$',views.one2many),
url(r'^onetomanyinsertoptions/$',views.one2manyinsertoptions),
url(r'^onetomanyextractoptions/$',views.one2manyextractoptions),
url(r'^manytomany/$',views.many2many),
url(r'^manytomany/requestNresponse/$',views.requestNresponse),
url(r'^manytomany/athletescript/$',views.athletescript),
url(r'^manytomanyinsertoptions/$',views.many2manyinsertoptions),
url(r'^manytomanyextractoptions/$',views.many2manyextractoptions),
url(r'^newathlete/$',views.newathlete),
url(r'^newgame/$',views.newgame),
url(r'^viewathlete/$',views.viewathlete),
url(r'^viewgame/$',views.viewgame),
url(r'^thisgameathlete/$',views.thisgameathlete),
url(r'^editgame/$',views.editgame),
url(r'^editathlete/$',views.editathlete),
url(r'^viewgamelist/$',views.viewgamelist),
url(r'^deletegame/([0-9]+)/$',views.deletegame),

url(r'^editgamelist/$',views.editgamelist),
url(r'^editthatgame/$',views.editthatgame),
url(r'^changegamedetail/$',views.changegamedetail),
url(r'^editathletelist/$',views.editathletelist),
url(r'^editthatathlete/$',views.editthatathlete),
url(r'^changeathletedetail/$',views.changeathletedetail),
url(r'^editgamebyurl/([0-9]+)/$',views.editgamebyurl),

]
