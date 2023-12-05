from django.shortcuts import render
# from .models import Article

# views.py

from django.shortcuts import render
from firebase_admin import firestore

# Create your views here.


def cv(request):
    return render(request, 'app1/cv.html', {})

def bienvenu(request):
    return render(request, 'app1/bienvenue.html', {})

def home(request):
    # articles = Article.objects.all().order_by('-published_date')
    # context = {'articles': articles}
    postes = get_postes()
    annonces = get_annoncements()
    
    # postes = []
    # annonces = []
    
    context = {
        'postes': postes,
        'annonces': annonces,
    }
    
    return render(request, 'app1/home.html', context)


def get_object_by_id(collection_name, document_id):
    """
    Retrieve a Firestore document based on the document ID.

    Args:
        collection_name (str): The name of the Firestore collection.
        document_id (str): The ID of the document to retrieve.

    Returns:
        dict or None: The document data if found, or None if not found.
    """
    # Initialize Firestore client and reference to the collection
    db = firestore.client()
    collection_ref = db.collection(collection_name)

    # Get the document reference based on the document_id
    doc_ref = collection_ref.document(document_id)

    # Retrieve the document snapshot
    doc_snapshot = doc_ref.get()

    # Check if the document exists
    if doc_snapshot.exists:
        # Return the document data
        return doc_snapshot.to_dict()
    else:
        # Document not found
        return None


def details_page(request, post_id):
    poste = get_object_by_id("postes", post_id)
    # print(f"poste.video_url : {poste.video_url}")
    if(poste['video_url'] == ""):
        print(f"poste : {poste['video_url']}")
    
    context = {
        "poste": poste
    }
    return render(request, 'app1/details_page.html', context)

def annoucement_details(request, annonce_id):
    annonce = get_object_by_id("annonces", annonce_id)
    # print(f"poste.video_url : {poste.video_url}")
    if(annonce['video_url'] == ""):
        print(f"annonce : {annonce['video_url']}")
    
    context = {
        "annonce": annonce
    }
    return render(request, 'app1/annoucement_details.html', context)

def consulate(request):
    context = {}
    return render(request, 'app1/consulate.html', context)

def services(request):
    context = {}
    return render(request, 'app1/services.html', context)

def affaires_sociales(request):
    context = {}
    return render(request, 'app1/affaires_sociales.html', context)

def services_etrangers(request):
    context = {}
    return render(request, 'app1/services_etrangers.html', context)

def documents_citoyens(request):
    context = {}
    return render(request, 'app1/documents_citoyens.html', context)

def etat_civil(request):
    context = {}
    return render(request, 'app1/etat_civil.html', context)


def get_postes():
    # Example: Fetch documents from Firestore
    data = []
    docs = firestore.client().collection('postes').stream()
    for doc in docs:
        data.append(doc.to_dict())
        
    print(f"data : {data}")
    return data

def get_annoncements():
    data = []
    docs = firestore.client().collection('annonces').stream()
    for doc in docs:
        data.append(doc.to_dict())
        
    print(f"data : {data}")
    return data



def announcements(request):
    postes = get_postes()
    annonces = get_annoncements()
    
    context = {
        'postes': postes,
        'annonces': annonces,
    }
    return render(request, 'app1/announcements.html', context)

def gallery(request):
    context = {}
    return render(request, 'app1/gallery.html', context)
def immatriculation(request):
    context = {}
    return render(request,"app1/immatriculation.html", context)

def studentsInfo(request):
    context = {}
    return render(request,"app1/studentsinfo.html", context)

def visas(request):
    context = {}
    return render(request,"app1/visas.html",context)

def fonctions_du_consulat(request):
    context = {}
    return render(request,"app1/fonctions_du_consulat.html", context)

def contact(request):
    context = {}
    return render(request,"app1/contact.html", context)