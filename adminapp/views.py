from audioop import reverse
from django.shortcuts import redirect, render

# from app1.models import Article
# from adminapp.forms import ArticleForm
from firebase_admin import firestore
from django.utils.safestring import mark_safe
from datetime import datetime

from usersmanagement.decorators import login_required
from django.http import JsonResponse


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

########################################
def get_consulate_contacts():
    data = []
    docs = firestore.client().collection('consulate_contacts').stream()
    for doc in docs:
        data.append(doc.to_dict())
        
    print(f"data : {data}")
    return data

@login_required
def consulate_contacts(request):
    consulate_contacts = get_consulate_contacts()
    print(f"consulate_contacts : {consulate_contacts}")
    context = {
        'consulate_contacts': consulate_contacts,
    }
    return render(request,"adminapp/consulate_contact.html", context)

# @login_required
def addConsulate_contact(address,phoneNumber1,phoneNumber2,email):
    collection_ref = firestore.client().collection('consulate_contacts')
    # Get the current date and time
    current_datetime = datetime.now()

    # Format the date and time into a string suitable for an ID
    formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S')

    # Set the formatted datetime as the document ID
    doc_ref = collection_ref.document(formatted_datetime)
    
    # Data to be added to Firestore
    data = {
        'id':formatted_datetime,
        'address': address,
        'phoneNumber1': phoneNumber1,
        'phoneNumber2':phoneNumber2,
        'email': email,
    }
    
    # Add the data to Firestore
    doc_ref.set(data)
    print(f"doc_ref : {doc_ref}")
    return doc_ref

@login_required
def newConsulate_contact(request):
    if request.method == 'POST':
        # Get form data
        address = request.POST.get('address')
        phoneNumber1 = request.POST.get('phoneNumber1')
        phoneNumber2 = request.POST.get('phoneNumber2')
        email = request.POST.get('email')
        print(f"data : {address},{phoneNumber1},{phoneNumber2},{email}")
        
        doc_ref = addConsulate_contact(address,phoneNumber1, phoneNumber2,email)
        return redirect('adminapp:newConsulate_contact')
    else:
        print(f"method is {request.method}")
    
        return render(request,'adminapp/consulate_contact_form.html',{})
    
    
@login_required
def delete_consulate_contact(request, consulate_contact_id):
    if request.method == "GET":
        db = firestore.client()
        consulate_contact_ref = db.collection('consulate_contacts').document(str(consulate_contact_id))
        consulate_contact_ref.delete()
    else: 
        print(f"method is {request.method}")
            
    return redirect('adminapp:consulate_contacts')
    
    
#####################################
    
########################################
def get_etat_civils():
    data = []
    docs = firestore.client().collection('etat_civils').stream()
    for doc in docs:
        data.append(doc.to_dict())
        
    print(f"data : {data}")
    return data

@login_required
def etat_civils(request):
    etat_civils = get_etat_civils()
    print(f"etat_civils : {etat_civils}")
    context = {
        'etat_civils': etat_civils,
    }
    return render(request,"adminapp/etat_civils.html", context)

# @login_required
def addetat_civil(type_de_demande,frais):
    collection_ref = firestore.client().collection('etat_civils')
    # Get the current date and time
    current_datetime = datetime.now()

    # Format the date and time into a string suitable for an ID
    formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S')

    # Set the formatted datetime as the document ID
    doc_ref = collection_ref.document(formatted_datetime)
    
    # Data to be added to Firestore
    data = {
        'id':formatted_datetime,
        "type_de_demande": type_de_demande,
        'frais': frais,
    }
    
    # Add the data to Firestore
    doc_ref.set(data)
    print(f"doc_ref : {doc_ref}")
    return doc_ref

@login_required
def newetat_civil(request):
    if request.method == 'POST':
        # Get form data
        type_de_demande = request.POST.get('type_de_demande')
        frais = request.POST.get('frais')
        print(f"data : {type_de_demande},{frais}")
        
        doc_ref = addetat_civil(type_de_demande ,frais)
        return redirect('adminapp:newetat_civil')
    else:
        print(f"method is {request.method}")
    
        return render(request,'adminapp/etat_civil_form.html',{})
    
    
@login_required
def update_etat_civil(request, etat_civil_id):
    
    if request.method == 'GET':
        # try:
            # Retrieve user data from Firestore
            db = firestore.client()
            etat_civil_ref = db.collection('etat_civils').document(str(etat_civil_id))
            etat_civil_data = etat_civil_ref.get().to_dict()

            if not etat_civil_data:
                return JsonResponse({'success': False, 'message': 'etat_civil not found'})
            
            context = {
                "etat_civil_data" : etat_civil_data
            }
            
            return render(request,"adminapp/update_etat_civil_page.html", context)
            # return JsonResponse({'success': True, 'user': user_data})
        # except Exception as e:
        #     return JsonResponse({'success': False, 'message': str(e)})
        
    if request.method == 'POST':
        # try:
            # Extract user data from POST request
            data = request.POST
            type_de_demande = data.get('type_de_demande')
            frais = data.get('frais')

            # Create or update user in Firestore
            user_data = {
                'id': etat_civil_id,
                'type_de_demande':type_de_demande,
                'frais': frais,
            }

            # Save user data to Firestore
            db = firestore.client()
            user_ref = db.collection('etat_civils').document(etat_civil_id)
            user_ref.set(user_data)

            return redirect('adminapp:etat_civils')
        
