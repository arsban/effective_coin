from django.views import View
from django.http import HttpResponse


class СurrencyView(View):
    def get(self, request):
        # Логика для обработки GET-запроса
        return HttpResponse("Тут будет курс валют")

    # def post(self, request):
    #     # Логика для обработки POST-запроса
    #     return HttpResponse("POST-запрос получен")
