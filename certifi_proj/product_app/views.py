# products/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
from io import BytesIO
from .models import Product
from .forms import ProductForm

# Add a new product
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'addproduct.html', {'form': form})

# Show all products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_details.html', {'products': products})

# Download all products as PDF
def download_all_products_pdf(request):
    products = Product.objects.all()
    template = get_template('product_pdf.html')
    html = template.render({'products': products})

    buffer = BytesIO()
    pisa_status = pisa.CreatePDF(html, dest=buffer)

    if pisa_status.err:
        return HttpResponse('PDF creation error!')

    response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="all_products.pdf"'
    return response

def send_all_products_email(request):
    products = Product.objects.all()
    html_content = render_to_string('all_products_email.html', {'products': products})

    email = EmailMessage(
        subject='All Product Details',
        body='Please find all product details below.',
        to=['owner@example.com'], 
    )
    email.content_subtype = 'html'
    email.body = html_content
    email.send()

    return HttpResponse("All product details sent via email!")