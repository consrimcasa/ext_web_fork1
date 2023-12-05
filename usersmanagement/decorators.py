from django.shortcuts import redirect



def login_required(view_func):
    
    def wrapper(request, *args, **kwargs):
        user_id = request.session.get('user_id')
        if user_id is not None:
            # User is logged in, do something with user_id
            return view_func(request, *args, **kwargs)
        else:
            # User is not logged in, redirect to login page
            return redirect('usersmanagement:login')
        # if request.user.is_authenticated:
        #     return view_func(request, *args, **kwargs)
        # else:
        #     return redirect('usersmanagement:login')
    return wrapper