@login_required
def delete_etat_civil(request, etat_civil_id):
    if request.method == "GET":
        db = firestore.client()
        user_ref = db.collection('etat_civils').document(str(etat_civil_id))
        user_ref.delete()
    else: 
        print(f"method is {request.method}")
            
    return redirect('adminapp:etat_civils')




#####################################
    
########################################
def get_visa_infos():
    data = []
    docs = firestore.client().collection('visa_infos').stream()
    for doc in docs:
        data.append(doc.to_dict())
        
    print(f"data : {data}")
    return data

@login_required
def visa_infos(request):
    visa_infos = get_visa_infos()
    print(f"visa_infos : {visa_infos}")
    context = {
        'visa_infos': visa_infos,
    }
    return render(request,"adminapp/visa_infos.html", context)

# @login_required
def addvisa_info(monde,jours_30,jours_90,de_3_mois_à_1_an,de_1_à_2_ans,de_2_à_3_ans,de_3_ans_et_plus):
    collection_ref = firestore.client().collection('visa_infos')
    # Get the current date and time
    current_datetime = datetime.now()

    # Format the date and time into a string suitable for an ID
    formatted_datetime = current_datetime.strftime('%Y%m%d%H%M%S')

    # Set the formatted datetime as the document ID
    doc_ref = collection_ref.document(formatted_datetime)
    # Data to be added to Firestore
    data = {
        'id':formatted_datetime,
        "monde": monde,
        '30_jours':jours_30,
        '90_jours':jours_90,
        'de_3_mois_à_1_an':de_3_mois_à_1_an,
        'de_1_à_2_ans':de_1_à_2_ans,
        'de_2_à_3_ans':de_2_à_3_ans,
        'de_3_ans_et_plus':de_3_ans_et_plus,
    }
    
    # Add the data to Firestore
    doc_ref.set(data)
    print(f"doc_ref : {doc_ref}")
    return doc_ref

@login_required
def newvisa_info(request):
    if request.method == 'POST':
        # Get form data
        
        monde = request.POST.get('monde')
        jours_30 = request.POST.get('30_jours')
        jours_90 = request.POST.get('90_jours')
        de_3_mois_à_1_an = request.POST.get('de_3_mois_à_1_an')
        de_1_à_2_ans = request.POST.get('de_1_à_2_ans')
        de_2_à_3_ans = request.POST.get('de_2_à_3_ans')
        de_3_ans_et_plus = request.POST.get('de_3_ans_et_plus')
        
        doc_ref = addvisa_info(monde ,jours_30,jours_90,de_3_mois_à_1_an,de_1_à_2_ans,de_2_à_3_ans,de_3_ans_et_plus)
        return redirect('adminapp:newvisa_info')
    else:
        print(f"method is {request.method}")
    
        return render(request,'adminapp/visa_info_form.html',{})
    
    
@login_required
def update_visa_info(request, visa_info_id):
    
    if request.method == 'GET':
        # try:
            # Retrieve user data from Firestore
            db = firestore.client()
            visa_info_ref = db.collection('visa_infos').document(str(visa_info_id))
            visa_info_data = visa_info_ref.get().to_dict()

            if not visa_info_data:
                return JsonResponse({'success': False, 'message': 'visa_info not found'})
            
            context = {
                "visa_info_data" : visa_info_data
            }
            
            return render(request,"adminapp/update_visa_info_page.html", context)
            # return JsonResponse({'success': True, 'user': user_data})
        # except Exception as e:
        #     return JsonResponse({'success': False, 'message': str(e)})
        
    if request.method == 'POST':
        # try:
            # Extract user data from POST request
            data = request.POST
            monde = data.get('monde')
            jours_30 = data.get('30_jours')
            jours_90 = data.get('90_jours')
            de_3_mois_à_1_an = data.get('de_3_mois_à_1_an')
            de_1_à_2_ans = data.get('de_1_à_2_ans')
            de_2_à_3_ans = data.get('de_2_à_3_ans')
            de_3_ans_et_plus = data.get('de_3_ans_et_plus')
            

            # update VISAINFOS in Firestore
            
            visa_infos_data = {
                'id':visa_info_id,
                "monde": monde,
                '30_jours':jours_30,
                '90_jours':jours_90,
                'de_3_mois_à_1_an':de_3_mois_à_1_an,
                'de_1_à_2_ans':de_1_à_2_ans,
                'de_2_à_3_ans':de_2_à_3_ans,
                'de_3_ans_et_plus':de_3_ans_et_plus,
            }

            # Save user data to Firestore
            db = firestore.client()
            visa_infos_ref = db.collection('visa_infos').document(visa_info_id)
            visa_infos_ref.set(visa_infos_data)

            return redirect('adminapp:visa_infos')
        
@login_required
def delete_visa_info(request, visa_info_id):
    if request.method == "GET":
        db = firestore.client()
        visa_info_ref = db.collection('visa_infos').document(str(visa_info_id))
        visa_info_ref.delete()
    else: 
        print(f"method is {request.method}")
            
    return redirect('adminapp:visa_infos')