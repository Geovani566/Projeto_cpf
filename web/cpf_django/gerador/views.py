from django.shortcuts import render
from .funcoes_cpf import gerar_cpf,validar_cpf,formatar_cpf
# Create your views here.
def home(request):
    cpf=None
    valido=None
    ultimo_cpf=request.session.get('ultimo_cpf')


    cpf_digitado=request.session.get('cpf_digitado')
    mensagem=request.session.get('mensagem')
    valido=request.session.get('valido')



    if "gerar_cpf" in request.POST :
        
        cpf=gerar_cpf()
        cpf=formatar_cpf(cpf)
        request.session['ultimo_cpf']=cpf
        ultimo_cpf=cpf
        
    if "validar_cpf" in request.POST :
        cpf_digitado=request.POST.get("cpf_digitado")
        request.session['cpf_digitado']=cpf_digitado
        valido,mensagem=validar_cpf(cpf_digitado)
        request.session['valido']=valido
        request.session['mensagem']=mensagem
    if cpf_digitado:
        cpf_digitado_formatado=formatar_cpf(cpf_digitado)
    else:
        cpf_digitado_formatado=None





    return render(     
            request,'gerador/home.html',
            {
            'cpf':cpf,
            'valido':valido,
            'ultimo_cpf':ultimo_cpf,
            'cpf_digitado':cpf_digitado,
            'mensagem':mensagem,
            'cpf_digitado_formatado':cpf_digitado_formatado,
            }
    )
    