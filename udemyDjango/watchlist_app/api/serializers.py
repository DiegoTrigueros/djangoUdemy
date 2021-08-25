from rest_framework import serializers
from watchlist_app.models import WatchList, StreamingPlatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = '__all__'
        exclude = ["watchlist"]


class WatchListSerializer(serializers.ModelSerializer):
    # len_name = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = WatchList
        fields = '__all__'
        # fields = ['id', 'name', 'description']
        # exclude = ['active']
    
class StreamingPlatformSerializer(serializers.ModelSerializer):
    # Nested serializer
    watchlist = WatchListSerializer(many=True, read_only=True)
    # watchlist = serializers.StringRelatedField(many=True)
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # watchlist = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='movie-details')

    class Meta:
        model = StreamingPlatform
        fields = '__all__'
    # def get_len_name(self, object):
    #     lenght = len(object.name)
    #     return lenght

    # def validate_name(self, value):

    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short")
    #     else:
    #         return value

    # def validate(self, data):
    #     if data["name"] == data["description"]:
    #         raise serializers.ValidationError("Description and Title must be different")
        
    #     return value

# def name_lenght(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Name is too short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_lenght])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     # def validate_name(self, value):

#     #     if len(value) < 2:
#     #         raise serializers.ValidationError("Name is too short")
#     #     else:
#     #         return value

#     def validate(self, data):
#         if data["name"] == data["description"]:
#             raise serializers.ValidationError("Description and Title must be different")
        
#         return value