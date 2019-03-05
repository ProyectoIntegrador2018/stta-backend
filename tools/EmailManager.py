
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class EmailManager:

    fromUser = 'tramitesescolarestec2019@gmail.com'
    passwordUser = 'Ingser19&'

    @staticmethod
    def sendPasswordLink(link="", email=""):
        # create message object instance
        msg = MIMEMultipart()

        # setup the parameters of the message
        password = EmailManager.passwordUser
        msg['From'] = "noreply@reddefilantropia.site"
        msg['To'] = email
        msg['Subject'] = "Restablece tu contraseña"

        msg.add_header('Content-Type', 'text/html')
        body = "<a href=\"http://localhost:3000/restaurar/"+link+ "\"> Haz click aquí para restablecer tu contraseña</a>\n\n\n"
        body = MIMEText(body, "html", _charset="utf-8")
        msg.set_payload(body)

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        # Login Credentials for sending the mail
        server.login(EmailManager.fromUser, password)

        server.sendmail("noreply@reddefilantropia.site", msg['To'], msg.as_string())

        server.quit()

        return "successfully sent email to %s:" % (msg['To'])

    @staticmethod
    def sendConfirmationLink(link="", email=""):
        # create message object instance
        msg = MIMEMultipart()

        # setup the parameters of the message
        password = EmailManager.passwordUser
        msg['From'] = "noreply@reddefilantropia.site"
        msg['To'] = email
        msg['Subject'] = "Confirma tu cuenta"

        msg.add_header('Content-Type', 'text/html')
        body = "<a href=\"https://www.reddefilantropia.site/confirm/" + link + "\"> Haz click aquí para confirmar tu cuenta</a><br/><br/><br/>Red de Filantropía"
        body = MIMEText(body, "html", _charset="utf-8")
        msg.set_payload(body)

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        # Login Credentials for sending the mail
        server.login(EmailManager.fromUser, password)

        server.sendmail("noreply@reddefilantropia.site", msg['To'], msg.as_string())

        server.quit()

        return "successfully sent email to %s:" % (msg['To'])

    @staticmethod
    def sendConfirmationLink2(link="", email=""):
        # create message object instance
        msg = MIMEMultipart()

        # setup the parameters of the message
        password = EmailManager.passwordUser
        msg['From'] = "noreply@reddefilantropia.site"
        msg['To'] = email
        msg['Subject'] = "Confirma tu cuenta"

        msg.add_header('Content-Type', 'text/html')
        body = "<p>Estimado alumno(a):&nbsp;</p><p><b>Te recordamos que creaste una cuenta en el sistema de la Red de filantropía y no confirmaste tu correo.</b></p><a href=\"https://www.reddefilantropia.site/confirm/" + link + "\"> Haz click aquí para confirmar tu cuenta</a><br/><br/><br/>Red de Filantropía"
        body = MIMEText(body, "html", _charset="utf-8")
        msg.set_payload(body)

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        # Login Credentials for sending the mail
        server.login(EmailManager.fromUser, password)

        server.sendmail("noreply@reddefilantropia.site", msg['To'], msg.as_string())

        server.quit()

        return "successfully sent email to %s:" % (msg['To'])

    @staticmethod
    def sendConfirmationExtra(email):
        # create message object instance
        msg = MIMEMultipart()

        # setup the parameters of the message
        password = EmailManager.passwordUser
        msg['From'] = "noreply@reddefilantropia.site"
        msg['To'] = email
        msg['Subject'] = "Información adicional enviada"

        msg.add_header('Content-Type', 'text/html')
        body = "<p>Estimado alumno(a):&nbsp;</p><p><b>Tu información adicional se registro con éxito.</b></p><p>Saludos con afecto.</p><p>&nbsp;</p><p><strong>Coordinaci&oacute;n Nacional</strong></p><p>Apoyo de Vida</p>"
        body = MIMEText(body, "html", _charset="utf-8")
        msg.set_payload(body)

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        # Login Credentials for sending the mail
        server.login(EmailManager.fromUser, password)

        server.sendmail("noreply@reddefilantropia.site", msg['To'], msg.as_string())

        server.quit()

        return "successfully sent email to %s:" % (msg['To'])

    @staticmethod
    def sendExtraInfoEmail(email):
        # create message object instance
        msg = MIMEMultipart()

        # setup the parameters of the message
        password = EmailManager.passwordUser
        msg['From'] = "noreply@reddefilantropia.site"
        msg['To'] = email
        msg['Subject'] = "Información adicional"

        msg.add_header('Content-Type', 'text/html')
        body = '<p>Estimado alumno(a):&nbsp;</p><p>Muchas gracias por el env&iacute;o de tu forma de registro para este semestre.</p><p>Te informamos que con el deseo de tener mayor evidencia de lo mucho que ayuda este apoyo a nuestros estudiantes, te solicitamos ingreses al sitio <a href="http://www.reddefilantropia.site">www.reddefilantropia.site</a> con tu usuario y contrase&ntilde;a y contestes las preguntas que aparecen en el sistema. Adicionalmente, se te solicitar&aacute; elaborar un video de 3 minutos con tus respuestas y reflexiones para mostrarlo a nuestros donantes.</p><p>Hacemos de tu conocimiento tambi&eacute;n, que en caso de ser beneficiado con el apoyo, al final del semestre deber&aacute;s de enviar un reporte de las actividades realizadas y un video que de evidencia de los beneficios para tu desarrollo estudiantil y personal.&nbsp;</p><p>Finalmente, y despu&eacute;s de haber compartido con ustedes las limitaciones del programa, te comparto un correo de uno de tus compa&ntilde;eros que muestra un gran ejemplo de solidaridad y que invita a reflexionar nuevamente sobre nuestro compromiso de reciprocidad.</p><p>&nbsp;</p><table style="border-color: black; margin: auto !important; padding: 5px;" border="solid"><tbody><tr><td style="width: 510px; padding:15px;"><p><em>Buen d&iacute;a,</em></p><p><em>&nbsp;</em></p><p><em>Soy un L&iacute;der del Ma&ntilde;ana de la cuarta generaci&oacute;n. Los &uacute;ltimos tres semestres he sido benefactor del programa de apoyo de la Red de Filantrop&iacute;a, estando muy agradecido con todos ustedes y los donadores por ayudarme a cubrir mis gastos escolares. Veo que en este &uacute;ltimo semestre han estado haciendo recortes para seguir pudiendo apoyar a varios alumnos. Quiero decirles que <strong><u>este semestre no voy a renovar la solicitud de apoyo</u></strong> y que quisiera que mi espacio se lo den a alguien que lo necesite m&aacute;s. Estoy muy agradecido con el apoyo de la red que he recibido estos semestres, pero creo que en mi casa podemos hacer un esfuerzo extra para cubrir los gastos del semestre y que otro alumno con mayor necesidad del apoyo pueda seguir estudiando en el Tec.</em></p><p><em>Tengo entendido que este semestre dijeron que solo los que contaron con el apoyo el pasado pueden renovar, pero <strong><u>espero que mi espacio s&iacute; pueda ser transferido a otra persona</u></strong>.</em><em>&nbsp;</em></p><p><em>Como comentario, una amiga que tambi&eacute;n es L&iacute;der del Ma&ntilde;ana de mi generaci&oacute;n no pudo recibir el apoyo el semestre pasado y s&iacute; lo necesita este semestre. Si la pueden considerar para el apoyo, estar&iacute;a muy agradecido. Si no, agradecer&iacute;a como quiera que este espacio se pueda ceder a otro alumno.</em></p><p><em>&nbsp;</em></p><p><em>Muchas gracias.</em></p></td></tr></tbody></table><p>&nbsp;&nbsp;</p><p>Gracia por tu apoyo y deseamos lo mejor para ti este semestre y siempre.</p><p>Saludos con afecto.</p><p>&nbsp;</p><p><strong>Coordinaci&oacute;n Nacional</strong></p><p>Apoyo de Vida</p>'
        body = MIMEText(body, "html", _charset="utf-8")
        msg.set_payload(body)

        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        # Login Credentials for sending the mail
        server.login(EmailManager.fromUser, password)

        server.sendmail("noreply@reddefilantropia.site", msg['To'], msg.as_string())

        server.quit()

        return "successfully sent email to %s:" % (msg['To'])


    @staticmethod
    def sendAnswer(email, saludo="", nombre="", otorgado=0):
        # create message object instance
        fromUser = 'redfilantropia@servicios.itesm.mx'
        passwordUser = 'HoMp(9573'

        msg = MIMEMultipart('alternative')
        msg['To'] = email
        msg['Subject'] = "Apoyo de vida"
        msg.add_header('Content-Type', 'text/html; charset=utf-8')

        if otorgado == 0:
            body = '<p>' + saludo + ' ' + nombre + ':</p><p>Con el gusto de saludarte, y considerando los requisitos establecidos por el programa para la renovaci&oacute;n del Apoyo de Vida de la Red de Filantrop&iacute;a para el per&iacute;odo <strong>enero &ndash; mayo 2019</strong>:</p><ul><li>Ser alumno actual del Tecnol&oacute;gico de Monterrey</li><li>Contar con un apoyo educativo m&iacute;nimo del 70% con comprobaci&oacute;n de necesidad econ&oacute;mica autorizada por Becas.</li><li>Mantener un promedio m&iacute;nimo de 85 en tu desempe&ntilde;o acad&eacute;mico en el semestre agosto-diciembre 2018.</li><li>Haber contado con el beneficio del Apoyo de Vida el semestre agosto-diciembre 2018</li><li>Enviar las formas de registro para la renovaci&oacute;n del apoyo, as&iacute; como el video de 3 minutos donde describes la importancia de este beneficio.</li></ul><p>Hacemos de tu conocimiento que lamentablemente no cubres alguno de los requisitos antes mencionados, por lo que no podr&aacute;s contar con este beneficio durante este semestre.&nbsp;</p><p>Si tienes alguna urgencia o necesitas apoyo, no dudes en comunicarte con nosotros a la direcci&oacute;n: <a href="mailto:redfilantropia@servicios.itesm.mx">redfilantropia@servicios.itesm.mx</a>&nbsp;</p><p>Te deseamos el mayor de los &eacute;xitos en este semestre y nos reiteramos a tus &oacute;rdenes para trabajar juntos en la consecuci&oacute;n de tus objetivos y metas.</p><p>Coordinaci&oacute;n Nacional</p><p>Apoyo de Vida</p><p>Tecnol&oacute;gico de Monterrey</p><p>&nbsp;</p>'
        if otorgado == 1:
            body = '<p>' + saludo + ' ' + nombre + ':</p><p>Con el gusto de saludarte, y considerando los requisitos establecidos por el programa para la renovaci&oacute;n del Apoyo de Vida de la Red de Filantrop&iacute;a para el per&iacute;odo <strong>enero &ndash; mayo 2019</strong>:</p><ul><li>Ser alumno actual del Tecnol&oacute;gico de Monterrey</li><li>Contar con un apoyo educativo m&iacute;nimo del 70% con comprobaci&oacute;n de necesidad econ&oacute;mica autorizada por Becas.</li><li>Mantener un promedio m&iacute;nimo de 85 en tu desempe&ntilde;o acad&eacute;mico en el semestre agosto-diciembre 2018</li><li>Haber contado con el beneficio del Apoyo de Vida el semestre agosto-diciembre 2018</li><li>Enviar las formas de registro para la renovaci&oacute;n del apoyo, as&iacute; como el video de 3 minutos donde describes la importancia de este beneficio.&nbsp;</li></ul><p>Queremos felicitarte, porque toda la informaci&oacute;n solicitada y los requisitos establecidos, los cubriste en tiempo y forma, por lo que no existe inconveniente para extenderte el beneficio de contar por un semestre m&aacute;s con este apoyo.</p><p>Es importante compartir que la sostenibilidad del programa es indispensable para continuar con el apoyo, por lo que el contar con la ayuda en este semestre no garantiza la permanencia en el mismo, ya que el n&uacute;mero de beneficiarios puede variar de acuerdo a la disponibilidad financiera, por lo que te invitamos a que planees tus actividades y nos apoyes a promover el que m&aacute;s personas puedan solidarizarse con esta causa tan importante para algunos de nuestros alumnos.&nbsp;</p><p>Te reitero la direcci&oacute;n electr&oacute;nica a la que podr&aacute;s canalizar a todos aquellos interesados en sumarse a esta causa: <a href="https://crowdfunding.tec.mx/">https://crowdfunding.tec.mx/</a></p><p>El primer dep&oacute;sito lo recibir&aacute;s en tu tarjeta Edenred a m&aacute;s tardar el 15 de febrero y cubrir&aacute; lo correspondiente a los dos primeros meses del a&ntilde;o. En los meses subsecuentes, y hasta el mes de junio, el dinero se depositar&aacute; los primeros 10 d&iacute;as de cada mes.</p><p>Te recordamos que la rendici&oacute;n de cuentas es importante en todo programa, por lo que, para la &uacute;ltima semana del mes de mayo, se requerir&aacute; nos hagas llegar el reporte de actividades sobre lo realizado con este recurso y su impacto en tu vida y tu entorno, para as&iacute; poder recibir el recurso final.</p><p>En espera de que este apoyo contribuya en tu desarrollo acad&eacute;mico, personal y familiar, te deseamos el mayor de los &eacute;xitos en este semestre y nos reiteramos a tus &oacute;rdenes para trabajar juntos en la consecuci&oacute;n de tus objetivos y metas.</p><p>&nbsp;</p><p>Coordinaci&oacute;n Nacional</p><p>Apoyo de Vida</p><p>Tecnol&oacute;gico de Monterrey</p>'

        body = MIMEText(body, "html", _charset="utf-8")
        msg.attach(body)

        server = smtplib.SMTP('smtp-mail.outlook.com: 587')
        server.starttls()

        # Login Credentials for sending the mail
        server.login(fromUser, passwordUser)

        server.sendmail(fromUser, msg['To'], msg.as_string())


        server.quit()

        return "successfully sent email to %s:" % (msg['To'])
