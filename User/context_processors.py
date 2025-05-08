def user_type_context(request):
    """Add user type information to the template context."""
    context = {
        'is_rest_user': False
    }
    
    if request.user.is_authenticated:
        
        try:
           
            from User.models import rest_det
            
            # Check if current user is instance of rest_det
            if isinstance(request.user, rest_det):
                context['is_rest_user'] = True
                
        except ImportError:
            pass
    
    return context