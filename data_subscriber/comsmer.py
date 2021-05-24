import pika
import time
import database2 as db
import logging
import warnings

logging.basicConfig(format='%(asctime)s %(message)s', level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning) 

connection = pika.BlockingConnection(
      pika.ConnectionParameters(host='172.21.0.1', port=5672))
channel = connection.channel()

channel.queue_declare(queue='hello', durable=True)

def callback(ch, method, properties, body):
    
    message = body.decode("utf-8")
    logging.info('receive messages:' + message)
    time.sleep(body.count(b'.'))
    db.insert(message)

    ch.basic_ack(delivery_tag=method.delivery_tag)
  
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='hello',on_message_callback=callback)
channel.start_consuming()

