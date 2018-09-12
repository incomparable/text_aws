from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from .models import Doctor, Patient
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMessage
from smtplib import SMTPException
from time import gmtime, strftime
# Create your views here.


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'anaconda.wb@gmail.com'
EMAIL_HOST_PASSWORD = 'ameo@anaconda'
EMAIL_PORT = 587


def home(request):
    # doctor = Doctor.objects.all()
    return render(request, 'index.html')


def doctor(request):
    doctor = Doctor.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        specification = request.POST.get('specification')
        cabin = request.POST.get('cabin')
        birth_date = request.POST.get('birth_date')
        contact = request.POST.get('contact')
        created_at = strftime("%Y-%m-%d", gmtime())
        
        Add_new_doctor = Doctor(d_name=name,
                                d_age=age,
                                email=email,
                                specification=specification,
                                birth_date=birth_date,
                                created_at=created_at,
                                contact=contact,
                                cabin_no=cabin)
        Add_new_doctor.save()

        cc_email = 'gauravkumarall@gmail.com'
        body_text = 'Welcome to XYZ Hospital'
        send_emails(request, name, email, body_text, cc_email)
        

        messages.add_message(request, messages.SUCCESS, 'Added new doctor!')

    return render(request, 'doctor.html', {'doctor': doctor})


def get_doctor(request, id):
    data = Doctor.objects.get(id=id)

    response_data = {}

    id = data.id
    d_name = data.d_name
    d_age = data.d_age
    email = data.email
    specification = data.specification
    cabin_no = data.cabin_no
    birth_date = data.birth_date
    contact = data.contact

    response_data['id'] = id
    response_data['d_name'] = d_name
    response_data['d_age'] = d_age
    response_data['email'] = email

    response_data['specification'] = specification
    response_data['cabin_no'] = cabin_no
    response_data['birth_date'] = birth_date
    response_data['contact'] = contact
    return JsonResponse(response_data, safe=True)


def delete_doctor(request, id):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    messages.add_message(request, messages.SUCCESS, 'Successfully delete!')
    return redirect("/app/Doctor")


def patient(request):
    patient = Patient.objects.all()
    doctor = Doctor.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        place = request.POST.get('place')
        problem = request.POST.get('problem')
        birth_date = request.POST.get('birth_date')
        contact = request.POST.get('contact')
        doctor_id = request.POST.get('doctor_id')

        doctor_data = Doctor.objects.filter(id=doctor_id).first()
        doctor_name = doctor_data.d_name
        cabin_no = doctor_data.cabin_no
        d_contact = doctor_data.contact
        created_at = strftime("%Y-%m-%d", gmtime())

        Add_new_patient = Patient( p_name=name, p_age=age, email=email, 
            place=place, problem=problem, birth_date=birth_date, contact=contact, 
            Doctor_name=doctor_name, cabin_no=cabin_no, d_contact=d_contact, created_at=created_at)
        Add_new_patient.save()

        cc_email = 'gauravkumarall@gmail.com'
        body_text = 'Welcome to XYZ Hospital'
        send_emails(request, name, email, body_text, cc_email)

        messages.add_message(request, messages.SUCCESS, 'Added new patient please check your email!')

    return render(request, 'patient.html', {"patient": patient, 'doctor':doctor})


def get_patient(request, id):
    data = Patient.objects.get(id=id)

    response_data = {}

    id = data.id
    d_id = data.d_id
    print('............................',id)
    # doctor_data = Doctor.objects.filter(d_id=d_id).first()
    # doctor_id = doctor_data.id

    p_name = data.p_name
    p_age = data.p_age
    email = data.email
    place = data.specification
    problem = data.cabin_no
    birth_date = data.birth_date
    Doctor_name = data.Doctor_name
    cabin_no = data.cabin_no
    contact = data.contact
    doc_id = data.doctor_id

    response_data['id'] = id
    response_data['p_name'] = p_name
    response_data['p_age'] = p_age
    response_data['email'] = email

    response_data['place'] = place
    response_data['problem'] = problem
    response_data['birth_date'] = birth_date
    response_data['Doctor_name'] = Doctor_name

    response_data['cabin_no'] = cabin_no
    response_data['contact'] = contact
    response_data['doc_id'] = doc_id
    return JsonResponse(response_data, safe=True)


def delete_patient(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    messages.add_message(request, messages.SUCCESS, 'Successfully delete!')
    return redirect("/app/Patient")


def update_doctor(request):
    try:
        data = json.loads(request.POST.get("data"))
        if data:
            for item in data:
                id = item.get('id', None)
                name = item.get('name', None)
                age = item.get('age', None)
                email = item.get('email', None)
                specification = item.get('specification', None)
                cabin = item.get('cabin', None)
                birth_date = item.get('birth_date', None)
                contact = item.get('contact', None)

                data = Doctor.objects.get(id=id)
                data.d_name = name
                data.d_age=age
                data.email=email
                data.specification=specification
                data.cabin_no=cabin
                data.birth_date=birth_date
                data.contact=contact
                data.save()
        else:
            pass
    except:
        return None
    return render(request, 'doctor.html', {'doctor': doctor})


def send_email(request):
    doctor = Doctor.objects.all()
    if request.POST:
        try:
            cc_email = request.POST.get('to_email')
            body_text = request.POST.get('body_text')
            email = request.POST.get('email')
            name = 'Doctor/Patient'
            send_emails(request, name, email, body_text, cc_email)
            messages.add_message(request, messages.SUCCESS, 'Email has been sent.')
        except SMTPException as e:
            print('There was an error sending an email: ', e)
        return redirect("/app/Doctor/")
    return render(request, 'email.html', {'doctor': doctor})



def send_emails(request, name, email, body_text, cc_email):
    print(email)
    email_data = EmailMessage(
        'XYZ | Welcome %s'%name.capitalize(),
        body_text,
        'anaconda.wb@gmail.com',
        [email],
        [cc_email],
        reply_to=['kgaurav.ameotech@gmail.com'],
        headers={'XYZ': 'Hospital'},
        )
    email_data.content_subtype = "html"
    return email_data.send(fail_silently=True)