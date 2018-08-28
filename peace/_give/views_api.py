from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from .models import *
import json

@login_required
@require_http_methods(["POST"])
def CreateItemPostAPI(request):
    images = request.POST.get('images', None)
    type_item = request.POST.get('type_item', None)
    state_item = request.POST.get('state_item', None)
    location = request.POST.get('location', None)
    title = request.POST.get('title', None)
    cost = request.POST.get('cost', None)
    contents = request.POST.get('contents', None)
    amount = request.POST.get('amount', None)
    tags = request.POST.get('tags', None).split(",")

    try:

        ItemPostModel = ItemPostModel.objects.create(
            user=request.user,
            images=images,
            type_item=type_item,
            state_item=state_item,
            location=location,
            title=title,
            cost=int(cost),
            contents=contents,
            amount=int(amount),
            tags=tags.distinct(),
        )

        print('프로젝트 생성')

    except:
        message = 'error'

    context = { 'message': message }
    return HttpResponse(json.dumps(context), content_type="application/json")
