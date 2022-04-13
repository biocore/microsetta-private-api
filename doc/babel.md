# To extract and update email translations 

```bash
cd microsetta-private-api
pybabel extract -F ../babel.cfg -o translations/base.pot .
pybabel update -i translations/base.pot -d translations
```

# To generate naive automatic translations

Please see the `naive_translate.py` script as part of `microsetta-interface`
