from mysql import connector
from config import db

datatype_mapping = {
    'tinyint': 'byte',
    'smallint': 'short',
    'mediumint': 'int',
    'int': 'int',
    'integer': 'int',
    'bigint': 'long',
    'float': 'float',
    'double': 'double',
    'char': 'String',
    'varchar': 'String',
    'blob': 'String',
    'text': 'String'
}

datatype_nullable_mapping = {
    'tinyint': 'Byte',
    'smallint': 'Short',
    'mediumint': 'Integer',
    'int': 'Integer',
    'integer': 'Integer',
    'bigint': 'Long',
    'float': 'Float',
    'double': 'Double',
    'char': 'String',
    'varchar': 'String',
    'blob': 'String',
    'text': 'String'
}


class Row(object):
    def __init__(self,field,type,nullable):
        self.field = field
        self.nullable = nullable
        tokens = self.field.split('_')
        self.first_uppercase = ''.join(x.capitalize() or '_' for x in tokens)
        if len(tokens) > 1:
            self.camel = tokens[0] + ''.join(x.capitalize() or '_' for x in tokens[1:])
        else:
            self.camel = self.field

        if nullable == 'NO':
            self.type = self.get_type(datatype_mapping, type)
        else:
            self.type = self.get_type(datatype_nullable_mapping, type)

        # name used in ResultSet.getXXXX method
        self.rs_type = self.get_type(datatype_mapping, type).capitalize()
    
    def get_type(self, mapping, type):
        for k,v in mapping.iteritems():
            if(type.startswith(k)):
                return v
        print("unrecognize type:%s" % type)
        return None


def extract_row(tablename):
    con = connector.connect(**db)
    cursor = con.cursor()
    cursor.execute("DESC " + tablename)
    rows = cursor.fetchall()
    return [Row(*r[0:3]) for r in rows]

    
