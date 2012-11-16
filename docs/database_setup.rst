
# Database setup

Begotemp require PostgreSQL and PostGIS. We recomment you to install
them by using your package manager before continuing.

Begotemp also need psycopg2 python package. If you decide to install it
from python :

> pip install psycopg2

You will need Python and postgreSQL developement files (python-dev libpq-dev on Debian)


## Setup PostgreSQL

On a fresh PostgreSQL install you will probably need to edit ``pg_hba.conf`` to
allow local connection for the database user. Depending on you OS this config
file can be at various place. For example:
``/etc/postgresql/9.1/main`` on Ubuntu
``/var/lib/pgsql/data`` on OpenSUSE

Edit ``pg_hba.conf`` to trust local connections:
> local   all             all                                     trust

And start the postgres server:
> service postgres start


## Create the database

We will create the database as ``postgres`` user:
> sudo -i -u postgres

Now create a database user with will own the database:
> createuser -P begotemp

This will create the user and set his password. For the user rights, we only need
to allow this user to create database:
> Shall the new role be a superuser? (y/n) n
> Shall the new role be allowed to create databases? (y/n) y
> Shall the new role be allowed to create more new roles? (y/n) n

If you prefere you can create the database with postgres and change the database owner later.

Finaly create the database:
> createdb -U begotemp begotemp

## Add PostGIS support to the database

By default, Postgres database do not have PostGIS support. We need to execute
the postGIS sql scripts to do this. The script may be at various place depending on your
package manager.

On Debian/Ubuntu:
> psql -d begotemp -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
> psql -d begotemp -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql

On OpenSUSE:
> psql -d begotemp -f /usr/share/postgresql/contrib/postgis-1.5/postgis.sql
> psql -d begotemp -f /usr/share/postgresql/contrib/postgis-1.5/spatial_ref_sys.sql

This have created two tables in the database: `geometry_columns` & `spatial_ref_sys`
with belong to the `postgres` user. We need them to belong to the database user:
> psql -d begotemp
> begotemp=# ALTER TABLE geometry_columns OWNER TO begotemp;
> begotemp=# ALTER TABLE spatial_ref_sys OWNER TO begotemp;
> \q

## Initialize the database
We only need now to initialize the database with the initialize_anuket_db script:
> initialize_anuket_db development.ini

This create the admin/admin default user.





