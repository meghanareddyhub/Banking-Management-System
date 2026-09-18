from database import get_connection 

def check_balance(account_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        select balance
        from account
        where account_id = %s
    """
    cursor.execute(query,(account_id,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    if result is None :
        return None

    return result[0]

def verify_password(account_id , password):
    connection = get_connection()
    cursor = connection.cursor()
    query = """
            select password
            from account
            where account_id = %s
        """
    cursor.execute(query,(account_id,))
    
    result = cursor.fetchone()
    
    cursor.close()
    connection.close()
    
    if result is None :
            return None
    
    return result[0] == password 

def view_my_details(account_id):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
    select c.full_name, c.phone, c.email, c.address, a.account_id 
    from customer c 
    join account a ON c.customer_id = a.customer_id 
    where a.account_id = %s """

    cursor.execute(query,(account_id,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()

    return result 

def create_customer(full_name,phone,email,address):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        insert into customer(full_name,phone,email,address) values (%s,%s,%s,%s)
    """
    cursor.execute(query,(full_name,phone,email,address))
    connection.commit()
    customer_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return customer_id

