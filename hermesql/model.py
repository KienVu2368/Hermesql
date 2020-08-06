import json

class model:
    def __init__(self, model: dict):
        self.tables = model['table']
        self.joins = model['join']
        self.functions = model['function']        
        
    @classmethod
    def from_json_file(cls, file_path):
        f = open(file_path)
        json_file = f
        f.close()
        return cls.from_json(json_file)
        
    @classmethod
    def from_json(cls, json):
        model_dict = json.load(json) 
        return cls(model_dict)
        
    def load_table(self, table_name):
        self.table_alias = self.tables[table_name]['alias']
        fields = self.load_field_from_dict(self.tables[table_name]['field'])
        creteria = self.tables[table_name]['criteria']        
        return (table_name, self.table_alias, fields, creteria)
    
    def load_field_from_dict(self, field_dict):
        fields = {}
        for field in field_dict.keys():
            calculation = field_dict[field]['calculation'] if "calculation" in field_dict[field].keys() else None
            type = field_dict[field]['type']
            fields[field] = self.load_field(field, calculation, type, self.table_alias)         
        return fields
    
    def load_field(self, field_name, calculation, type, table_alias):
        return Field_piece(field_name, calculation, type, table_alias)
    
    def load_join(self, join_name): return None
    
    def load_function(sefl, function_name): return None