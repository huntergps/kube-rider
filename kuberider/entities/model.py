import json
from typing import List, Dict

import attr
import cattr

APP_STATE_RECORD_TYPE = "app_state"


@attr.s(auto_attribs=True)
class AppState:
    record_type: str = APP_STATE_RECORD_TYPE
    contexts: List[str] = []
    commands: List[str] = []
    current_context: str = None
    namespaces: List[str] = []
    current_namespace: str = None

    @classmethod
    def from_json(cls, json_obj):
        if not json_obj:
            return cls()
        return cattr.structure(json_obj, cls)

    def to_json(self):
        return cattr.unstructure(self)

    def to_json_str(self):
        return json.dumps(self.to_json())


@attr.s(auto_attribs=True)
class KubeNamespace(object):
    apiVersion: str
    kind: str
    metadata: Dict = {}
    spec: Dict = {}
    status: Dict = {}


@attr.s(auto_attribs=True)
class KubeNamespaces(object):
    apiVersion: str = ""
    kind: str = ""
    metadata: Dict = {}
    items: List[KubeNamespace] = []

    @classmethod
    def from_json_str(cls, json_str):
        if not json_str:
            return cls()
        return cattr.structure(json.loads(json_str), cls)
