from . import views
from django.urls import path
from .views import PublicationListView, PublicationCreateView, \
    PublicationUpdateView, PublicationDeleteView,\
    PublicationWCreateView, PublicationWUpdateView, PublicationWDeleteView, \
    PublicationICreateView, PublicationIUpdateView, PublicationIDeleteView, PublicationTagsView,\
    AddLike, AddDisLike, PublicationDetail, PublicationWDetail, AddLikeW, AddDisLikeW, AddLikeC,\
    AddDisLikeC, CommentDeleteView, CommentEditView, CommentWEditView, CommentWDeleteView,\
    AddLikeCW, AddDisLikeCW




urlpatterns = [
    path('', PublicationListView.as_view(), name='home'),
    path('tags/<slug:tag_slug>/', PublicationTagsView.as_view(), name='publicationtags'),
    path('create/', PublicationCreateView.as_view(), name='publicationcreate'),
    path('publication/<int:pk>', PublicationDetail.as_view(), name='publicationdetail'),
    path('publication/<int:pk>/update', PublicationUpdateView.as_view(), name='publicationupdate'),
    path('publication/<int:pk>/delete', PublicationDeleteView.as_view(), name='publicationdelete'),
    path('createw/', PublicationWCreateView.as_view(), name='publicationwcreate'),
    path('publicationw/<int:pk>', PublicationWDetail.as_view(), name='publicationwdetail'),
    path('publicationw/<int:pk>/update', PublicationWUpdateView.as_view(), name='publicationwupdate'),
    path('publicationw/<int:pk>/delete', PublicationWDeleteView.as_view(), name='publicationwdelete'),
    path('createi/', PublicationICreateView.as_view(), name='publicationicreate'),
    path('publicationi/<int:pk>/update', PublicationIUpdateView.as_view(), name='publicationiupdate'),
    path('publicationi/<int:pk>/delete', PublicationIDeleteView.as_view(), name='publicationidelete'),
    path('publication/<int:post_pk>/comment/update/<int:pk>', CommentEditView.as_view(), name='commentupdate'),
    path('publication/<int:post_pk>/comment/delete/<int:pk>', CommentDeleteView.as_view(), name='commentdelete'),
    path('publication/<int:post_pk>/comment/update/<int:pk>', CommentWEditView.as_view(), name='commentwupdate'),
    path('publication/<int:post_pk>/comment/delete/<int:pk>', CommentWDeleteView.as_view(), name='commentwdelete'),
    path('publication/<int:pk>/like', AddLike.as_view(), name='like'),
    path('publication/<int:pk>/dislike', AddDisLike.as_view(), name='dislike'),
    path('publicationw/<int:pk>/likew', AddLikeW.as_view(), name='likew'),
    path('publicationw/<int:pk>/dislikew', AddDisLikeW.as_view(), name='dislikew'),
    path('publication/<int:post_pk>/comment/<int:pk>/likec', AddLikeC.as_view(), name='likec'),
    path('publication/<int:post_pk>/comment/<int:pk>/dislikec', AddDisLikeC.as_view(), name='dislikec'),
    path('publication/<int:post_pk>/comment/<int:pk>/likecw', AddLikeCW.as_view(), name='likecw'),
    path('publication/<int:post_pk>/comment/<int:pk>/dislikecw', AddDisLikeCW.as_view(), name='dislikecw'),

]
