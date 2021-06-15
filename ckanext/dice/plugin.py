import ckan.plugins as p
import ckan.plugins.toolkit as tk

class DicePlugin(p.SingletonPlugin, tk.DefaultDatasetForm):
    p.implements(p.IDatasetForm)
    p.implements(p.IConfigurer)

    def update_config(self, config_):
        tk.add_template_directory(config_, 'templates')

    def _modify_package_schema(self, schema):
        schema.update({
            'publisher_uri': [tk.get_validator('ignore_missing'),
                            tk.get_converter('convert_to_extras')]
        })
        schema['resources'].update({
            'size' : [ tk.get_validator('ignore_missing') ]
        })
        return schema

    def create_package_schema(self):
        schema = super(DicePlugin, self).create_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def update_package_schema(self):
        schema = super(DicePlugin, self).update_package_schema()
        schema = self._modify_package_schema(schema)
        return schema

    def show_package_schema(self):
        schema = super(DicePlugin, self).show_package_schema()
        schema.update({
            'publisher_uri': [tk.get_converter('convert_from_extras'),
                            tk.get_validator('ignore_missing')]
        })
        schema['resources'].update({
            'size' : [ tk.get_validator('ignore_missing') ]
        })
        return schema

    def is_fallback(self):
        # Return True to register this plugin as the default handler for
        # package types not handled by any other IDatasetForm plugin.
        return True

    def package_types(self):
        # This plugin doesn't handle any special package types, it just
        # registers itself as the default (above).
        return []
