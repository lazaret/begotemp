Begotemp
********
:Author: LDPL - Laboratoire Départemental de Préhistoire du Lazaret
:Version: 0.1a, released 2012-XX-XX
:PyPI:
:License: Expat license (MIT license)
:Docs:
:Source: https://github.com/miniwark/begotemp (Git)
:Bugs: https://github.com/miniwark/begotemp/issues


..warning: COMPLETLY ALPHA STAGE PROJECT



Setup the database
==================

1) Install prerequistes :

postgresql
postgresql-devel
postgis

install the app

> pip install begotemp


2) Configure postgresql

Edit the pg_hba.conf to replace ‘ident’ method by the ‘password’ method in the IPv4 and IPv6
local connection strings (or ‘md5’ if you prefer).

On linux the file is probably located at /var/lib/pgsql/data/pg_hba.conf

The new fille will include line like this :

# IPv4 local connections:
host    all             all             127.0.0.1/32            password
# IPv6 local connections:
host    all             all             ::1/128                 password


3) Start the server

as root
> rcpostgresql start


4) Create the database user role and the database

As root
> su postgres
> createuser -SDRP begotemp
(set the user password at command prompt)
> createdb --owner=begotemp begotemp


6) Add postgis to the database

- For Postgresql >= 9.1 and PostGis >=2.0.0

- For Postgis = 1.5

As postgres user
> psql -d begotemp -f /usr/share/postgresql/contrib/postgis-1.5/postgis.sql
> psql -d begotemp -f /usr/share/postgresql/contrib/postgis-1.5/spatial_ref_sys.sql

7) grant privileges to the owner for the tPostGIS tables

> psql -d begotemp
> ALTER TABLE spatial_ref_sys OWNER TO begotemp;
> ALTER TABLE geometry_columns OWNER TO begotemp;
> \q

7) setup the connectionstring in develpment.ini

# database connection string
sqlalchemy.url = postgresql://begotemp:password@localhost/begotemp


8) Initialize the database

> initialize_anuket_db development.ini


9) test the application

> pserve development.ini

Connect with a browser at http://0.0.0.0:6543/login
with admin/admin credentials

And the try http://0.0.0.0:6543/geo/zone
with normally display an empty list of geographical zones


Note : If necessary to delete the database and the user as postgres user
> dropdb begotemp
> dropuser begotemp
