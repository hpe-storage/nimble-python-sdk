#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#

class Resource:
    __slots__ = ['id', 'attrs', 'collection', '_client']

    def __init__(self, id, attrs=None, client=None, collection=None):
        self.id = id
        self.attrs = {} if attrs is None else attrs
        self.collection = collection

        self._client = client

    def reload(self):
        self.attrs = self.collection.get(self.id).attrs

    def update(self, **kwargs):
        resp = self._client.update_resource(self.collection.resource_type, self.id, **kwargs)
        self.attrs = resp

    def delete(self, **kwargs):
        return self._client.delete_resource(self.collection.resource_type, self.id)

    def __repr__(self):
        if 'name' in self.attrs:
            return f"<{self.__class__.__name__}(id={self.id}, name={self.attrs['name']})>"
        else:
            return f"<{self.__class__.__name__}(id={self.id})>"

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.id == other.id

    def __hash__(self):
        return hash(f"{self.__class__.__name__}:{self.id}")

class Collection:
    __slots__ = ['resource', 'resource_type', '_client']

    def __init__(self, client=None):
        self._client = client

    def get(self, id=None, **kwargs):
        if id is not None:
            obj = self._client.get_resource(self.resource_type, id)
            return self.resource(obj['id'], obj, client=self._client, collection=self)

        elif kwargs is not None:
            objs = self._client.list_resources(self.resource_type, detail=True, **kwargs)
            if len(objs) == 0:
                return None
            else:
                return self.resource(objs[0]['id'] if 'id' in objs[0] else 0, objs[0], client=self._client, collection=self)

    def create(self, name, **kwargs):
        resp = self._client.create_resource(self.resource_type, name=name, **kwargs)
        return self.resource(resp['id'], resp, client=self._client, collection=self)

    def update(self, id, **kwargs):
        resp = self._client.update_resource(self.resource_type, id, **kwargs)
        return self.resource(resp['id'], resp, client=self._client, collection=self)

    def delete(self, id):
        return self._client.delete_resource(self.resource_type, id)

    def list(self, **kwargs):
        objs = self._client.list_resources(self.resource_type, **kwargs)
        return [self.resource(obj['id'] if 'id' in obj else index, obj, client=self._client, collection=self) for index, obj in enumerate(objs)]
