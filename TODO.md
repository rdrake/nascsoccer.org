# Changes

- Look into adding [fixtures](https://docs.djangoproject.com/en/dev/howto/initial-data/) for data that changes infrequently (parks, locations, age groups, etc.)
  - Consider using South's [data migrations](http://south.readthedocs.org/en/latest/tutorial/part3.html) as per [mpurdon's suggestion](https://github.com/rdrake/nascsoccer.org/commit/6dd989159cbacb882cec6b7ec5ad3912199a365b#commitcomment-4123974)
    - Look at upcoming [1.7 migrations](https://docs.djangoproject.com/en/dev/topics/migrations/) if feeling really adventerous
- Open issues instead of creating difficult to reference and track todo file

# Tools & Libraries

## Testing

- [mock](https://code.google.com/p/mock/)
- [coverage.py](http://nedbatchelder.com/code/coverage/)
- [Nose](https://nose.readthedocs.org/en/latest/)
  - [django-nose](https://pypi.python.org/pypi/django-nose)
- [Jenkins](http://jenkins-ci.org/)
- [Selenium](http://seleniumhq.org)

## Devops

- [Puppet](http://puppetlabs.com/puppet/)
- [Fabric](http://fabfile.org/)
