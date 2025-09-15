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
<<<<<<< HEAD
=======
    # lo que hace es eliminar toda la informacion de la sesion es como eliminar el cache del navegador
>>>>>>> e99703f12acfebac4082134a4372a8fcc356d997
    request.session.flush()
    return redirect('/login/login.html')
