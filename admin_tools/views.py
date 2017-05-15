from datetime import date, timedelta

from django.http import HttpResponse
from django.shortcuts import render
from django.db import connections

from openpyxl import Workbook


def invoice_report(request):
    template_name = 'admin_tools/reports/invoices.html'
    return render(request, template_name, {'title': 'Invoices'})


def submit(request):
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=invoices.xlsx'
    wbk = Workbook()
    begin = request.POST.get('begin_date')
    begin_date = date(int(begin[0:4]), int(begin[5:7]),
                      int(begin[8:10]))
    end = request.POST.get('end_date')
    end_date = date(int(end[0:4]), int(end[5:7]),
                    int(end[8:10]))

    ws = wbk.active

    cursor = connections['default'].cursor()
    cursor.execute("SELECT InvoiceId, Customer.LastName, Customer.FirstName, InvoiceDate, BillingAddress, BillingCity, BillingState, BillingCountry, BillingPostalCode, Total \
                            FROM Invoice, Customer        \
                            WHERE Invoice.InvoiceDate >= %s                                       \
                            AND Invoice.InvoiceDate < %s                                        \
                            AND Invoice.CustomerID = Customer.CustomerID \
                            ORDER BY Invoice.Total desc", [begin_date, end_date + timedelta(days=1)])
    results = cursor.fetchall()
    titles = ['Invoice ID', 'Customer Last Name', 'Customer First Name', 'Invoice Date', 'Billing Address', 'Billing City', 'Billing State', 'Billing Country', 'Billing Postal Code', 'Total']
    ws.append(titles)
    for result in results:
        ws.append(result)

    wbk.save(response)
    return response


