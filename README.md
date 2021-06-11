# DICE CKANext

A Python package that implements customizations over [DICE CKAN](https://github.com/dice-group/dice-ckan).

It adds an additional dataset field *Publisher URI*


## Installation

**Install the extension**:

```shell
docker exec -it ckan bash
source $CKAN_VENV/bin/activate && cd $CKAN_VENV/src/

wget -O dice-ckanext-master.zip https://github.com/dice-group/dice-ckanext/archive/refs/heads/master.zip

unzip dice-ckanext-master.zip
mv dice-ckanext-master/ ckanext-dice/
cd ckanext-dice/

python setup.py install
```

**Add the extension to CKAN plugins**:

```shell
docker exec -it ckan nano /etc/ckan/production.ini
```

**Values**:

```ini
ckan.plugins = [...] dice-ckanext
```

Restart CKAN (e.g.):

```shell
docker-compose restart ckan
```
