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
    if not request.user.is_authenticated:
        return redirect('/accounts/login/')
    else:
        return redirect(reverse('accept'))  # Make sure 'accept' is NOT mapped to '/'

@login_required
def accept(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        summary = request.POST.get("summary", "")
        degree = request.POST.get("degree", "")
        school = request.POST.get("school", "")
        university = request.POST.get("university", "")
        previous_work = request.POST.get("previous_work", "")
        skills = request.POST.get("skills", "")

        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            degree=degree,
            school=school,
            university=university,
            previous_work=previous_work,
            skills=skills
        )
        profile.save()

        # Render to PDF
        html = render_to_string("pdf/resume.html", {"user_profile": profile})
        config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_CMD)
        pdf_data = pdfkit.from_string(html, False, configuration=config)

        # Email PDF
        email_msg = EmailMessage(
            subject="Your Resume PDF",
            body="Hi, please find your attached resume.",
            from_email=settings.EMAIL_HOST_USER,
            to=[email],
        )
        email_msg.attach(f"{name}_resume.pdf", pdf_data, "application/pdf")
        email_msg.send()

        return render(request, "pdf/submission_success.html")

    return render(request, "pdf/accept.html")


@login_required
def resume(request, id):
    user_profile = get_object_or_404(Profile, pk=id)

    html = render_to_string("pdf/resume.html", {"user_profile": user_profile})
    config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_CMD)
    pdf_data = pdfkit.from_string(html, False, configuration=config)

    # Email again
    email = EmailMessage(
        subject="Your Resume PDF",
        body="Hi, please find your attached resume.",
        from_email=settings.EMAIL_HOST_USER,
        to=[user_profile.email],
    )
    email.attach(f"{user_profile.name}_resume.pdf", pdf_data, "application/pdf")
    email.send()

    response = HttpResponse(pdf_data, content_type="application/pdf")
    response["Content-Disposition"] = f'inline; filename="{user_profile.name}_resume.pdf"'
    return response


@login_required
def list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/list.html', {'profiles': profiles})


def list(request):
    profiles = Profile.objects.all()
    return render(request,'pdf/list.html',{'profiles':profiles})




