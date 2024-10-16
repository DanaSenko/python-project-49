install:
	poetry install

build:
	poetry build
	
package-install:
	python3 -m pip install dist/*.whl

brain-games:	
	poetry run brain-games

brain-calc:
	poetry run brain-calc

brain-even:
	poetry run brain-even

brain-gcd:
	poetry run brain-gcd

brain-prime:
	poetry run brain-prime

brain-progression:
	poetry run brain-progression

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games

