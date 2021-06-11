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

`docker volume inspect docker_ckan_home`  
`ls /var/lib/docker/volumes/docker_ckan_home/_data`  
`cp -r /var/lib/docker/volumes/docker_ckan_home/_data/venv/src/ckanext-dice/ ~/DICE/git/dice-ckanext/`




## TODO




https://docs.ckan.org/en/2.9/extensions/adding-custom-fields.html
