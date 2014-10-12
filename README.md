## A Basic app built with python and django. 


#### Working CRUD version:
[Playbook](http://radiant-bastion-6945.herokuapp.com)

#### Full-text search version (under development):
[Playbook with search](http://enigmatic-savannah-6878.herokuapp.com/)

This version uses Haystack and Whoosh, but heroku can not seem to build indexes. Files may have to be hosted elsewhere. Code with search functionality is in 'Search' branch.




#### Technologies:
```python
python 2.7.1
django 1.7
postgresql
```

#### Dependencies:

```python
Django==1.7
dj-database-url==0.3.0
dj-static==0.0.6
gunicorn
psycopg2==2.5.4
static3==0.5.1
wsgiref==0.1.2
```