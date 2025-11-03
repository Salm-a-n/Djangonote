from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import get_template
from .forms import CertificateForm
from io import BytesIO
from xhtml2pdf import pisa

def generate_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save()

            # Render certificate template
            template = get_template('certificate_pdf.html')
            html = template.render({'certificate': certificate})

            # Generate PDF
            buffer = BytesIO()
            pisa_status = pisa.CreatePDF(html, dest=buffer)

            if pisa_status.err:
                return HttpResponse('PDF creation error!')

            # Send email
            email = EmailMessage(
                subject='Your Course Completion Certificate',
                body=f"Hi {certificate.student_name},\n\nAttached is your certificate for completing {certificate.course_name} on {certificate.completion_date}.",
                to=[certificate.student_email]
            )
            email.attach('certificate.pdf', buffer.getvalue(), 'application/pdf')
            email.send()

            # Return PDF for download
            response = HttpResponse(buffer.getvalue(), content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{certificate.student_name}_certificate.pdf"'
            return response
    else:
        form = CertificateForm()
    return render(request, 'certificate_form.html', {'form': form})