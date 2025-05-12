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

    def get_all_orders(self):
        return self.exec("SELECT * FROM orders",fetch=True)
    
    def get_selles_in_week(self):
        return self.exec("""
    SELECT date(o.created_at) as date, sum(oi.total) as total
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    WHERE o.created_at >= date('now', '-7 days')
    GROUP BY date(o.created_at)
    ORDER BY date(o.created_at)
""", fetch=True)
