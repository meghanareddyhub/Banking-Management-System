import mysql.connector

def get_connection():
    connection = mysql.connector.connect(
        host ="localhost",
        user ="root",
        password ="Nova@123",
        database ="nova_bank"
    )
    return connection


