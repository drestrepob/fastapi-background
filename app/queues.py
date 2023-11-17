from rq import Queue

from app.broker import redis_client


orders_queue = Queue('orders', connection=redis_client)
