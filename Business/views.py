from django.db.models import Q
from django.http import JsonResponse
from rest_framework.views import APIView
from Account_App.models import BusinessAccount
from .get_distance import get_distances  # Import the get_distances function from your module
from rest_framework import permissions
from Account_App.models import Review
from .serializers import ReviewSerializer
from rest_framework import generics
from django.db.models import Avg
from django.db.models import F, ExpressionWrapper, fields
from django.db.models.functions import Sqrt
from django.db.models import Value, CharField


class FindBusinessAccounts(APIView):
    def get(self, request):
        try:
            # Get parameters from the request
            latitude = float(request.GET.get('latitude'))
            longitude = float(request.GET.get('longitude'))
            max_range = float(request.GET.get('max_range'))
            cuisine_names = request.GET.getlist('cuisine_name')

            # Use the get_distances function to get distances to all business accounts
            source = F('latitude') + F('longitude')  # A placeholder to use in the annotate expression
            destination = ExpressionWrapper(
                Sqrt(
                    (F('latitude') - latitude) * (F('latitude') - latitude) +
                    (F('longitude') - longitude) * (F('longitude') - longitude)
                ) * 111.32,  # Convert to kilometers (approximate)
                output_field=fields.FloatField()
            )
            businesses = BusinessAccount.objects.all().annotate(distance=destination)

            # Filter business accounts within the specified range
            if max_range:
                businesses = businesses.filter(distance__lte=max_range)

            # Filter business accounts by cuisine names
            if cuisine_names:
                businesses = businesses.filter(cuisines__name__in=cuisine_names)

            # Calculate average ratings
            businesses = businesses.annotate(avg_rating=Avg('reviews__rating'))

            # Sort results based on average rating and distance
            businesses = businesses.order_by('-avg_rating', 'distance')

            # Serialize the results
            data = [{
                'business_name': business.business_name,
                'street_name': business.street_name,
                'locality': business.locality,
                'avg_rating': business.avg_rating,
                'distance': business.distance,
                # Include other fields you want to return
            } for business in businesses]

            return JsonResponse({'business_accounts': data})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]  # Ensure that only authenticated users can create reviews

    def perform_create(self, serializer):
        # Automatically associate the logged-in user with the review
        serializer.save(user_account=self.request.user)