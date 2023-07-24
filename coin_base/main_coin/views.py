from django.views import View
from .forms import CurrencyForm
from django.http import HttpResponse
from django.shortcuts import render
import requests
import xml.etree.ElementTree as ET
from datetime import date


class СurrencyView(View):
    def get(self, request):
        form = CurrencyForm(request.GET)
        if form.is_valid():
            selected_date = form.cleaned_data['selected_date']
        else:
            selected_date = date.today()
        url = f"https://www.cbr.ru/scripts/XML_daily.asp?date_req={selected_date.strftime('%d/%m/%Y')}"
        payload = {}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            root = ET.fromstring(response.text)
            currencies_info = []
            for valute in root.findall('.//Valute'):
                Name = valute.find('Name').text
                Nominal = valute.find('Nominal').text
                Value = valute.find('Value').text
                # NumCode = valute.find('NumCode').text
                CharCode = valute.find('CharCode').text
                currency_info = (
                    f"{Name}<br>"
                    f"Номинал: {Nominal}<br>"
                    f"Курс: {Value} рублей<br>"
                    # f"NumCode: {NumCode}<br>"
                    f"CharCode: {CharCode}<br>"
                )
                currencies_info.append(currency_info)
            return render(request, 'currency.html', {'currencies': currencies_info, 'form': form})
        else:
            return HttpResponse(
                f"Failed to fetch data. Status code: {response.status_code}"
                )
