from django.contrib import admin
from django.urls import path
from pinkbud import views
from pinkbud import login_views
from pinkbud import sign_up_views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('posts/',views.post_list),
    path('posts/<int:id>',views.posts_detail),
    path('login/',login_views.login, name = 'login'),
    path('users/',sign_up_views.user_sign_up),
    path('therapists/',sign_up_views.therapist_sign_up),
    path('lawyers/',sign_up_views.lawyer_sign_up),
    path('ngos/',sign_up_views.ngo_sign_up),

]
