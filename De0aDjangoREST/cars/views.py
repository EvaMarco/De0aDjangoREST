from rest_framework import filters, generics
from rest_framework.permissions import IsAuthenticated


from .models import Brand
from .paginations import SmallResultsSetPagination
from .serializers import BrandSerializer


class BrandListView(generics.ListAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
    pagination_class = SmallResultsSetPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, )
    search_fields = ('name', )
    ordering_fields = ('name', )


class BrandCreateView(generics.CreateAPIView):
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated, )


class BrandRetrieveView(generics.RetrieveAPIView):
    serializer_class = BrandSerializer
    permission_classes = ()
    queryset = Brand.objects.all()
    lookup_field = 'id'


class BrandUpdateView(generics.UpdateAPIView):
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Brand.objects.all()
    lookup_field = 'id'


class BrandDestroyView(generics.DestroyAPIView):
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated, )
    queryset = Brand.objects.all()
    lookup_field = 'id'
