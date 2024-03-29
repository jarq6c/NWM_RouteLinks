PYENV=env
PYTHON=$(PYENV)/bin/python3

.PHONY: clean

all: RouteLink.h5 RouteLinks.tar.gz

RouteLink.h5: csv
	$(PYTHON) scripts/make_hdf.py -i csv -o RouteLink.h5

RouteLinks.tar.gz: csv
	tar -czvf RouteLinks.tar.gz csv

csv: $(PYENV)/bin/activate netcdf
	$(PYTHON) scripts/make_csv.py -i netcdf -o csv

netcdf: $(PYENV)/bin/activate files.txt
	$(PYTHON) scripts/retrieve_netcdf_files.py -f files.txt -o netcdf

$(PYENV)/bin/activate: requirements.txt
	test -d $(PYENV) || python3 -m venv $(PYENV)
	$(PYTHON) -m pip install -U pip wheel
	$(PYTHON) -m pip install -r requirements.txt
	touch $(PYENV)/bin/activate

all-clean: clean
	rm -rf RouteLink.h5 RouteLinks.tar.gz

clean:
	rm -rf $(PYENV) netcdf csv
