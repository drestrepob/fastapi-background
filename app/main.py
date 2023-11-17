from fastapi import FastAPI, HTTPException

from app.jobs.orders import process_order
from app.queues import orders_queue
from app.schemas import OrderSchema


app = FastAPI(
    title='Restaurant API',
    description='An API for a restaurant that serves various dishes and drinks',
    version='0.1.0',
)


@app.get("/")
def index():
    return {
        'message': 'Welcome to RQ restaurant!'
    }


@app.post("/orders", status_code=202)
def submit_order(order: OrderSchema):
    job = orders_queue.enqueue(process_order, order.dish)
    return {
        'message': f'Order {job.id} submitted.'
    }


@app.get("/orders/{job_id}")
def get_order_status(job_id: str):
    job = orders_queue.fetch_job(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail='Order not found.')
    
    if job.get_status() == 'failed':
        raise HTTPException(status_code=500, detail="Job failed")
    
    if job.get_status() != 'finished':
        return {
            'status': job.get_status()
        }
    
    return {
        'status': job.get_status(),
        'result': job.result,
    }
