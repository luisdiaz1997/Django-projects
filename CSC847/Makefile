CONDA_ACTIVATE=source $$(conda info --base)/etc/profile.d/conda.sh ; conda activate ; conda activate
SHELL=/bin/bash

all:
	@echo "make build: sets up the environment"
	@echo "make run: runs the website"

build:
	@conda env create -f CSC847.yml
	($(CONDA_ACTIVATE) django; npm install -g @vue/cli @vue/cli-service-global )

