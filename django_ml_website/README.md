# ModelLab — Django ML Website Starter

A responsive Django website with a homepage and a house-price prediction demo form. The current estimate uses a **simple illustrative formula**, not a trained machine-learning model. It is a starting point for learning how Django handles web requests and forms.

## Run locally

Requires Python 3.10+.

1. Extract the ZIP and open a terminal in the `django_ml_website` folder.
2. Create and activate a virtual environment:

   **Windows (PowerShell)**
   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   ```
   **macOS/Linux**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies: `python -m pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Start the website: `python manage.py runserver`
6. Open http://127.0.0.1:8000/ (prediction form: http://127.0.0.1:8000/predict/).

## Connect your trained ML model

1. Save your trained pipeline/model to a trusted file, such as `predictor/model.joblib`.
2. In `predictor/views.py`, load it using `joblib.load(...)` and replace the clearly marked `DEMO ONLY` formula with `model.predict(...)` using the exact feature order and preprocessing used during training.
3. Save the full preprocessing pipeline along with the estimator when possible. Only load pickle/joblib files from trusted sources because deserialization can execute code.

## Before production deployment

This is a learning starter, not production-hardened. Set `DEBUG = False`, load a strong secret key from environment variables, configure production `ALLOWED_HOSTS`, serve static files properly, use HTTPS, and configure production hosting/database. Do not expose Django's development server to the public internet.
