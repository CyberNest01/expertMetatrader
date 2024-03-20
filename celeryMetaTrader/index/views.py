from django.shortcuts import render
from django.http import JsonResponse
from celeryMetaTrader.index.form import CreateConfigUser
from config.models import UserConfig
from services.controler import MetaTraderControler
from rest_framework.decorators import api_view
from rest_framework.response import Response



def index(request):
    if request.method == 'POST':
        form = CreateConfigUser(request.POST)
        if form.is_valid():
            info = form.save()
            info.save()
            return JsonResponse({'status': True, 'message': 'done'})
    return render(request, 'index.html')


@api_view(['GET'])
def get_order_history(request, account):
    context = {
        'status': False,
        'message': 'Not Found',
        'data': None
    }
    config = UserConfig.get_configs_by_account_id(account)
    if config:
        data = MetaTraderControler(
            int(config.account),
            config.password,
            config.server,
            config.file_name
        ).orders()
        if data['status']:
            context.update(data)
    return Response(context)
