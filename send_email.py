from smtplib import SMTP

def sendEmail():
    try:
        servidor_email = SMTP('smtp.gmail.com', 587)
        servidor_email.starttls()
        servidor_email.login('seuemail@gmail.com', 'password')
        
        remetente = 'seuemail@gmail.com'
        destinatarios = ['destinatario_1_@gmail.com', 'destinatario_2_@gmail.com', '... outros']
        conteudo = 'Servidor com temperatura acima de 18°C.'
        
        servidor_email.sendmail(remetente, destinatarios, conteudo.encode())
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
    finally:
        servidor_email.quit()