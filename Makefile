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
lint:
	poetry run flake8 brain_games
force:
	python3 -m pip install --user --force-reinstall dist/*.whl
brain-even:
	poetry run brain-even
brain-calc:
	poetry run brain-calc
brain-progression:
	poetry run brain-progression
aci:
	asciinema rec
