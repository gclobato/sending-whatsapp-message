# sending-whatsapp-message
 Sending-whatsapp-message-using-python



Oque cada parte faz:

Importando o Módulo: import pywhatkit importa o módulo pywhatkit, que oferece diversas funcionalidades, inclusive envio de mensagens do WhatsApp.

Tratamento de exceções (try-except): O código é encapsulado em um bloco try, que permite ao Python tentar o código dentro dele. Se ocorrer um erro durante a execução do código dentro do bloco try, o Python irá parar de executar esse bloco e pular para o bloco except.

Enviando mensagem do WhatsApp: Dentro do bloco try, a função pywhatkit.sendwhatmsg() é chamada para enviar uma mensagem do WhatsApp. São necessários quatro argumentos: o número de telefone do destinatário (incluindo o código do país), o conteúdo da mensagem, a hora do dia (no formato de 24 horas) em que a mensagem será enviada e o minuto da hora.

Mensagem de sucesso: Se a mensagem for enviada com sucesso e sem erros, o código dentro do bloco try será executado completamente e a mensagem de sucesso "Enviada com sucesso!" será impresso.

Tratamento de exceções (exceto): Se ocorrer algum erro inesperado durante a execução do código dentro do bloco try, o Python irá pular para o bloco except e executar o código dentro dele. Neste caso, simplesmente imprime a mensagem de erro "An Unexpected Error!". Isso garante que o programa não trave abruptamente se ocorrer um erro durante o envio da mensagem.