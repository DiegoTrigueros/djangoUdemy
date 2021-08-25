from watchlist_app.models import WatchList, StreamingPlatform, Review
from watchlist_app.api.serializers import (WatchListSerializer,
                                    StreamingPlatformSerializer, ReviewSerializer)
from rest_framework.response import Response
# from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework import mixins
from rest_framework import generics


class ReviewList(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)

        serializer.save(watchlist=watchlist)
# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


class WatchListAV(APIView):

    def get(self, request):
        WatchLists = WatchList.objects.all()
        serializer = WatchListSerializer(WatchLists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class WatchListDetailAV(APIView):

    def get(self, request, pk):
        try:
            Watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error': 'WatchList not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = WatchListSerializer(Watchlist)
        return Response(serializer.data)

    def put(self, request, pk):
        Watchlist = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(Watchlist, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        WatchList = WatchList.objects.get(pk=pk)
        WatchList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamingPlatformAV(APIView):
    def get(self, request):
        StreamingPlatforms = StreamingPlatform.objects.all()
        serializer = StreamingPlatformSerializer(StreamingPlatforms, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = StreamingPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class StreamingPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            StreamingPlatforms = StreamingPlatform.objects.get(pk=pk)
        except StreamingPlatform.DoesNotExist:
            return Response({'Error': 'WatchList not found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = StreamingPlatformSerializer(StreamingPlatforms)
        return Response(serializer.data)

    def put(self, request, pk):
        StreamingPlatforms = StramingPlatform.objects.get(pk=pk)
        serializer = StreamingPlatformSerializer(StreamingPlatforms, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        StreamingPlatforms = StramingPlatform.objects.get(pk=pk)
        StramingPlatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def movie_list(request):

#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_details(request, pk):

#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return Response({'Error': 'Movie not found'},status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
