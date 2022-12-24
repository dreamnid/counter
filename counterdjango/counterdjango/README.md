Instructions
---
(Optional) Create a empty `settings_overrides.py` to override any settings (e.g. the mysql key in 
the DATABASES setting)

Be sure to have a `counter_local` database in your MySQL server!
Then run migrations: `poetry run ./manage.py migrate`

To start local dev server: `poetry run ./manage.py runserver localhost:9000`

Open a browser to: http://localhost:9000

### Stress testing notes
`./manage.py runserver` will run in multiple threads by default.

You can use the `--nothreading` to disable this behavior

Alternatively, you can run `poetry run gunicorn counterdjango.wsgi:application -b localhost:9000`
which by default uses 1 worker and 1 thread

### Endpoints

* Redis - `curl -d somedummy http://localhost:9000/hook` - Use redis as storage for counter
* sqlite - `curl -d somedummy http://localhost:9000/hooksqlite` - Use SQLite as storage for counter
* MySQL - `curl -d somedummy http://localhost:9000/hookmysql` - Use MySQL as storage for counter
