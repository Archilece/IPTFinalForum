from django.urls import path
from . import views

app_name = 'forums'
urlpatterns = [
    path('forums/', views.forums_list, name='list'),
    path('forums/<int:forum_id>/', views.forums_detail, name='detail'),
    path('forums/<int:forum_id>/create_topic/', views.create_topic, name='create_topic'),
    # path('forums/<int:forum_id>/topics/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('forums/<int:forum_id>/topics/<int:topic_id>/add_comment/', views.add_comment, name='add_comment'),
    # path('<int:forum_id>/topics/<int:topic_id>/add_comment/', views.add_comment, name='add_comment'),


    ####USERLOG
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('logout/', views.logout_view, name="logout"), 


]
