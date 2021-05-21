from builtins import str
from ckanext.dcat.profiles import RDFProfile

from rdflib import URIRef, BNode, Literal
from rdflib.namespace import Namespace, RDF, RDFS

DCT = Namespace("http://purl.org/dc/terms/")


class DICEDCATProfile(RDFProfile):
    '''
    An RDF profile for the Swedish DCAT-AP recommendation for data portals

    It requires the European DCAT-AP profile (`euro_dcat_ap`)

    TODO: this is a skeleton for customizations related to DCAT serialization.
     The customizations are made by extending RDFProfile class (part of DCAT
     extension - https://github.com/ckan/ckanext-dcat). Methods parse_dataset
     and graph_from_dataset handle deserialization (TTL -> Dataset) and
     serialization (Dataset -> TTL) respectively. Unfinished due to debugging issues.

    '''

    def parse_dataset(self, dataset_dict, dataset_ref):

        # Spatial label
        # spatial = self._object(dataset_ref, DCT.spatial)
        # if spatial:
        #     spatial_label = self.g.label(spatial)
        #     if spatial_label:
        #         dataset_dict['extras'].append({'key': 'spatial_text',
        #                                        'value': str(spatial_label)})

        return dataset_dict

    def graph_from_dataset(self, dataset_dict, dataset_ref):
        g = self.g
        print "-------------------------- running main dataset_dict"
        print dataset_dict

        # g = self.g
        #
        # spatial_uri = self._get_dataset_value(dataset_dict, 'spatial_uri')
        # spatial_text = self._get_dataset_value(dataset_dict, 'spatial_text')
        #
        # if spatial_uri:
        #     spatial_ref = URIRef(spatial_uri)
        # else:
        #     spatial_ref = BNode()
        #
        # if spatial_text:
        #     g.add((dataset_ref, DCT.spatial, spatial_ref))
        #     g.add((spatial_ref, RDF.type, DCT.Location))
        #     g.add((spatial_ref, RDFS.label, Literal(spatial_text)))


# Debug
o = DICEDCATProfile()
o.graph_from_dataset({'a': 1, 'b': 6}, None)
