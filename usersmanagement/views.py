# # Create your views here.

# def login(request):
#     pass

# def register(request):
#     pass

# # views.py

from django.urls import reverse
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from firebase_admin import auth, firestore
from .decorators import login_required
# from .models import User
from datetime import datetime


import hashlib

def md5_hash(text):
    # # Create an MD5 hash object
    # md5_hasher = hashlib.md5()

    # # Update the hash object with the bytes of the input text
    # md5_hasher.update(text.encode('utf-8'))

    # # Get the hexadecimal representation of the hash
    # hashed_text = md5_hasher.hexdigest()

    # return hashed_text
    if text is None:
            raise ValueError("Input text cannot be None")

    # Create an MD5 hash object
    md5_hasher = hashlib.md5()

    # Update the hash object with the bytes of the input text
    md5_hasher.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_text = md5_hasher.hexdigest()

    return hashed_text

@login_required
def create_user(request):
    if request.method == 'POST':
        # try:
            # Extract user data from POST request
            data = request.POST
            email = data.get('email')
            password = data.get('password')
            first_name = data.get('firstName')
            last_name = data.get('lastName')
            phone_number = data.get('phoneNumber')
            
            # Get the current date and time
            current_datetime = datetime.now()

            # Format the date and time into a string suitable for an ID
            user_id = current_datetime.strftime('%Y%m%d%H%M%S')

            # # Create user in Firebase Authentication
            # user = auth.create_user(
            #     email=email,
            #     password=password,
            # )

            # Hash the password before saving it to the database
            hashed_password = md5_hash(password)

            # Create or update user in Firestore
            user_data = {
                'id': user_id,
                # 'image': None,  # You can handle image upload separately
                'firstName': first_name,
                'lastName': last_name,
                'phoneNumber': phone_number,
                'email': email,
                'password': hashed_password,
            }

            # Save user data to Firestore
            db = firestore.client()
            user_ref = db.collection('users').document(user_id)
            user_ref.set(user_data)

            return redirect('usersmanagement:create')
        # except Exception as e:
        #     return JsonResponse({'success': False, 'message': str(e)})
        
    context = {}
    return render(request,"usersmanagement/create_user_page.html", context)

    # return JsonResponse({'success': False, 'message': 'Invalid request method'})
    

@login_required
def update_user(request, user_id):
    
    if request.method == 'GET':
        # try:
            # Retrieve user data from Firestore
            db = firestore.client()
            user_ref = db.collection('users').document(str(user_id))
            user_data = user_ref.get().to_dict()

            if not user_data:
                return JsonResponse({'success': False, 'message': 'User not found'})
            
            context = {
                "user_data" : user_data
            }
            
            return render(request,"usersmanagement/update_user_page.html", context)
            # return JsonResponse({'success': True, 'user': user_data})
        # except Exception as e:
        #     return JsonResponse({'success': False, 'message': str(e)})
        
    if request.method == 'POST':
        # try:
            # Extract user data from POST request
            data = request.POST
            email = data.get('email')
            # password = data.get('password')
            first_name = data.get('firstName')
            last_name = data.get('lastName')
            phone_number = data.get('phoneNumber')
            
            # # Get the current date and time
            # current_datetime = datetime.now()

            # # Format the date and time into a string suitable for an ID
            # user_id = current_datetime.strftime('%Y%m%d%H%M%S')

            # # Hash the password before saving it to the database
            # hashed_password = make_password(password)

            # Create or update user in Firestore
            user_data = {
                'id': user_id,
                # 'image': None,  # You can handle image upload separately
                'firstName': first_name,
                'lastName': last_name,
                'phoneNumber': phone_number,
                'email': email,
                # 'password': hashed_password,
            }

            # Save user data to Firestore
            db = firestore.client()
            user_ref = db.collection('users').document(user_id)
            user_ref.set(user_data)

            return redirect('adminapp:users')
        
    # if request.method == 'POST':
    #     return redirect('adminapp:newPost')
    # return JsonResponse({'success': False, 'message': 'Invalid request method'})

