echo "Running flake8 linter..."
flake8 . --exclude=venv,__pycache__

echo "Running flake8 lint..."
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

echo "Basic linting complete. Running full report..."
flake8 . --exit-zero --max-complexity=10 --max-line-length=127 --statistics
