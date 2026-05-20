


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            from django.shortcuts import redirect
            return redirect('login')  # yoki kerakli sahifa
        return view_func(request, *args, **kwargs)
    return wrapper