def forgot_password(request):
    if request.method == 'POST':
        # try:
            # Extract email from POST request
            email = request.POST.get('email')
            # Retrieve user by email from Firestore
            db = firestore.client()
            users_ref = db.collection('users')
            query = users_ref.where('email', '==', email)
            user_docs = query.stream()
            
            # # Check if any user is found
            # if not user_docs:
            #     return JsonResponse({'success': False, 'message': 'User not found'})

            # # Assuming there's only one user with the given email
            # user_data = user_docs[0].to_dict()
             # Check if any user is found
            user_data = None
            for user_doc in user_docs:
                user_data = user_doc.to_dict()
                print(f"user_data : {user_data}")
                print(f"user_data['id'] : {user_data['id']}")
            
            # Check if any user is found
            if user_docs:
                # redirect('usersmanagement:update_password')
                # Redirect to the update_password page with the user_id parameter
                return redirect(reverse('usersmanagement:update_password', kwargs={'user_id': user_data['id']}))
            # redirect("usersmanagement:update_password" user_data['id'])

        #     # Send password reset email
        #     auth.generate_password_reset_link(email)

        #     return JsonResponse({'success': True, 'message': 'Password reset email sent'})
        # except Exception as e:
        #     return JsonResponse({'success': False, 'message': str(e)})

    return render(request,"usersmanagement/forget_password.html", {})


def update_password(request, user_id):
    if request.method == 'POST':
        # try:
            # Extract new password from POST request
            new_password = request.POST.get('password')

            # Hash the new password before saving it
            hashed_password = md5_hash(new_password)

            # # Update password in Firebase Authentication
            # user = auth.get_user(str(user_id))
            # auth.update_user(
            #     user.uid,
            #     password=new_password,
            # )

            # Update hashed password in Firestore
            db = firestore.client()
            user_ref = db.collection('users').document(str(user_id))
            user_ref.update({'password': hashed_password})
            
            # redirect('usersmanagement:login')

            return JsonResponse({'success': True, 'message': 'Password updated successfully'})
        # except Exception as e:
        #     return JsonResponse({'success': False, 'message': str(e)})

    return render(request,"usersmanagement/update_password_page.html", {"user_id":user_id})

@login_required
def delete_user(request, user_id):
    if request.method == "GET":
        db = firestore.client()
        user_ref = db.collection('users').document(str(user_id))
        user_ref.delete()
    else: 
        print(f"method is {request.method}")
            
    return redirect('adminapp:users')


# def get_user_by_email_password(email, password):
#    # Save user data to Firestore
#     db = firestore.client()
#     user_ref = db.collection('users')
#     # Hash the password before saving it to the database
#     hashed_password = make_password(password)
#     query = user_ref.where('email', '==', str(email)).where('password', '==', hashed_password)

#     user_docs = query.stream()
#     # user_data = user_docs[0].to_dict()
    
#     # for user_doc in user_docs:
#     #     user_data = user_doc.to_dict()
#     #     return user_data
#     # return user_data
    
#     user_data = None
#     for user_doc in user_docs:
#         user_data = user_doc.to_dict()
#         print(f"user_data : {user_data}")
#         print(f"user_data['id'] : {user_data['id']}")
        
#     if user_docs:
#         return user_docs

# import bcrypt

# def hash_password(password):
#     # Generate a salt and hash the password
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
#     # Convert the hashed password to a string for storage
#     return hashed_password.decode('utf-8')

# def check_password(password, hashed_password):
#     # Check if the provided password matches the hashed password
#     return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


# @login_required
def get_user_by_email_password(email, password):
    db = firestore.client()
        

    # Query the 'users' collection based on email
    users_ref = db.collection('users')
    query = users_ref.where('email', '==', email)

    # Get the result
    user_docs = query.stream()

    # Check if a user with the provided email exists
    for user_doc in user_docs:
        user_data = user_doc.to_dict()
        
        # Hash the password before saving it to the database
        hashed_password = md5_hash(password)
        print(f"hashed_password :{hashed_password}")
        # Check if the password matches
        if user_data['password'] == hashed_password:
            return user_data

    # Return None if no user is found or password doesn't match
    return None

def login(request):
    if request.method == 'POST':
        data = request.POST
        email = data.get('email')
        password = data.get('password')

        user = get_user_by_email_password(email, password)
        
        # if user is not None:
        #     login(request, user)
        #     # Store user information in session
        #     request.session['user_id'] = user.id

        if user:
            # Store user information in session
            request.session['user_id'] = user['id']
            # request.session['user_username'] = user.username

            # Assuming you want to redirect to the 'adminapp:index' on successful login
            return redirect('adminapp:index')
        else:
            # Redirect to the login page if email/password are incorrect
            return redirect('usersmanagement:login')

    # Render the login page for GET requests
    return render(request, "usersmanagement/login_page.html", {})


def logout(request):
    # Clear user information from session
    request.session.pop('user_id', None)
    # ... clear other user information if needed
    return redirect('usersmanagement:login')
