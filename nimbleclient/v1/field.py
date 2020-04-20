#
#   © Copyright 2020 Hewlett Packard Enterprise Development LP
#

def and_(*args):
    ''' Build AND filters '''

    return  {
                'operator': 'and',
                'criteria': list(args)
            }

def or_(*args):
    ''' Build OR filters '''

    return  {
                'operator': 'or',
                'criteria': list(args)
            }

class _Field:
    def __init__(self, name, value=None):
        self.name = name

    def _get_value(self, value):
        if value is True:
            value = 'true'
        elif value is False:
            value = 'false'
        elif value is None:
            value = 'null'
        else:
            value = str(value)
        return value

    def  __eq__(self, value):
        return {"fieldName": self.name, "operator": "equals", "value": self._get_value(value)}

    def __ne__(self, value):
        return {"fieldName": self.name, "operator": "notEqual", "value": self._get_value(value)}

    def __ge__(self, value):
        return {"fieldName": self.name, "operator": "greaterOrEqual", "value": value}

    def __gt__(self, value):
        return {"fieldName": self.name, "operator": "greaterThan", "value": value}

    def __lt__(self, value):
        return {"fieldName": self.name, "operator": "lessThan", "value": value}

    def __le__(self, value):
        return {"fieldName": self.name, "operator": "lessOrEqual", "value": value}

    def __in__(self, value):
        return {"fieldName": self.name, "operator": "iContains", "value": str(value)}

    def __contains__(self, value):
        return {"fieldName": self.name, "operator": "iContains", "value": str(value)}

    def eq(self, value, case_sensitive=True):
        return {"fieldName": self.name, "operator": "equals" if case_sensitive else "iEquals", "value": value}

    def ne(self, value, case_sensitive=True):
        return {"fieldName": self.name, "operator": "notEqual" if case_sensitive else "iNotEqual", "value": value}

    def contains(self, value, case_sensitive=True):
        return {"fieldName": self.name, "operator": "contains" if case_sensitive else "iContains", "value": str(value)}

    def in_set(self, values):
        return {"fieldName": self.name, "operator": "inSet", "values": list(values)}

    def not_in_set(self, values):
        return {"fieldName": self.name, "operator": "notInSet", "values": list(values)}

    def between(self, value1, value2):
        return {"fieldName": self.name, "operator": "between", "value1": value1, "value2": value2}

    def between_inclusive(self, value1, value2):
        return {"fieldName": self.name, "operator": "betweenInclusive", "value1": value1, "value2": value2}

    def regex(self, value):
        return {"fieldName": self.name, "operator": "regexp", "value": str(value)}

    def __str__(self):
        return self.name
