class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        # Intended as internal/protected. dpy registers this intent.
        self._balance = balance 

    def withdraw(self, amount: float):
        if amount <= self._balance:
            self._balance -= amount


class ATMService:
    def __init__(self):
        self.total_dispensed = 0.0

    def process_payout(self, account: BankAccount, cash_amount: float):
        # VIOLATION: Directly accessing a non-public field (_balance) 
        # instead of calling a public method or property.
        if account._balance >= cash_amount:
            account._balance -= cash_amount
            self.total_dispensed += cash_amount

    
class UtilityManager:
    """
    DESIGN SMELL 2: Multifaceted Abstraction (or God Class)
    This class handles completely unrelated responsibilities: 
    database connection, email sending, logging, and string manipulation.
    """
    def __init__(self):
        self.db_connected = False

    def connect_db(self):
        self.db_connected = True

    def send_email(self, to_addr: str, message: str):
        print(f"Sending {message} to {to_addr}")

    def log_error(self, error_msg: str):
        with open("error.log", "a") as f:
            f.write(error_msg + "\n")

    def reverse_string(self, s: str) -> str:
        return s[::-1]
        
    def calculate_tax(self, amount: float) -> float:
        return amount * 0.2


class OrderProcessor:
    def __init__(self):
        self.orders = []

    def process_orders_still_complex(self, orders: list):
        """
        IMPLEMENTATION SMELL 1: Complex Method
        Extremely high cyclomatic complexity with deeply nested loops and branches.
        """
        for order in orders:
            if order.get("is_valid"):
                if order.get("type") == "physical":
                    if order.get("weight", 0) > 10:
                        if order.get("destination") == "international":
                            order["shipping_cost"] = 50
                        else:
                            order["shipping_cost"] = 20
                    else:
                        order["shipping_cost"] = 5
                elif order.get("type") == "digital":
                    if order.get("subscription"):
                        order["recurring"] = True
                    else:
                        order["recurring"] = False
                else:
                    if order.get("special"):
                        pass
            else:
                if order.get("status") == "pending":
                    pass
                elif order.get("status") == "cancelled":
                    pass

    def process_order_long(self, order_id: str):
        """
        IMPLEMENTATION SMELL 2: Long Method
        This method is artificially inflated to be very long.
        """
        step = 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        step += 1
        print(f"Executing step {step}")
        
        return step
