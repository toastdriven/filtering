M2M Filtering
=============

To replicate:

* Clone this repo.
* Use a virtualenv (or symlink in tastypie).
* ``./manage.py syncdb``
* ``./manage.py loaddata base_data``
* ``./manage.py runserver``

* In browser:
  * Hit http://localhost:8000/api/v1/parent/?format=json - there should be two
    parents there. (Same as your setup)
  * Hit http://localhost:8000/api/v1/child/?format=json - there should be three
    children there. (Same as your setup)
  * Hit http://localhost:8000/api/v1/child/?format=json&parents=1 - there should
    be **ONLY** two children there, both of which have ``/api/v1/parent/1/`` in
    their ``parents`` field.
  * Hit http://localhost:8000/api/v1/child/?format=json&parents=2 - there should
    be **ONLY** two children there, both of which have ``/api/v1/parent/2/`` in
    their ``parents`` field.
  * Hit http://localhost:8000/api/v1/child/?format=json&parents=3 - there should
    be no children (because that parent doesn't exist).
