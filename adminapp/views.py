from audioop import reverse
from django.shortcuts import redirect, render

# from app1.models import Article
# from adminapp.forms import ArticleForm
from firebase_admin import firestore
from django.utils.safestring import mark_safe
from datetime import datetime

from usersmanagement.decorators import login_required


# def get_content_html(self):
#         return mark_safe(self.content)
# Create your views here.


@login_required
def index(request):
    return render(request, 'adminapp/admin_home.html', {})

@login_required
def articles(request):
    # articles_list = Article.objects.all()
    context = {
        # "articles" : articles_list,
    }
    return render(request,"adminapp/articles.html", context)

# @login_required
def get_postes():
    # Example: Fetch documents from Firestore
    data = []
    docs = firestore.client().collection('postes').stream()
    for doc in docs:
        data.append(doc.to_dict())
        
    print(f"data : {data}")
    return data

@login_required
def get_firestore_data(request):
    # Example: Fetch documents from Firestore
    data = []
    docs = firestore.client().collection('postes').stream()
    for doc in docs:
        data.append(doc.to_dict())
        
    print(f"data : {data}")
    return render(request, 'home.html', {'data': data})

@login_required
def getPostes(request):
    postes = get_postes()
    print(f"postes : {postes}")
    # articles = Article.objects.all()
    # for article in articles:
    #     print(f'article : {articles}')
    context = {
        'postes': postes,
        # 'articles': articles
    }
    return render(request,'adminapp/postes.html', context)

# @login_required
def addPostes(image_url,video_url,title,author,description,content):
    collection_ref = firestore.client().collection('postes')
    # Get the current date and time
    current_datetime = datetime.now()

    # Format the date and time into a string suitable for an ID
    formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S')

    # Set the formatted datetime as the document ID
    doc_ref = collection_ref.document(formatted_datetime)
    
    # Data to be added to Firestore
    data = {
        'id':formatted_datetime,
        'image_url': image_url,
        'video_url': video_url,
        'title': title,
        'author': author,
        'description': description,
        'content': mark_safe(content),
        'published_date': formatted_datetime  # You can store the formatted datetime if needed
    }
    # doc_ref = collection_ref.add({
    #             'image': image,
    #             'title': title,
    #             'author':author,
    #             'description': description,
    #             'content': mark_safe(content),
    #             'published_date': 'published_date'
    #         })
    
    # firestore_document_id = doc_ref.id
    
    # Add the data to Firestore
    doc_ref.set(data)
    print(f"doc_ref : {doc_ref}")
    return doc_ref


@login_required
def newPost(request):
    if request.method == 'POST':
        # Get form data
        image_url = request.POST.get('image_url')
        video_url = request.POST.get('video_url')
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        content = request.POST.get('content')
        print(f"data : {image_url},{title},{author},{description},{content}")
        # collection_ref = firestore.client().collection('postes')
        # doc_ref = collection_ref.add({
        #             'image': image,
        #             'title': title,
        #             'author':author,
        #             'description': description,
        #             'content': mark_safe(content),
        #             'published_date': 'published_date'
        #         })
        
        doc_ref = addPostes(image_url,video_url,title,author,description,content)
        return redirect('adminapp:newPost')
    else:
        print(f"method is {request.method}")
    
        return render(request,'adminapp/article_Form.html',{})
    
########################################

@login_required
def users(request):
    # Retrieve users from Firestore
    db = firestore.client()
    users_ref = db.collection('users')
    users_data = [user.to_dict() for user in users_ref.stream()]
    print(f"users_data : {users_data}")
    context = {
        'users': users_data,
    }
    return render(request,"adminapp/users.html",context)


################################################

def get_annoncements():
    data = []
    docs = firestore.client().collection('annonces').stream()
    for doc in docs:
        data.append(doc.to_dict())
        
    print(f"data : {data}")
    return data

@login_required
def annonces(request):
    annonces = get_annoncements()
    print(f"annonces : {annonces}")
    context = {
        'annonces': annonces,
    }
    return render(request,"adminapp/annonces.html", context)

# @login_required
def addAnnoucement(image_url,video_url,title,description,content):
    collection_ref = firestore.client().collection('annonces')
    # Get the current date and time
    current_datetime = datetime.now()

    # Format the date and time into a string suitable for an ID
    formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S')

    # Set the formatted datetime as the document ID
    doc_ref = collection_ref.document(formatted_datetime)
    
    # Data to be added to Firestore
    data = {
        'id':formatted_datetime,
        'image_url': image_url,
        'video_url': video_url,
        'title': title,
        'description': description,
        'content': mark_safe(content),
        'published_date': formatted_datetime  # You can store the formatted datetime if needed
    }
    
    # Add the data to Firestore
    doc_ref.set(data)
    print(f"doc_ref : {doc_ref}")
    return doc_ref

@login_required
def newAnnoucement(request):
    if request.method == 'POST':
        # Get form data
        image_url = request.POST.get('image_url')
        video_url = request.POST.get('video_url')
        title = request.POST.get('title')
        description = request.POST.get('description')
        content = request.POST.get('content')
        print(f"data : {image_url},{title},{description},{content}")
        
        doc_ref = addAnnoucement(image_url,video_url,title,description,content)
        return redirect('adminapp:newAnnoucement')
    else:
        print(f"method is {request.method}")
    
        return render(request,'adminapp/annoucement_form.html',{})
