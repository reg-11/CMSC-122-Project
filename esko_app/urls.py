from django.urls import path, include

from .views import (PostListView, PostDetailView,PostCreateView, PostUpdateView, 
	PostDeleteView, AddCommentView, HomeListView, PasswordsChangeView, TagIndexView)

from . import views

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'esko_app'
urlpatterns = [
	path('', views.index, name='index'),
	path('signup/', views.signup, name='signup'),
	path('login/', views.loginPage, name='login'),

	path('home/', views.home, name='home'),
	path('profile/', views.profile, name='profile'),

	path('category/', views.category, name='category'),
	path('search_tags/', views.search_tags, name='search_tags'),
	path('sell/', views.sell, name='sell'),

	path('profileOther/<username>/', views.profileOther, name='profile-other'),
	path('profileOtherComment/<username>/', views.profileOtherComment, name='profile-other-comment'),


	# path('home/', HomeListView.as_view(), name='home'),
	# path('profile/', PostListView.as_view(), name='profile'),
	path('about/', views.about, name='about'),
	path('logout/', views.logoutUser, name='logout'),

	path('password-reset/', 
		PasswordsChangeView.as_view(template_name='esko_app/password_reset.html'),
		name= 'password_reset'),	
	path('password-reset/done/', views.password_success, name= 'password_success'),
	
	
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
	path('profileSettings/', views.profileSettings, name='profileSettings'),
	path('like/<int:pk>/',views.LikeView, name='like_post'),
	# path('likeHome/',views.LikeViewHome, name='like_post_home'),
	path('post/<int:pk>/comment', AddCommentView.as_view(), name='add_comment'),

	path('tags/<slug:tag_slug>/', TagIndexView.as_view(), name='posts_by_tags'),
	# path('post/<int:pk>/report', ReportView.as_view(), name='report'),

]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)