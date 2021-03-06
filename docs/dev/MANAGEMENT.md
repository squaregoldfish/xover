
Django management functionality
-------------------------------

Djangos build in management functionality is reached through the d2qc/manage.py
file (se [aliases](ALIASES.md) for shortcuts. Below I use `m` as alias for
./manage.py)

List available functionality (only displaying custom funcitonality here):

```
$ m

[data]
    add_dev_admin_user
    calculate_xover
    cc
    clear_db
    clear_refdata
    db_restore_from_prod
    dbbackup
    import_exc_file
    import_refdata
    init_data_types
```

### For each function under [data] ###

To show the help for functions, use `m help functionname`. Overview of functions
in the data section (more info in the help):

* add_dev_admin_user: adds user: admin, password: 123
* calculate_xover: internal command to calculate crossovers in the background
* cc: clear cache
* clear_db: Drop and restore the database, optionally initialize it
* clear_refdata: Delete all reference data from the database, keeping other data
* db_restore_from_prod: download and restore the prod database to your computer
* dbbackup: backs up your current database
* import_exc_file: Internal function to import file in the background
* import_refdata: Funtionality to import glodap reference data
* init_data_types: Funtionality to initialize data types in the database.
