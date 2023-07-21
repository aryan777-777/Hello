"""
Create table Customer(
        cid int primary key auto_increment,
        name text,
        phone text,
        email text
);

  describe Customer;
  insert into Customer values(null, 'john', '34567976543', 'aryan@gmail.com');
  select * from Customer;

"""
import mysql.connector as db
class Customer:
    def __init__(self):
        self.name = input("enter  customer name:")
        self.phone = input("enter the customer phone:")
        self.email = input("enter customer email:")





def main():
    customer = Customer()
    print(vars(customer))

    # database connetivity
    connection = db.connect(user='root',
                            password='',
                            host='122.435.5',
                            database='harry')
    cursor = connection.cursor()
    sql = "insert into Customer values(null, '{name}', '{phone}', '{email}');".format_map(vars(customer))

    cursor.execute(sql)
    connection.commit()

    print("customer inserted...")


if __name__ == "__main__":
    main()