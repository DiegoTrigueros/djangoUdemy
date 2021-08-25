from django.urls import path, include
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchListDetailAV,
                                StreamingPlatformAV, StreamingPlatformDetailAV, ReviewDetail, ReviewList,
                                ReviewCreate)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('platforms/', StreamingPlatformAV.as_view(), name='streaming-platform'),
    path('<int:pk>', WatchListDetailAV.as_view(), name='movie-details'),

    path('platforms/<int:pk', StreamingPlatformDetailAV.as_view(), name='streaming-details'),
    
    path('platforms/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('platforms/<int:pk>/review', ReviewList.as_view(), name='review-list'),
    path('platforms/review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]
