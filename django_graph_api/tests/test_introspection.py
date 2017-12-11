from django_graph_api.graphql.schema import (
    DirectiveObject,
    DirectiveLocationEnum,
    EnumValueObject,
    FieldObject,
    InputValueObject,
    SchemaObject,
    TypeObject,
    TypeKindEnum,
)
from django_graph_api.graphql.types import (
    Boolean,
    Int,
    String,
)

from test_app.schema import (
    Character,
    Episode,
    schema,
)


def test_schema__get_types():
    schema_object = SchemaObject(None, schema.query_root, None)

    types = schema_object.get_types()
    assert types == [
        Character,
        Episode,
        DirectiveObject,
        DirectiveLocationEnum,
        EnumValueObject,
        FieldObject,
        InputValueObject,
        SchemaObject,
        TypeObject,
        TypeKindEnum,
        Boolean,
        Int,
        String,
    ]


def test_type__scalar__get_fields():
    type_object = TypeObject(None, Boolean, None)
    assert type_object.get_fields() is None


def test_type__scalar__get_inputFields():
    type_object = TypeObject(None, Boolean, None)
    assert type_object.get_inputFields() is None


def test_type__scalar__get_interfaces():
    type_object = TypeObject(None, Boolean, None)
    assert type_object.get_interfaces() is None


def test_type__scalar__get_possibleTypes():
    type_object = TypeObject(None, Boolean, None)
    assert type_object.get_possibleTypes() is None


def test_type__scalar__get_enumValues():
    type_object = TypeObject(None, Boolean, None)
    assert type_object.get_enumValues() is None


def test_type__object__get_name():
    type_object = TypeObject(None, Character, None)
    assert type_object.get_name() == 'Character'
    type_object = TypeObject(None, TypeObject, None)
    assert type_object.get_name() == '__Type'


def test_type__object__get_fields():
    type_object = TypeObject(None, TypeObject, None)
    assert type_object.get_fields() == [
        ('description', type_object._declared_fields['description']),
        ('enumValues', type_object._declared_fields['enumValues']),
        ('fields', type_object._declared_fields['fields']),
        ('inputFields', type_object._declared_fields['inputFields']),
        ('interfaces', type_object._declared_fields['interfaces']),
        ('kind', type_object._declared_fields['kind']),
        ('name', type_object._declared_fields['name']),
    ]


def test_type__object__get_inputFields():
    type_object = TypeObject(None, TypeObject, None)
    assert type_object.get_inputFields() is None


def test_type__object__get_interfaces():
    type_object = TypeObject(None, TypeObject, None)
    assert type_object.get_interfaces() == []


def test_type__object__get_possibleTypes():
    type_object = TypeObject(None, TypeObject, None)
    assert type_object.get_possibleTypes() is None


def test_type__object__get_enumValues():
    type_object = TypeObject(None, TypeObject, None)
    assert type_object.get_enumValues() is None


def test_type__enum__get_fields():
    type_object = TypeObject(None, TypeKindEnum, None)
    assert type_object.get_fields() is None


def test_type__enum__get_inputFields():
    type_object = TypeObject(None, TypeKindEnum, None)
    assert type_object.get_inputFields() is None


def test_type__enum__get_interfaces():
    type_object = TypeObject(None, TypeKindEnum, None)
    assert type_object.get_interfaces() is None


def test_type__enum__get_possibleTypes():
    type_object = TypeObject(None, TypeKindEnum, None)
    assert type_object.get_possibleTypes() is None


def test_type__enum__get_enumValues():
    type_object = TypeObject(None, TypeKindEnum, None)
    assert type_object.get_enumValues() == TypeKindEnum.values


def test_execute__introspect_directives():
    document = '''{
        __schema {
            directives {
                name
                description
                locations
                args {
                    ...InputValue
                }
            }
        }
    }
    '''
    assert schema.execute(document) == {
        'data': {
            '__schema': {
                'directives': [],
            },
        },
    }
