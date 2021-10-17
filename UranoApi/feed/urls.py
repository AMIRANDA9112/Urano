from . import views
from django.urls import path
from .views import PublicationListView, PublicationCreateView, \
    PublicationUpdateView, PublicationDeleteView,\
    PublicationWCreateView, PublicationWUpdateView, PublicationWDeleteView, \
    PublicationICreateView, PublicationIUpdateView, PublicationIDeleteView, PublicationTagsView,\
    AddLike, AddDisLike



urlpatterns = [
    path('', PublicationListView.as_view(), name='home'),
    path('tags/<slug:tag_slug>/', PublicationTagsView.as_view(), name='publicationtags'),
    path('create/', PublicationCreateView.as_view(), name='publicationcreate'),
    path('publication/<int:pk>/update', PublicationUpdateView.as_view(), name='publicationupdate'),
    path('publication/<int:pk>/delete', PublicationDeleteView.as_view(), name='publicationdelete'),
    path('createw/', PublicationWCreateView.as_view(), name='publicationwcreate'),
    path('publicationw/<int:pk>/update', PublicationWUpdateView.as_view(), name='publicationwupdate'),
    path('publicationw/<int:pk>/delete', PublicationWDeleteView.as_view(), name='publicationwdelete'),
    path('createi/', PublicationICreateView.as_view(), name='publicationicreate'),
    path('publicationi/<int:pk>/update', PublicationIUpdateView.as_view(), name='publicationiupdate'),
    path('publicationi/<int:pk>/delete', PublicationIDeleteView.as_view(), name='publicationidelete'),
    path('publication/<int:pk>/like', AddLike.as_view(), name='like'),
    path('publication/<int:pk>/dislike', AddDisLike.as_view(), name='dislike'),


]
