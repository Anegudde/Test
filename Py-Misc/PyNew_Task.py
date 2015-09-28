#!/usr/bin/env python
import pika
import sys
import logging
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.CRITICAL)


'''
credentials = pika.PlainCredentials('<user>', '<password>')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost', 5672, '/', credentials))
channel = connection.channel()
'''

connection = pika.AsyncoreConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='', routing_key='task_queue', body=message,properties=pika.BasicProperties(delivery_mode = 2, # make message persistent
		))
print " [x] Sent %r" % (message,)