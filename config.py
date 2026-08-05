import pika

# ===============================
# CONFIGURACIÓN RABBITMQ
# ===============================

# RABBITMQ_HOST = "gerbil.rmq.cloudamqp.com"
# RABBITMQ_PORT = 5672
# USERNAME = "etpyjjad"
# PASSWORD = "tNhqawuyTs3W0-pOrL6WpxU1SBCNZ1hb"
# VHOST = "etpyjjad"

RABBITMQ_HOST = "shark.rmq.cloudamqp.com"
RABBITMQ_PORT = 1883
USERNAME = "gxejfhds:gxejfhds"
PASSWORD = "7TGPPF21qN0WLvZP-mumV4iC1cxpCZbs"
VHOST = "gxejfhds" # No se si este VHOST este bien

EXCHANGE = "Taller2"

def get_connection():
    
    #Retorna una conexión configurada a RabbitMQ
    
    credentials = pika.PlainCredentials(USERNAME, PASSWORD)

    parameters = pika.ConnectionParameters(
        host=RABBITMQ_HOST,
        port=RABBITMQ_PORT,
        virtual_host=VHOST,
        credentials=credentials
    )

    return pika.BlockingConnection(parameters)
