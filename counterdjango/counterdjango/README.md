Instructions
---
(Optional) Create a empty `settings_overrides.py` to override any settings (e.g. DATABASES)

Be sure to have a `counter_local` database in your MySQL server!
Then run migrations: `poetry run ./manage.py migrate`

To start local dev server: `poetry run ./manage.py run server localhost:9000`
Open a browser to: http://localhost:9000

### Endpoints

* Redis - `curl -d somedummy http://localhost:9000/hook` - Use redis as storage for counter
* sqlite - `curl -d somedummy http://localhost:9000/hooksqlite` - Use SQLite as storage for counter
* MySQL - `curl -d somedummy http://localhost:9000/hookmysql` - Use MySQL as storage for counter
