from django.shortcuts import render
from .models import FeedbackData,ContactData,CoursesData
from .forms import FeedbackForm,contactForm
from django.http.response import HttpResponse
import datetime

date=datetime.datetime.now()


def main_page(request):
    return render(request, 'base.html')


def home_page(request):
    return render(request, 'home_page.html')


def contact_page(request):
        if request.method == "POST":
            eform = contactForm(request.POST)
            if eform.is_valid():
                name = request.POST.get('name', '')
                mobile = request.POST.get('mobile', '')
                email = request.POST.get('email', '')
                courses = eform.cleaned_data.get('courses', '')
                locations = eform.cleaned_data.get('locations', '')
                shifts = eform.cleaned_data.get('shifts', '')
                gender = eform.cleaned_data.get('gender', '')
                batch_start_date = eform.cleaned_data.get('batch_start_date', '')

                data = ContactData(
                    name=name,
                    mobile=mobile,
                    email=email,
                    courses=courses,
                    locations=locations,
                    shifts=shifts,
                    gender=gender,
                    batch_start_date=batch_start_date
                )
                data.save()
                cform = contactForm()
                return render(request, 'contact_page.html', {'cform': cform})
        else:
            cform = contactForm()
            return render(request, 'contact_page.html', {'cform': cform})

        return render(request, 'contact_page.html')


def courses_page(request):
    courses=CoursesData.objects.all()
    return render (request,'courses_page.html',{'courses':courses})


def feedback_page(request):
    if request.method == 'POST':
        fform = FeedbackForm(request.POST)
        if fform.is_valid():
            name = request.POST.get('name', '')
            rating = request.POST.get('rating', '')
            feedback = request.POST.get('feedback', '')

            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date,
            )
            data.save()
            fform = FeedbackForm()
            fdata = FeedbackData.objects.all()
            return render(request, 'feedback_page.html', {'fform': fform, 'fdata': fdata})
        else:
            return HttpResponse("Invalid")
    else:
        fdata = FeedbackData.objects.all()
        fform = FeedbackForm()
        return render(request, 'feedback_page.html', {'fform': fform, 'fdata': fdata})


def team_page(request):
    return render(request, 'team_page.html')


def gallery_page(request):
    return render(request, 'gallery_page.html')














