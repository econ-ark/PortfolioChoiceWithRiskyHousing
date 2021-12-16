#!/bin/bash
# install the versioned required packages
python3 -m pip install --quiet -r binder/requirements.txt

# navigate to code/ and execute the python file to create figures
cd ./code/python
jupyter nbconvert --to python PortfolioChoiceWithRiskyHousing.ipynb
ipython PortfolioChoiceWithRiskyHousing.py


