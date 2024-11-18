run:
	python src/main.py

test:
	pytest tests/

clean:
	find . -name "*.pyc" -delete
