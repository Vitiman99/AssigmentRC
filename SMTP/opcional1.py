import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor y las credenciales de Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'manumartinez0309@gmail.com'
password = 'ojhn kqsh pzek tgqn'  # Reemplaza con tu contraseña de Gmail

# Crea el mensaje de correo electrónico
subject = 'Prueba de correo electrónico con TLS/SSL'
message = 'Hola, esto es una prueba de envío de correo electrónico con TLS/SSL desde Python.'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = 'vmsire@gmail.com'
msg['Subject'] = subject

body = MIMEText(message, 'plain')
msg.attach(body)

# Inicia la conexión con el servidor SMTP de Gmail utilizando TLS
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()

# Inicia sesión en tu cuenta de Gmail
smtp.login(sender_email, password)

# Envía el correo electrónico
smtp.sendmail(sender_email, 'victormsire@gmail.com', msg.as_string())

# Cierra la conexión con el servidor SMTP
smtp.quit()
