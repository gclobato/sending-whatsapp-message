# importando o módulo

import pywhatkit


# usando o Tratamento de Exceções para evitar erros sem precedentes

try:


# enviando mensagem ao destinatário usando pywhatkit

    pywhatkit.sendwhatmsg("+919767292502","Hello Python",21, 23)

    print("Enviada com sucesso!")

except:


# tratando exceção e imprimindo mensagem de erro

    print("Um erro inesperado!")