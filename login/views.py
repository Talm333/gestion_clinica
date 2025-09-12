from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        user = False
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'inacap' and password == 'clinica2025':
            user = True
            return redirect(request, 'recepcion/registrar.html', {'user': username})
        if user is False:
            return render(request, 'login/error.html', {'error': 'Credenciales inválidas'})
        
    return render(request, 'login/login.html')
