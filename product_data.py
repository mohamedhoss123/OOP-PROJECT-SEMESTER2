from data_container import DataContainer
class ProductData(DataContainer):
    def __init__(self):
        super().__init__()
    
    def save(self, name: str, price: float, category_id: int) -> list:
        self.exec(f"insert into products(name,price,category_id) values(\"{name}\",\"{price}\",\"{category_id}\") ")
        return self.exec("SELECT * FROM products WHERE id = last_insert_rowid();", fetch=True)[0]
    
    def get_all_products(self):
        return self.exec("select * from products", fetch=True)
    
    def delete(self, id):
        self.exec(f"delete from products where id={id}")
        
    def get_products_by_category(self, category_id):
        return self.exec(f"select * from products where category_id={category_id}", fetch=True)