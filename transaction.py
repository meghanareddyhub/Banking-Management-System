from database import get_connection 

def deposit_money(account_id, amount):
    if amount <= 0:
        return False
    connection = get_connection()
    cursor = connection.cursor()

    query = """
         update account
        set balance = balance + %s
        where account_id = %s
    """
    cursor.execute(query,(amount,account_id))
    if cursor.rowcount == 0 :
        cursor.close()
        connection.close()
        return False
    
    transaction_query = """
        insert into bank_transaction(account_id,transaction_type,amount) values (%s,'Deposit', %s)
        """
    cursor.execute(transaction_query,(account_id,amount))
    connection.commit()
        
    cursor.close()
    connection.close()
        
    return True

def withdraw_money(account_id,amount):
    if amount <= 0:
        return False
    connection = get_connection()
    cursor = connection.cursor()
    
    query = """
                update account
                set balance = balance - %s
                where account_id = %s and balance >= %s
            """
    cursor.execute(query,(amount,account_id,amount))
    if cursor.rowcount == 0 :
        cursor.close()
        connection.close()
        return False

    transaction_query = """
        insert into bank_transaction(account_id , transaction_type , amount) values (%s, 'Withdrawal' ,%s)
    """
    cursor.execute(transaction_query,(account_id,amount))
    connection.commit()
        
    cursor.close()
    connection.close()
        
    return True

 
def create_account(customer_id,account_type):
    connection = get_connection()
    cursor = connection.cursor()
        
    query = """
                insert into account(customer_id, account_type) values (%s,%s)
        """
    cursor.execute(query,(customer_id, account_type,"1234"))
    connection.commit()
    account_id = cursor.lastrowid
    cursor.close()
    connection.close()
            
    return account_id


def view_transactions(account_id):
    connection = get_connection()
    cursor = connection.cursor()
    
    query = """
                select transaction_type, amount , transaction_date 
                from bank_transaction 
                where account_id = %s
                order by transaction_date desc
            """
    cursor.execute(query,(account_id,))

    transactions = cursor.fetchall()
    cursor.close()
    connection.close()
        
    return transactions




    