import re
import random
def validar_cpf(cpf):

    if not cpf:
        return False,'Campo vazio!' 
    cpf = re.sub (r'[^0-9]','',cpf)
    if len(cpf) != 11:
         return False,'CPF deve conter exatamente 11 digitos!'
      
    if cpf[0] * 11 == cpf:
     return False,'CPF não pode ter todos os digitos iguais!'
    nove_primeiros=cpf[:9]
    
    multiplicador=10
    soma = 0 
    for n in nove_primeiros:
        soma += (int(n)* multiplicador)
        multiplicador -= 1 
    digito_1=(soma*10)%11
    if digito_1 == 10:
        digito_1 = 0
    if digito_1 != int(cpf[9]):
        return False,'CPF inválido'
    dez_primeiros=nove_primeiros + str(digito_1)
    multiplicador = 11
    soma = 0 
    for n in dez_primeiros:
        soma += (int(n) * multiplicador)
        multiplicador -= 1 
    digito_2=(soma * 10 ) % 11
    if digito_2 == 10 :
        digito_2 = 0
    
    if digito_2 != int(cpf[10]):
        return False,'CPF inválido'
       
    else:
         
         return True,'CPF válido'
       

def gerar_cpf():
    
        cpf_base = ''
        for _ in range(9):
            cpf_base += str(random.randint(0,9))
        multiplicador = 10
        soma = 0
        for n in cpf_base:
            soma += (int(n) * multiplicador) 
            multiplicador -= 1

        digito_1=(soma * 10) % 11
        if digito_1 == 10:
            digito_1 = 0
        multiplicador = 11
        soma = 0
        for n in cpf_base+ str(digito_1):
            soma += (int(n) * multiplicador) 
            multiplicador -= 1
        digito_2=(soma * 10) % 11
        if digito_2 == 10:
            digito_2 = 0
        cpf_valido=cpf_base + str(digito_1) + str(digito_2)
        if validar_cpf(cpf_valido):
            return cpf_valido

def formatar_cpf(cpf):
    cpf = re.sub (r'[^0-9]','',cpf)
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"