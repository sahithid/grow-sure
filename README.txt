Runnning the Flask App (BACKEND)
    1. Install the necessary packages in the requirements.txt file
            (pip install -r requirements.txt)
        
    2. Run the app.py file by executing the following code 
            (python backend/app.py)

Running the Vue CLI (FRONTEND)
    1. Go to the frontend directory in a fresh terminal
        (cd frontend)
    2. Run the Vue CLI 
        (npm run serve)

Running Celery Scheduled Tasks 
    1. Run Redis Server 
        (redis-server)

    2. Running Celery Worker inside /backend
        (celery -A app:celery_app worker --loglevel=INFO --pool=solo)

    3. Running Celery Beat (scheduled tasks) inside /backend
        ((celery -A app:celery_app beat --loglevel=INFO))
    
    
