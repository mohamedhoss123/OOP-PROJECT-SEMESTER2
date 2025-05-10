from data_container import DataContainer
class CategoryData(DataContainer):
    def __init__(self,*args):
        super().__init__()
    def save(self,name):
        self.exec(f"insert into categories(name) values(\"{name}\") ")
        return self.exec("SELECT * FROM categories WHERE id = last_insert_rowid();",fetch=True)[0]
    def delete(self,id):
        self.exec(f"delete from categories where id={id}")
    
    def get_all_categories(self):
        return self.exec("select * from categories",fetch=True)