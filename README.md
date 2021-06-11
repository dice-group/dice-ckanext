# DICE CKANext

A Python package that implements customizations over [DICE CKAN](https://github.com/dice-group/dice-ckan).

It adds an additional dataset field *Publisher URI*.


### Install ZIP package

```shell
docker exec -u 0 -it ckan bash # as root
apt-get install unzip
```

### Install the extension

```shell
docker exec -it ckan bash
source $CKAN_VENV/bin/activate && cd $CKAN_VENV/src/

wget -O dice-ckanext-master.zip https://github.com/dice-group/dice-ckanext/archive/refs/heads/master.zip

unzip dice-ckanext-master.zip
cd dice-ckanext-master/

python setup.py install
```

### Add the extension to CKAN plugins

```shell
docker exec -it ckan nano /etc/ckan/production.ini
```

Values:

```ini
ckan.plugins = [...] dice
```

### Restart CKAN (e.g.)

```shell
docker-compose restart ckan
```
