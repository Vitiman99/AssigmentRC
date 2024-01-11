from email.mime.image import MIMEImage
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configuración del servidor y las credenciales de Gmail
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'victormanuelsiremartinez@gmail.com'
password = 'viza fyes bnur qmyf'  # Reemplaza con tu contraseña de Gmail

# Crea el mensaje de correo electrónico
subject = 'Prueba de correo electrónico con TLS/SSL'
message = 'Hola, esto es una prueba de envío de correo electrónico con TLS/SSL desde Python.'

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = 'loreconsu48@gmail.com'
msg['Subject'] = subject

body = MIMEText(message, 'plain')
msg.attach(body)

# Inicia la conexión con el servidor SMTP de Gmail utilizando TLS
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()

# Inicia sesión en tu cuenta de Gmail
smtp.login(sender_email, password)

# Ruta de la imagen que deseas adjuntar
image_path = '\Assigment3\OIP.jpg'

# Abre la imagen en modo binario
with open(image_path, 'rb') as f:
    image_data = f.read()

# Crea un objeto MIMEImage con los datos de la imagen
image = MIMEImage(image_data)

# Establece el nombre de archivo de la imagen
image.add_header('Content-Disposition', 'attachment', filename='OIP.jpg')

# Adjunta la imagen al mensaje de correo electrónico
msg.attach(image)

# Envía el correo electrónico
smtp.sendmail(sender_email, 'loreconsu48@gmail.com', msg.as_string())

# Cierra la conexión con el servidor SMTP
smtp.quit()