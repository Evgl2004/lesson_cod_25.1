from rest_framework import serializers

from vehicle.models import Car, Moto, Mileage


class MileageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mileage
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    last_mileage = serializers.IntegerField(source='mileage.all.first.mileage', read_only=True)
    mileage = MileageSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = '__all__'


class MotoSerializer(serializers.ModelSerializer):
    last_mileage = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_mileage(self, instance):
        if instance.mileage.all().first():
            return instance.mileage.all().first().mileage
        return 0


class MotoMileageSerializer(serializers.ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Mileage
        fields = ('id', 'mileage', 'year', 'moto')


class MotoCreateSerializer(serializers.ModelSerializer):
    mileage = MileageSerializer(many=True)

    class Meta:
        model = Moto
        fields = '__all__'

    def create(self, validated_data):
        mileages = validated_data.pop('mileage')

        moto_item = Moto.objects.create(**validated_data)

        for mileage in mileages:
            Mileage.objects.create(**mileage, moto=moto_item)

        return moto_item
