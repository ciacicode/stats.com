# Stats.com library

## Installation

# Install a virtual environment, suggested Conda: https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
1. Clone the repository
2. cd to the directory ```/stats.com```
3. Activate your virtual env ```$ source activate <env>```
4. Execute ```pip install -r requirements.txt```

## How to use
Edit the config.py file with your Stats.com API info

~~~~ py
import stats
from config import Config

#instantiate an EPLRequest
EPL = EPLRequest(Config)

params = {'startDate':'20160812', 'endDate':'20160819'}
events = EPL_request.get_events(params)

print events
~~~~

