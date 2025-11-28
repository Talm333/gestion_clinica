from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.
def login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            request.session['autenticado'] = False
            if username == "inacap" and password == "clinica2025":
                request.session['autenticado'] = True
                request.session['username'] = username  # Guardar el nombre de usuario en sesión
                return redirect('/recepcion/registrar/')
            else:
                return render(request, 'login/login.html', {'form': form, 'error': 'Credenciales inválidas'})
    return render(request, 'login/login.html', {'form': form})

def logout(request):
    # lo que hace es eliminar toda la informacion de la sesion es como eliminar el cache del navegador
    request.session.flush()
    return redirect('/login/login.html')