from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string

def index(request):

    #create the instance when clicking submit
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            print('It is valid, my friend')

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            content = form.cleaned_data['content']

            #Use the template for testing emails!
            # html = render_to_string('contact/emails/contactform.html',{
            #     'name' : name,
            #     'email' : email,
            #     'content' : content
            # })

            # send_mail('The Subject', 'The Message', 'from@email.com', ['to@email.com'], html_message=html)

            #sending email with gmail
            send_mail(
                f'Contact Form Submit: {subject}',
                f'Name: {name}\nEmail: {email}\n\nMessage: \n{content}',
                email,
                ['mario.33a.r@gmail.com'],
                fail_silently=False,
            )
            return redirect('index')

    #if we do not get any post request , we just create an form instance
    # to render the index.html 
        
    else:
        form = ContactForm()

    return render(request, 'contact/index.html',{
        'form':form
    })