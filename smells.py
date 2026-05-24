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


    def process_orders_new_complex(self, orders: list):
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

def process_order_and_invoice_and_notify(order_id, user_data, items, discount_code):
    print(f"Starting process for order {order_id}")
    
    # 1. Validation Logic
    if not user_data.get("email") or "@" not in user_data["email"]:
        raise ValueError("Invalid email address")
    if not items:
        raise ValueError("Order must contain items")
        
    # 2. Pricing and Discount Logic
    total_price = 0
    for item in items:
        if item["quantity"] <= 0:
            continue
        item_price = item["price"] * item["quantity"]
        if item.get("category") == "electronics":
            item_price *= 0.95 # 5% electronics discount
        total_price += item_price

    if discount_code:
        if discount_code == "SUMMER20":
            total_price *= 0.8
        elif discount_code == "WELCOME10":
            total_price *= 0.9
        elif discount_code == "VIP_FREE_SHIPPING":
            if total_price > 100:
                print("Applied VIP shipping")
            else:
                total_price += 5
        else:
            print("Invalid discount code")
            total_price += 10 # Default shipping fee
    else:
        total_price += 10

    # 3. Tax Calculation Logic
    country = user_data.get("country", "US")
    if country == "US":
        state = user_data.get("state")
        if state == "CA":
            total_price *= 1.0825
        elif state == "NY":
            total_price *= 1.08875
        else:
            total_price *= 1.05
    elif country == "CA":
        total_price *= 1.12
    else:
        total_price *= 1.20

    # 4. Database & Invoice Generation
    invoice = {
        "id": order_id,
        "user": user_data["email"],
        "amount": round(total_price, 2),
        "date": datetime.datetime.now().strftime("%Y-%m-%d")
    }
    
    # 5. Notification Logic
    try:
        print(f"Sending invoice email to {user_data['email']}...")
        # Simulated email sending logic
        if total_price > 500:
            print("Alerting fraud detection team for high value order")
    except Exception as e:
        print(f"Failed to send email: {e}")
        
    return invoice