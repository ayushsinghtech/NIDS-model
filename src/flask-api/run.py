# run.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Run the Flask app on 0.0.0.0 so it's accessible from Docker (if needed)
    app.run(debug=True, host="0.0.0.0", port=5000)
