install:
	poetry install
brain-games:
	poetry run brain-games
build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
publish:
	poetry publish --dry-run
init:
	poetry run flake8 brain_games
