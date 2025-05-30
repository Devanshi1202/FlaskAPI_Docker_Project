echo "Running flake8 lint checks..."

flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics

echo "Running full flake8 report..."
flake8 . --exit-zero --max-complexity=10 --max-line-length=127 --statistics
