# Auto generated from linkml_learning.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-09-13T13:31:35
# Schema: linkml-learning
#
# id: https://w3id.org/my-org/linkml-learning
# description: Just for learning ourpose
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LINKML_LEARNING = CurieNamespace('linkml_learning', 'https://w3id.org/my-org/linkml-learning/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
DEFAULT_ = LINKML_LEARNING


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class FalseId(NamedThingId):
    pass


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = LINKML_LEARNING.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class False(NamedThing):
    """
    Represents a no
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_LEARNING["False"]
    class_class_curie: ClassVar[str] = "linkml_learning:False"
    class_name: ClassVar[str] = "False"
    class_model_uri: ClassVar[URIRef] = LINKML_LEARNING.False

    id: Union[str, FalseId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    vital_status: Optional[Union[str, "PersonStatus"]] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FalseId):
            self.id = FalseId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.vital_status is not None and not isinstance(self.vital_status, PersonStatus):
            self.vital_status = PersonStatus(self.vital_status)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NoCollection(YAMLRoot):
    """
    A holder for no objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = LINKML_LEARNING["NoCollection"]
    class_class_curie: ClassVar[str] = "linkml_learning:NoCollection"
    class_name: ClassVar[str] = "noCollection"
    class_model_uri: ClassVar[URIRef] = LINKML_LEARNING.NoCollection

    entries: Optional[Union[Dict[Union[str, FalseId], Union[dict, False]], List[Union[dict, False]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=False, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=LINKML_LEARNING.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=LINKML_LEARNING.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=LINKML_LEARNING.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=LINKML_LEARNING.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=LINKML_LEARNING.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri=LINKML_LEARNING.age_in_years, name="age_in_years", curie=LINKML_LEARNING.curie('age_in_years'),
                   model_uri=LINKML_LEARNING.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri=LINKML_LEARNING.vital_status, name="vital_status", curie=LINKML_LEARNING.curie('vital_status'),
                   model_uri=LINKML_LEARNING.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.noCollection__entries = Slot(uri=LINKML_LEARNING.entries, name="noCollection__entries", curie=LINKML_LEARNING.curie('entries'),
                   model_uri=LINKML_LEARNING.noCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, FalseId], Union[dict, False]], List[Union[dict, False]]]])

slots.False_primary_email = Slot(uri=SCHEMA.email, name="False_primary_email", curie=SCHEMA.curie('email'),
                   model_uri=LINKML_LEARNING.False_primary_email, domain=False, range=Optional[str],
                   pattern=re.compile(r'^\S+@[\S+\.]+\S+'))