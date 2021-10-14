PYENV=env
PYTHON=$(PYENV)/bin/python3

.PHONY: clean

netcdf: $(PYENV)/bin/activate files.txt
	$(PYTHON) scripts/retrieve_netcdf_files.py -f files.txt -o netcdf

$(PYENV)/bin/activate: requirements.txt
	test -d $(PYENV) || python3 -m venv $(PYENV)
	$(PYTHON) -m pip install -U pip wheel
	$(PYTHON) -m pip install -r requirements.txt
	touch $(PYENV)/bin/activate

clean:
	rm -rf $(PYENV) netcdf
