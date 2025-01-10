# Your code here
# Función para calcular el saldo neto
def net_amount(transactions):
    # Inicializa el saldo neto
    net_balance = 0
    # Divide el registro de transacciones en una lista
    transaction_list = transactions.split()
    
    for i in range(0, len(transaction_list), 2):
        transaction_type = transaction_list[i]
        amount = int(transaction_list[i + 1])
        
        if transaction_type == "D":  # Depósito
            net_balance += amount
        elif transaction_type == "W":  # Retiro
            net_balance -= amount
   
    return net_balance


print(net_amount("D 300 D 300 W 200 D 100"))  