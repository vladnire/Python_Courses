# Behavior Driven Python with pytest-bdd

https://testautomationu.applitools.com/behavior-driven-python-with-pytest-bdd/

## Prerequisites

```
pytest
pytest-bdd
selenium
chromedriver.exe (add chromediver to eg: Python\Python39\Scripts\ which need to be added to system path
```

## Usage

```
pytest -v
pytest tests\steps_defs\test_web_steps.py -v
pytest -k "cucumber-basket" --disable-pytest-warnings
pytest -k "duckduckgo" --disable-pytest-warnings
pytest -k "duckduckgo and service" --disable-pytest-warnings
pytest -k "service or web" --disable-pytest-warnings
pytest -k "web" --disable-pytest-warnings
```