from django.core.mail import send_mail
from jobportal.settings import EMAIL_HOST_USER
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import *
from .forms import *

# Create your views here



def index(request):
    return render(request,'index.html')

def Login(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            em=a.cleaned_data['email']
            ps=a.cleaned_data['password']
            b=regmodel.objects.all()
            for i in b:
                cmp=i.company
                request.session['company']=cmp
                id=i.id
                if i.email==em and i.password==ps:
                    return render(request,'profile.html',{'cmp':cmp,'id':id})
            else:
                    return HttpResponse("LOGIN FAILED")
    else:
        return render(request,'login.html')

def Register(request):
    if request.method == 'POST':
        a=regform(request.POST)
        if a.is_valid():
            cm=a.cleaned_data['company']
            em=a.cleaned_data['email']
            ad=a.cleaned_data['address']
            ph=a.cleaned_data['phone']
            ps=a.cleaned_data['password']
            cp=a.cleaned_data['cpassword']

            if ps==cp:
                b=regmodel(company=cm,email=em,address=ad,phone=ph,password=ps)
                b.save()
                return redirect(Login)
            else:
                return HttpResponse("INCORRECT PASSWORD")

        else:
            return HttpResponse("COMPANY REGISTRATION FAILED...")

    else:
        return render(request,'registration.html')

# navbar

def profile(request):
    return render(request,'profile.html')

def aboutus(request):
    return render(request,'aboutus.html')


# upload vacancy
def uploadview(request, id):
    d=regmodel.objects.get(id=id)
    cm=d.company
    em=d.email
    if request.method=='POST':
        a=uploadform(request.POST)
        if a.is_valid():
            cm=a.cleaned_data['company']
            em=a.cleaned_data['email']
            jb=a.cleaned_data['job']
            jtype=a.cleaned_data['jobtype']
            wtype=a.cleaned_data['worktype']
            ex=a.cleaned_data['experience']
            qu=a.cleaned_data['qualification']

            b=uploadmodel(company=cm,email=em,job=jb,jobtype=jtype,worktype=wtype,experience=ex,qualification=qu)
            b.save()
            return redirect(displayview)
        #     return HttpResponse('vacancy uploaded succesfully...')
        # else:
        #     return HttpResponse('failed to upload vacancy...')
    else:
        return render(request, 'upload vacancies.html',{'cm':cm,'em':em})



def displayview(request):
    a=uploadmodel.objects.all()
    b=request.session['company']
    return render(request,'vacancy_display.html',{'a':a,'b':b})

# edit button
def editvacancy(request,id):
    a=uploadmodel.objects.get(id=id)
    if request.method=='POST':
        a.company=request.POST.get('company')
        a.email=request.POST.get('email')
        a.job=request.POST.get('job')
        a.jobtype=request.POST.get('jobtype')
        a.worktype=request.POST.get('worktype')
        a.experience=request.POST.get('experience')
        a.qualification=request.POST.get('qualification')
        a.save()
        return redirect(displayview)
    return render(request,'editvacancy.html',{'a':a,'id':id})

def deletevacancy(request,id):
    a=uploadmodel.objects.get(id=id)
    a.delete()
    return redirect(displayview)


# user login and resgistration


class UserRegister(generic.CreateView):
    form_class=reg
    template_name='user_registration.html'
    success_url = reverse_lazy('userlog')
#     pokenda pagente url name in reverse lazy

class UserLogin(generic.View):
    form_class=log
    template_name='user_login.html'

    def get(self,request):
        a=log
        return render(request,'user_login.html',{'a':a})

    def post(self,request):
        if request.method=='POST':
            a=log(request.POST)
            if a.is_valid():
                em=a.cleaned_data['email']
                pas=a.cleaned_data['password']

                b=User.objects.all()
                for i in b:
                    if i.email==em and i.password==pas:
                        return render(request,'user profile.html')
                else:
                    return HttpResponse("LOGIN FAILED")

# view vacany for user
def vacancyview(request):
    a=uploadmodel.objects.all()
    return render(request,'viewvac.html',{'a': a})

def userapply(request,id):
    a=uploadmodel.objects.get(id=id)
    cm=a.company
    jb=a.job
    if request.method=='POST':
        c=applyform(request.POST,request.FILES)
        if c.is_valid():
            cm=c.cleaned_data['company']
            jb=c.cleaned_data['job']
            nm=c.cleaned_data['name']
            em=c.cleaned_data['email']
            rs=c.cleaned_data['resume']

            b=userapplymodel(company=cm,job=jb,name=nm,email=em,resume=rs)
            b.save()
        # mail sending function
            subject=f"NEW JOB APPLIED TO {cm}"
            message=f"hi{nm}\n your application for {jb} is applied successfully"
            email_from = EMAIL_HOST_USER
            send_mail(subject,message,email_from,[em])
            return redirect(emailalert)
        else:
            return HttpResponse("failed to apply for the post")
    else:
        return render(request, 'userapply.html',{'cm':cm,'jb':jb})

def emailalert(request):
    return render(request,'emailalert.html')

def wishlist(request,id):
    a=uploadmodel.objects.get(id=id)
    b=wishmodel(company=a.company,email=a.email,job=a.job,jobtype=a.jobtype,worktype=a.worktype,experience=a.experience,qualification=a.qualification)
    b.save()
    return HttpResponse("job added to wishlist")

def wishdetail(request):
    a=wishmodel.objects.all()
    return render(request,'wishlistdetails.html',{'a':a})

def removewish(request,id):
    b=wishmodel.objects.get(id=id)
    b.delete()
    return redirect(wishdetail)


def appliedusersdisplay(request):
    a=userapplymodel.objects.all()
    b=request.session['company']

    resume=[]
    cm=[]
    jb=[]
    nm=[]
    em=[]
    id=[]
    for i in a:
        # cm-->list name,com-->model nin value take and saviing variable.. company-->model data
        re=i.resume
        resume.append(str(re).split('/')[-1])
        com=i.company
        cm.append(com)
        jt=i.job
        jb.append(jt)
        nam=i.name
        nm.append(nam)
        ema=i.email
        em.append(ema)
        id1=i.id
        id.append(id1)
    mylist=zip(resume,cm,jb,nm,em,id)

    return render(request,'appliedusers.html',{'a':mylist,'b':b})

def removeuser(request,id):
    a=userapplymodel.objects.get(id=id)
    a.delete()
    return redirect(appliedusersdisplay)

def sendemail(request,id):
    a = userapplymodel.objects.get(id=id)
    em = a.company

    if request.method == 'POST':
        c = userform(request.POST, request.FILES)
        if c.is_valid():
            jb = c.cleaned_data['job']
            nm = c.cleaned_data['name']
            em = c.cleaned_data['email']


            b = userapplymodel( name=nm, email=em,job=jb)
            b.save()
            # mail sending function
            subject = f"you are shortlisted "
            message = f"hi{nm}\n your application for {jb} is shortlisted"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            return render(request, 'usersendemail.html')
        else:
            return HttpResponse("failed")
           



# def userapply(request):
#     return render(request,'userapply.html')


#
# user_profile

def profileuser(request):
    return render(request,'user profile.html')

def profile_details(request):
    return render(request,'profile_details.html')


def userprodis(request,id):
    a=usermodel.objects.get(id=id)
    id=[]
    im=[]
    nm=[]
    em=[]
    re=[]
    ed=[]
    ex=[]
    ad=[]
    ph=[]
    for i in a:
        id1=i.id
        id.append(id1)
        img=i.image
        im.append(str(img).split('/')[-1])
        nam=i.name
        nm.append(nam)
        ema=i.email
        em.append(ema)
        res=i.resume
        re.append(str(res).split('/')[-1])
        edu=i.education
        ed.append(edu)
        exp=i.experience
        ex.append(exp)
        add=i.address
        ad.append(add)
        phn=i.phone
        ph.append(phn)
    mylist=zip(id,im,nm,em,re,ed,ex,ad,ph)

    return render(request,'userprofiledis.html',{'a':mylist,'id':id})






