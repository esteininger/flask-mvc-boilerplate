# Podcast-Word-Cloud
This is a Flask MVC boilerplate that includes:

  - Sentry logging with conditionals of live vs local 
  - Login required decorator
  - SQLAlchemy & MongoDB ready
  - Models, Views, Controllers (Routes) structured via blueprints
  - Route method (success vs error) handling
  - Mailer class
  - Configuration file

### Installation

This app requires Python 3+ to run, so install that first

1. Install the dependencies:

```python
pip install -r requirements.txt
```

2. Add your corresponding keys and environment variables in config.py

3. Run:

```python
python run.py
```


I welcome pull requests, as I'd help addressing the following enhancements:

  - More context in Sentry logs
  - MongoDB via ORM within env variables similar to SQLAlchemy
