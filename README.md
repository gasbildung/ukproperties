# ukproperties

This is a simple app that does a very basic analysis on UK property prices for the year 2022.
The API expects a postcode and returns price statistics for given postcode.
The postcode can be specific like `SW1A 2EJ` or non-specific like `SW`

Since this is a flask app you can run it as follows: 

`python app.py`


If you don't have flask installed please do install it using pip as follows:

`pip install flask`

The `logic.py` file checks if the data file exists, if not it downloads it from gov.uk into the `data` folder.

## Components used:

- Python

- Tailwind CSS


## Python libraries used:

- csv

- os

- urllib

- flask


