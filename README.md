# DICE CKANext

A Python package that implements customizations over the [DICE CKAN](https://github.com/dice-group/dice-ckan).


## Installation

Install the extension:

```shell
docker exec -it ckan bash
source $CKAN_VENV/bin/activate && cd $CKAN_VENV/src/
# To remove a previous version:
# rm dice-ckanext-master.zip
# rm -rf dice-ckanext
wget -O dice-ckanext-master.zip https://github.com/dice-group/dice-ckanext/archive/refs/heads/master.zip
unzip dice-ckanext-master.zip
mv dice-ckanext-master/ dice-ckanext/
cd dice-ckanext/
python setup.py install
```

Add the extension to CKAN plugins:

```shell
docker exec -it ckan nano /etc/ckan/production.ini
```

Values:

```ini
ckan.plugins = [...] dice-ckanext
```

Restart CKAN (e.g.):

```shell
docker-compose restart ckan
```



<!-- 

## Config settings

None at present

**TODO:** Document any optional config settings here. For example:

	# The minimum number of hours to wait before re-checking a resource
	# (optional, default: 24).
	ckanext.dice_customization.some_setting = some_default_value


## Developer installation

To install ckanext-dice-customization for development, activate your CKAN virtualenv and
do:

    git clone https://github.com/dice-group/ckanext-dice-customization.git
    cd ckanext-dice-customization
    python setup.py develop
    pip install -r dev-requirements.txt


## Tests

To run the tests, do:

    pytest --ckan-ini=test.ini


## Releasing a new version of ckanext-dice-customization

If ckanext-dice-customization should be available on PyPI you can follow these steps to publish a new version:

1. Update the version number in the `setup.py` file. See [PEP 440](http://legacy.python.org/dev/peps/pep-0440/#public-version-identifiers) for how to choose version numbers.

2. Make sure you have the latest version of necessary packages:

    pip install --upgrade setuptools wheel twine

3. Create a source and binary distributions of the new version:

       python setup.py sdist bdist_wheel && twine check dist/*

   Fix any errors you get.

4. Upload the source distribution to PyPI:

       twine upload dist/*

5. Commit any outstanding changes:

       git commit -a
       git push

6. Tag the new release of the project on GitHub with the version number from
   the `setup.py` file. For example if the version number in `setup.py` is
   0.0.1 then do:

       git tag 0.0.1
       git push --tags
 -->