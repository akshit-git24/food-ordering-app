# from functools import wraps
# from django.http import HttpResponseForbidden
# from django.shortcuts import redirect
# from django.contrib import messages
# from User.models import rest_det 
# def rest_det_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         # Check if user is authenticated
#         if not request.user.is_authenticated:
#             messages.error(request, "Please log in to continue")
#             return redirect('users:choice_login')# replace with your login URL name
            
#         # Check if user is a rest_det user
         
#         if isinstance(request.user, rest_det):
#             return view_func(request, *args, **kwargs)
            
#         # If user is not a rest_det user, forbid access
#         messages.info(request, "Only restaurant users can create orders")
#         return redirect('users:Homepage')  
        
#     return _wrapped_view