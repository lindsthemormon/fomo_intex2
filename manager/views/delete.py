from django.http import HttpResponseRedirect
from django_mako_plus import view_function
from catalog import models as cmod
from django.views.generic.edit import DeleteView
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
@view_function
def process_request(request, product:cmod.Product):
    # try:
    #     product = cmod.Product.objects.get(id=request.urlparams[0])
    # except cmod.Product.DoesNotExist:
    #     return HttpResponseRedirect('/')

    product.status = 'I'
    product.save()

    productList = cmod.Product.objects.filter(status='A')

    context={
            'productList': productList
    }

    return request.dmp.render('products.html', context)
