class UserAccount:
    """
    DESIGN SMELL 1: Deficient Encapsulation
    This class exposes all its attributes publicly and lacks any encapsulation.
    """
    def __init__(self, username: str, email: str, age: int):
        self.username = username
        self.email = email
        self.age = age
        self.is_active = True
        self.secret_token = "12345"
        
    def reset_token(self):
        self.secret_token = "00000"

class Car:
    """
    DESIGN SMELL 2: Deficient Encapsulation
    This class exposes all its attributes but with car history
    """
    def __init__(self, car_plate: str, car_model: str, car_year: int):
        self.car_plate = car_plate
        self.car_model = car_model
        self.car_year = car_year
        self.car_history = []
    
    def add_car(self, car_plate: str, car_model: str, car_year: int):
        self.car_plate = car_plate
        self.car_model = car_model
        self.car_year = car_year
        
        if self.car_history is None:
            self.car_history = []
            
        self.car_history.append(car_plate)
        
    def get_car_history(self):
        return self.car_history

    
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

    def process_orders_complex(self, orders: list):
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
