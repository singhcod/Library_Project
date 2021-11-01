from django.shortcuts import render,redirect
from .models import BookModel
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate,login



def signup_view(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserRegistrationForm()
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserRegistrationForm()
        return render(request,'signup.html',{'form':form})



def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(email=username,password = password)
        if user is not None:
            login(request,user)
            return redirect('displayall')
        else:
            return render(request,'login.html')

    else:
        return render(request,'login.html')


def bookdata_view(request):
    if request.method == "POST":
        book_name = request.POST.get('book_name')
        author_name = request.POST.get('author_name')
        pages = request.POST.get('pages')
        prise = request.POST.get('prise')
        released_date = request.POST.get("released_date")

        BookModel(
            book_name=book_name,
            author_name=author_name,
            pages=pages,
            prise=prise,
            released_date=released_date
        ).save()
        return redirect('displayall')




    else:
        return render(request,'bookentery.html')



def display_view(request):
    books = BookModel.objects.all()
    return render(request,'displaydata.html',{'books':books})

def update_view(request,id):
    book = BookModel.objects.get(id=id)
    return render(request,'updatedata.html',{'book':book})

def updateSave_view(request,id):
    Book = BookModel.objects.get(id=id)
    Book.book_name = request.POST.get('book_name')
    Book.author_name = request.POST.get('author_name')
    Book.pages = request.POST.get('pages')
    Book.prise = request.POST.get('prise')
    Book.released_date = request.POST.get("released_date")
    Book.save()
    return redirect('displayall')


def delete_view(request,id):
    book = BookModel.objects.get(id=id)
    book.delete()
    return redirect('displayall')

