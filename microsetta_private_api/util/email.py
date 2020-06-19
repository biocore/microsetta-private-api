import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from microsetta_private_api.config_manager import SERVER_CONFIG


class SendEmail:
    host = SERVER_CONFIG.get('smtp_host', 'localhost')
    user = SERVER_CONFIG.get('smtp_user')
    port = SERVER_CONFIG.get('smtp_port', 0)
    password = SERVER_CONFIG.get('smtp_password')
    reconnect_attempts = SERVER_CONFIG.get('smtp_reconnect_attempts', 3)

    from_ = 'no-reply@microsetta.ucsd.edu'
    reply_to = 'microsetta@ucsd.edu'
    connection = None

    @staticmethod
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
    def send(cls, to, email_template, **email_template_args):
        """Send a message

        Parameters
        ----------
        to : str
            The email address to send a message too
        email_template : EmailTemplate
            An object that contains a .plain and .html jinja2
            template for rendering
        email_template_args : dict, optional
            Arguments to provide for rendering. If "from" is included
            in the arguments, it is extracted and used as the "from"
            address in sending the email
        """
        from_ = email_template_args.pop('from', None)

        message = MIMEMultipart("alternative")
        message['To'] = to
        message['From'] = from_ or cls.from_
        message['Reply-To'] = cls.reply_to
        message['Subject'] = email_template.subject

        plain = email_template.plain.render(**email_template_args)
        html = email_template.html.render(**email_template_args)

        first = MIMEText(plain, "plain")
        second = MIMEText(html, "html")

        message.attach(first)
        message.attach(second)

        cls.connect()
        cls.connection.send_message(message)
