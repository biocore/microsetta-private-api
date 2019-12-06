To generate a new test database:
	python build_db.py

To investigate your new database you can use:
	psql
	\c ag_test			//Switches to the ag_test database
	SET search_path TO ag		//Switches to the ag schema
	\d				//List tables

(Note that if you miss any of these, it looks like your database is empty... but it isn't)
