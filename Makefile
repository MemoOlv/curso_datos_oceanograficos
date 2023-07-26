all: link1_curso.nc

link1_curso.nc:
	curl https://www.ncei.noaa.gov/data/oceans/ghrsst/L4/GLOB/JPL/MUR25/2014/001/20140101090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc \
	--output link1_curso.nc

otro_ejemplo.nc:
	curl https://www.ncei.noaa.gov/data/oceans/ghrsst/L4/GLOB/JPL/MUR25/2014/002/20140102090000-JPL-L4_GHRSST-SSTfnd-MUR-GLOB-v02.0-fv04.1.nc --output otro_ejemplo.nc


define checkDirectories
mkdir --parents $(@D)
endef

pngtemperatures = \
	figures/temperature_1.png \
	figures/temperature_2.png \
	figures/temperature_3.png \
	figures/temperature_4.png \
	figures/temperature_5.png \
	figures/temperature_6.png \
	figures/temperature_7.png \
	figures/temperature_8.png \
	figures/temperature_9.png \
	figures/temperature_10.png \
	figures/temperature_11.png \
	figures/temperature_12.png


$(pngtemperatures): src/read_mat_files.py
	$(checkDirectories)
	python src/read_mat_files.py


figures/temperature.gif: \
	$(pngtemperatures) \
	src/animation.py
	$(checkDirectories)
	python src/animation.py


.PHONY: \
		all \
		check \
		clean \
		coverage \
		format \
		init \
		install \
		linter \
		mutants \
		setup \
		tests

module = ocean_data

check:
	black --check --line-length 100 ${module}
	black --check --line-length 100 tests
	flake8 --max-line-length 100 ${module}
	flake8 --max-line-length 100 tests
	mypy ${module}
	mypy tests

clean:
	rm --force --recursive .*_cache
	rm --force --recursive ${module}.egg-info
	rm --force --recursive ${module}/__pycache__
	rm --force --recursive tests/__pycache__
	rm --force .mutmut-cache
	rm --force coverage.xml

coverage: setup
	pytest --cov=${module} --cov-report=xml --verbose && \
	coverage report --show-missing

format:
	black --line-length 100 ${module}
	black --line-length 100 src
	black --line-length 100 tests

init: setup tests

install:
	pip install --editable .

linter:
	$(call lint, ${module})
	$(call lint, tests)

mutants: setup
	mutmut run --paths-to-mutate ${module}

setup: clean install

tests:
	pytest --verbose