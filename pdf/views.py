import os
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from resume_generator import settings
from .models import Profile
import pdfkit


def home_redirect(request):
    # This is your `/` route — it will redirect to Google login if not logged in
    if not request.user.is_authenticated:
        return redirect('/accounts/google/login/')  # 🔗 Go to Google login directly
    return redirect('accept')  # ✅ After login, go to resume form


@login_required
def accept(request):
    # This is your form view (POST + GET)
    if request.method == "POST":
        data = {
            "name": request.POST.get("name", ""),
            "email": request.POST.get("email", ""),
            "phone": request.POST.get("phone", ""),
            "summary": request.POST.get("summary", ""),
            "degree": request.POST.get("degree", ""),
            "school": request.POST.get("school", ""),
            "university": request.POST.get("university", ""),
            "previous_work": request.POST.get("previous_work", ""),
            "skills": request.POST.get("skills", "")
        }

        profile = Profile(**data)
        profile.save()

        try:
            html = render_to_string("pdf/resume.html", {"user_profile": profile})
            config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_CMD)
            pdf_data = pdfkit.from_string(html, False, configuration=config)

            email_msg = EmailMessage(
                subject="Your Resume PDF",
                body="Hi, please find your attached resume.",
                from_email=settings.EMAIL_HOST_USER,
                to=[data['email']],
            )
            email_msg.attach(f"{data['name']}_resume.pdf", pdf_data, "application/pdf")
            email_msg.send()

        except Exception as e:
            return render(request, "pdf/error.html", {"error": str(e)})

        return render(request, "pdf/submission_success.html")

    return render(request, "pdf/accept.html")


@login_required
def download_resume(request, id):
    profile = get_object_or_404(Profile, pk=id)

    try:
        html = render_to_string("pdf/resume.html", {"user_profile": profile})
        config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_CMD)
        pdf_data = pdfkit.from_string(html, False, configuration=config)

        email = EmailMessage(
            subject="Your Resume PDF",
            body="Hi, please find your attached resume.",
            from_email=settings.EMAIL_HOST_USER,
            to=[profile.email],
        )
        email.attach(f"{profile.name}_resume.pdf", pdf_data, "application/pdf")
        email.send()

        response = HttpResponse(pdf_data, content_type="application/pdf")
        response["Content-Disposition"] = f'inline; filename="{profile.name}_resume.pdf"'
        return response

    except Exception as e:
        return render(request, "pdf/error.html", {"error": str(e)})


@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles': profiles})
