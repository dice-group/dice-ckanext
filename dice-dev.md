# Development: ckanext-dice

## Access docker

`docker exec -it ckan bash`  
`source $CKAN_VENV/bin/activate && cd $CKAN_VENV/src/`

## Creating extension

https://docs.ckan.org/en/2.9/extensions/tutorial.html

`ckan generate extension`  
> `cookiecutter` library is missing from import path.  
> Make sure you have dev-dependencies installed:  
> pip install -r dev-requirements.txt

http://localhost:5000/api/3/action/status_show  
> "ckan_version": "2.9.2"

`pip install -r https://raw.githubusercontent.com/ckan/ckan/ckan-2.9.2/dev-requirements.txt`

> Extension's name [must begin 'ckanext-']: ckanext-dice  
> Author's name []: DICE  
> Author's email []:  
> Your Github user or organization name []:  
> Brief description of the project []:  
> List of keywords (separated by spaces) [CKAN]:  
> Written: /usr/lib/ckan/venv/src/ckanext-dice

## Backup extension

The last command can be used to copy a running extension version from docker to git.

`docker volume inspect docker_ckan_home`  
`ls /var/lib/docker/volumes/docker_ckan_home/_data`  
`cp -r /var/lib/docker/volumes/docker_ckan_home/_data/venv/src/ckanext-dice/* ~/DICE/git/dice-ckanext/`

## Installation test

`docker exec -it ckan bash`  
`source $CKAN_VENV/bin/activate && cd $CKAN_VENV/src/`  
`cd ckanext-dice/`  
`python setup.py develop`

## Adding field

https://docs.ckan.org/en/2.9/extensions/adding-custom-fields.html

`sudo chmod -R o+w /var/lib/docker/volumes/docker_ckan_home/_data/venv/src/ckanext-dice/`  
`pluma /var/lib/docker/volumes/docker_ckan_home/_data/venv/src/ckanext-dice/ckanext/dice/plugin.py`  
Created 3 templates in ckanext/dice/templates/package/snippets

## Add extension

`docker exec -u 0 -it ckan bash # as root`  
`apt-get update ; apt-get install nano`

`docker exec -it ckan nano /etc/ckan/production.ini`  
`ckan.plugins = [...] dice`
