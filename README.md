# ckanext-dice-customization

A Python package that implements customizations over the default CKAN.


## Installation

To go into the Docker console:

docker exec -it ckan bash


To install ckanext-dice-customization:

1. Activate your CKAN virtual environment, for example:

    source $CKAN_VENV/bin/activate && cd $CKAN_VENV/src/

2. Remove existing copy, Clone the latest source and install it on the virtualenv

    rm -rf ckanext-dice-customization-master/
    
    rm dice-customization-master.zip
    
    wget -O dice-customization-master.zip https://github.com/tohardik/ckanext-dice-customization/archive/refs/heads/master.zip
    
    unzip dice-customization-master.zip
    
    cd ckanext-dice-customization-master/
    
    pip install -r requirements.txt
    
    python setup.py install
    
    cd ..

3. Add `dice-customization` to the `ckan.plugins` setting in your CKAN
   config file (by default the config file is located at
   `/etc/ckan/default/ckan.ini`).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu:

     sudo service apache2 reload

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
## License

[AGPL](https://www.gnu.org/licenses/agpl-3.0.en.html)
