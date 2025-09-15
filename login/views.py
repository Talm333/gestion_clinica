from django.shortcuts import render, redirect

# Create your views here.

def login(request):
    if request.method == 'POST':
        request.session['autenticado'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == "inacap" and password == "clinica2025":
            request.session['autenticado'] = True
            request.session['username'] = username  # Guardar el nombre de usuario en sesión
            return redirect('/recepcion/registrar/')
        if request.session['autenticado'] == False:
            return render(request, 'login/login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login/login.html')

def logout(request):
    request.session.flush()
    return redirect('/login/login.html')
