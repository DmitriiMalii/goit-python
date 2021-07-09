import json
import jsonpickle
import pickle
from abc import ABCMeta, abstractclassmethod


class SerializationInterface(metaclass=ABCMeta):
    @abstractclassmethod
    def serialize(self, data):
        pass

    abstractclassmethod
    def deserializese(self, data):
        pass


class SerializationListJson(SerializationInterface):
    def serialize(self, data):
        with open('list.json', 'w') as fh:
            json.dump(data, fh)
    
    def deserialize(self):
        with open('list.json', 'r') as fh:
            return json.load(fh)


class SerializationDictJson(SerializationInterface):
    def serialize(self, data):
        with open('dict.json', 'w') as fh:
            json.dump(data, fh)
    
    def deserialize(self):
        with open('dict.json', 'r') as fh:
            return json.load(fh)


class SerializationTupleJson(SerializationInterface):
    '''Using module jsonpickle for serialize/deserialize tuples'''
    def serialize(self, data):
        with open('tuple.json', 'w') as fh:
            json.dump(jsonpickle.encode(data), fh)
    
    def deserialize(self):
        with open('tuple.json', 'r') as fh:
            return jsonpickle.decode(json.load(fh))


class SerializationSetJson(SerializationInterface):
    '''Using module jsonpickle for serialize/deserialize sets'''
    def serialize(self, data):
        with open('set.json', 'w') as fh:
            json.dump(jsonpickle.encode(data), fh)
    
    def deserialize(self):
        with open('set.json', 'r') as fh:
            return jsonpickle.decode(json.load(fh))


class SerializationListBin(SerializationInterface):
    def serialize(self, data):
        with open('list.bin', 'wb') as fh:
            pickle.dump(data, fh)
    
    def deserialize(self):
        with open('list.bin', 'rb') as fh:
            return pickle.load(fh)


class SerializationDictBin(SerializationInterface):
    def serialize(self, data):
        with open('dict.bin', 'wb') as fh:
            pickle.dump(data, fh)
    
    def deserialize(self):
        with open('dict.bin', 'rb') as fh:
            return pickle.load(fh)


class SerializationTupleBin(SerializationInterface):
    def serialize(self, data):
        with open('tuple.bin', 'wb') as fh:
            pickle.dump(data, fh)
    
    def deserialize(self):
        with open('tuple.bin', 'rb') as fh:
            return pickle.load(fh)


class SerializationSetBin(SerializationInterface):
    def serialize(self, data):
        with open('set.bin', 'wb') as fh:
            pickle.dump(data, fh)
    
    def deserialize(self):
        with open('set.bin', 'rb') as fh:
            return pickle.load(fh)


assert issubclass(SerializationListJson, SerializationInterface)
assert issubclass(SerializationDictJson, SerializationInterface)
assert issubclass(SerializationTupleJson, SerializationInterface)
assert issubclass(SerializationSetJson, SerializationInterface)

assert issubclass(SerializationListBin, SerializationInterface)
assert issubclass(SerializationDictBin, SerializationInterface)
assert issubclass(SerializationTupleBin, SerializationInterface)
assert issubclass(SerializationSetBin, SerializationInterface)

# asserts i/o for json's classes
SerializationListJson().serialize([0, True])
assert SerializationListJson().deserialize() == [0, True]

SerializationDictJson().serialize({'1': 'one', '2': 'two'})
assert SerializationDictJson().deserialize() == {'1': 'one', '2': 'two'}

SerializationTupleJson().serialize(('1', 'one', '2', 'two'))
assert SerializationTupleJson().deserialize() == ('1', 'one', '2', 'two')

SerializationSetJson().serialize({1, 'one', '2', 'two'})
assert SerializationSetJson().deserialize() == {1, 'one', '2', 'two'}

# asserts i/o for pickle's classes
SerializationListBin().serialize([0, True])
assert SerializationListBin().deserialize() == [0, True]

SerializationDictBin().serialize({'1': 'one', '2': 'two'})
assert SerializationDictBin().deserialize() == {'1': 'one', '2': 'two'}

SerializationTupleBin().serialize(('1', 'one', '2', 'two'))
assert SerializationTupleBin().deserialize() == ('1', 'one', '2', 'two')

SerializationSetBin().serialize({1, 'one', '2', 'two'})
assert SerializationSetBin().deserialize() == {1, 'one', '2', 'two'}
