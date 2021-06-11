import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.utils import formataddr
import html2text

from microsetta_private_api.config_manager import SERVER_CONFIG


class SendEmail:
    host = SERVER_CONFIG.get('smtp_host', 'localhost')
    user = SERVER_CONFIG.get('smtp_user')
    port = SERVER_CONFIG.get('smtp_port', 0)
    password = SERVER_CONFIG.get('smtp_password')
    reconnect_attempts = SERVER_CONFIG.get('smtp_reconnect_attempts', 3)

    from_ = formataddr(('The Microsetta Initiative',
                        'no-reply@microsetta.ucsd.edu'))
    reply_to = formataddr(('The Microsetta Initiative',
                           'microsetta@ucsd.edu'))
    connection = None

    @classmethod
    def _connect(cls):
        """Establish a SMTP connection"""
        connection = smtplib.SMTP(cls.host, port=cls.port)
        if cls.user is not None:
            connection.login(cls.user, cls.password)
        return connection

    @classmethod
    def connect(cls):
        """Connect or reconnect if a connection has timed out"""
        def reconnect():
            if cls.connection is None or cls.connection.noop()[0] == 421:
                return True
            else:
                return False

        count = 0
        for i in range(cls.reconnect_attempts + 1):
            if reconnect():
                count += 1
                cls.connection = cls._connect()
            else:
                break

        if count > cls.reconnect_attempts:
            raise smtplib.SMTPException("Unable to connect")

    @classmethod
    def send(cls, to, email_template, email_template_args=None, from_=None,
             attachment_filepath=None, attachment_filename=None):
        """Send a message

        Parameters
        ----------
        to : str
            The email address to send a message too
        email_template : EmailTemplate
            An object that contains a .html jinja2
            template for rendering
        email_template_args : dict, optional
            Arguments to provide for rendering.
        from_ : str, optional
            A from email address. This is optional, and if not provided
            the default defined by this class is used.
        attachment_filepath : str, optional
            A path to a file to attach. If specified, it is necessary for the
            file to exist, and it is also necessary to provide a
            "attachment_filename"
        attachment_filename : str, optional
            The name of the attachment within the email. If
            "attachment_filepath" is specified, it is necessary to also include
            a value here.
        """
        if attachment_filepath is not None or attachment_filename is not None:
            assert attachment_filepath is not None and \
                    attachment_filename is not None

        message = MIMEMultipart("alternative")
        message['To'] = to
        message['From'] = from_ or cls.from_
        message['Reply-To'] = cls.reply_to
        message['Subject'] = email_template.subject

        html = email_template.html.render(email_template_args or {})
        plain = html2text.html2text(html)

        first = MIMEText(plain, "plain")
        second = MIMEText(html, "html")

        message.attach(first)
        message.attach(second)

        if attachment_filepath:
            with open(attachment_filepath, 'rb') as f:
                data = f.read()
                attachment = MIMEApplication(data, Name=attachment_filename)
            disposition = f'attachment; filename="{attachment_filename}"'
            attachment['Content-Disposition'] = disposition
            message.attach(attachment)

        cls.connect()
        cls.connection.send_message(message)
