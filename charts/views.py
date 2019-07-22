from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from datetime import timedelta
from posts.models import Post, Voter

### Summary Charts ###
# Renders page with all data in database in json format
def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    
    return JsonResponse(data)
    
class ChartData(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        labels = ['Day', 'Week', 'Month']
        default_items = [Post.objects.filter(type="Feature Request", status="Doing", published_date__gte=timezone.now()-timedelta(30)).count() / 30,
                        Post.objects.filter(type="Feature Request", status="Doing", published_date__gte=timezone.now()-timedelta(28)).count() / 4,
                        Post.objects.filter(type="Feature Request", status="Doing", published_date__gte=timezone.now()-timedelta(30)).count()]
        default_items2 = [Post.objects.filter(type="Bug", status="Doing", published_date__gte=timezone.now()-timedelta(30)).count() / 30,
                        Post.objects.filter(type="Bug", status="Doing", published_date__gte=timezone.now()-timedelta(28)).count() / 4,
                        Post.objects.filter(type="Bug", status="Doing", published_date__gte=timezone.now()-timedelta(30)).count()]
        data = {
            "labels": labels,
            "default": default_items,
        }
        data2 = {
            "labels": labels,
            "default": default_items2,
        }
        return Response(data)

# Renders page with summary charts
def charts(request):
    return render(request, 'charts.html')