from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from round1.forms import SubmissionForm,AccountForm,UserForm
from round1.models import Submission,mp3_file,lyric_file,Author
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    if request.method == 'POST':
        form =AccountForm(request.POST)
        if form.is_valid():
            user = User(username=request.POST.username,email=request.POST.email,password=request.POST.password)
            user.save()
            return HttpResponseRedirect(reverse('round1.views.home'))
    else:
        #form=AccountForm()
        return render_to_response(
        'index.html',#{'form':form},
        context_instance=RequestContext(request)
    )
def about(request):
    return render_to_response(
        'about.html',context_instance=RequestContext(request)
    )

def rules(request):
    return render_to_response(
        'rules.html',context_instance=RequestContext(request)
    )
def auth_util(passedrequest):

    if passedrequest.user.id==None:
        return 1
    else:
        return passedrequest.user.id
def register(request):
    context = RequestContext(request)

    #initially this is set to be false and is updated if the user is registered
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)


        #If the form valid
        if user_form.is_valid():
            user = user_form.save()
            #the set_password method will hash the password
            user.set_password(user.password) #Django does this to password fields by default.
            user.save()
            #is_author = request.POST['author']
            #if is_author != u'on' :

        else:
            print user_form.errors
        return HttpResponseRedirect('/login')
    else:
        user_form = UserForm()

    return render_to_response(
        'register.html',
        {'user_form': user_form, 'registered':registered},
        context)

def submit(request):
    context=RequestContext(request)
    userid=auth_util(request)
    if userid<0:
        return render_to_response('login.html', {}, RequestContext(request))
    form =SubmissionForm()

    if request.method == 'POST':
        form = SubmissionForm(request.POST,request.FILES)

        print form.errors
        if form.is_valid():
            print 'Saving Bulletin'
            print request.user
            submission=Submission(owner=request.user,title=request.POST['title'],text_description=request.POST['text_description'])
            submission.save()
            #authors=[]
            try:
                author1=request.POST['author1']
                a = Author(comp_id=author1,piece=submission)
                a.save()
                author2=request.POST['author2']
                a = Author(comp_id=author2,piece=submission)
                a.save()
                author3=request.POST['author3']
                a = Author(comp_id=author3,piece=submission)
                a.save()
            except:
                pass
            mp3=request.FILES['mp3']
            lyrics=request.FILES['lyrics']
            from django.core.mail import send_mail,EmailMessage
            try:
                mail = EmailMessage('Submission:'+str(request.POST['title']), str(request.POST['text_description']),
                                    'UVaFightSong.com', ['fightsong@virginia.edu'])
                mail.attach(mp3.name,mp3.read())
                mail.attach(lyrics.name,lyrics.read())
                mail.send(fail_silently=False)

                mp3=mp3_file(submitted=submission)
                mp3.save(0)
                lyric=lyric_file(submitted=submission)
                lyric.save()
            except Exception as e:
                print e
            #bulletin = Bulletin(folder=Folder.objects.filter(f_key__exact=request.POST['folder'])[0],author_id=userid,title=request.POST['title'],lat=lat,long=long,text_description=request.POST['text_description'], encrypted=enc )
            #bulletin.save()
            return HttpResponseRedirect('/list')
        else:
            return render_to_response('submit.html',{'form':form},RequestContext(request))
        # doc_formset=DocumentFormSet(request.POST,request.FILES,prefix='documents')
        # if doc_formset.is_valid() and form.is_valid():
        #     for doc in doc_formset:
        #         print 'Saving a file'
        #         cd=doc.cleaned_data
        #         if cd.get('docfile')!=None:
        #             newdoc = Document(docfile=cd.get('docfile'),posted_bulletin=bulletin)
        #             newdoc.save(encrypted=enc)

    else:
        #print form
        return render_to_response('submit.html',{'form':form},RequestContext(request))

def list(request):
    context=RequestContext(request)
    userid=auth_util(request)
    if userid<0:
        return render_to_response('login.html', {}, RequestContext(request))
    else:
        submissions = Submission.objects.filter(owner=request.user)
        submissions=[i for i in submissions]
        return render_to_response('list.html',{'subs':submissions},context)

#Log-in Function
def user_login(request):
    context = RequestContext(request)

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        #If the password/username combination is valid, an User Object will be returned
        user = authenticate(username=username, password=password)
        # profile = request.user.get_profile()

        if user != None:
            #check if the account is active and then redirect back to main page
            if user.is_active:
                django_login(request, user)
               # if profile.author:
 #                  if User.objects.filter(username=username).count():
 #                if is_author(user):
 #                    return HttpResponseRedirect('/profile')
 #                else:
                return HttpResponseRedirect('/submit')
              #  else:
                #    return HttpResponseRedirect('/index')
            else:
                #otherwise account is inactive
                return HttpResponse("Account is not active")
        else:
            #invalid username/password combination
            return HttpResponse("The username and password combination that you provided is invalid")

    else:
        #The request is not a POST so it's probably a GET request
        return render_to_response('login.html', {}, context)

#logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/index/')