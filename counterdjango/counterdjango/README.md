Instructions
---
(Optional) Create a empty `settings_overrides.py` to override any settings (e.g. DATABASES)

Be sure to have a `counter_local` database in your MySQL server!
Then run migrations: `poetry run ./manage.py migrate`

To start local dev server: `poetry run ./manage.py run server localhost:9000`
Open a browser to: http://localhost:9000
