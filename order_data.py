from data_container import DataContainer

class OrderData(DataContainer):
    def __init__(self):
        super().__init__()
    
    def create_order(self):
        self.exec("insert into orders(created_at) values(datetime('now'))")
        return self.exec("SELECT last_insert_rowid();",fetch=True)[0][0]
    def save_order_items(self,order_number,order_items):
        for i in order_items:
            self.exec(f"insert into order_items(product_id,quantity,total,order_id) values({i[0]},{i[2]},{i[2]*i[3]},{order_number})")
            print(i)

    def get_all_orders(self):
        pass
    
