class Product:
    """Represents a product available on the website."""

    def __init__(self, product_id, name, category, price, stock):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        """Increase or decrease stock."""
        self.stock += quantity

    def is_available(self, quantity):
        """Check whether requested quantity is available."""
        return self.stock >= quantity

    def display_product(self):
        """Display product details."""
        print("-" * 45)
        print(f"Product ID : {self.product_id}")
        print(f"Name       : {self.name}")
        print(f"Category   : {self.category}")
        print(f"Price      : ₹{self.price}")
        print(f"Stock      : {self.stock}")
        print("-" * 45)

# 2

class Website:
    """Parent class for all users of the shopping website."""

    website_name = "BigBasket"

    def __init__(self, username):
        self.username = username
        self.logged_in = False

    def login(self):
        self.logged_in = True
        print(f"\nWelcome {self.username}!")
        print(f"Successfully logged into {Website.website_name}.")

    def logout(self):
        self.logged_in = False
        print(f"\n{self.username} logged out successfully.")

    def search_product(self, products, keyword):
        """Search products by name."""
        print("\nSearch Results")

        found = False

        for product in products:
            if keyword.lower() in product.name.lower():
                product.display_product()
                found = True

        if not found:
            print("No matching product found.")

    def display_all_products(self, products):
        """Display all available products."""

        print("\nAvailable Products")

        for product in products:
            product.display_product()

# 3
class Customer(Website):
    """Represents a customer using the shopping website."""

    def __init__(self, username, password, phone, address):
        super().__init__(username)

        self.__password = password
        self.__phone = phone
        self.__address = address
        self.__wallet = 0

    # -----------------------------
    # Encapsulation Methods
    # -----------------------------

    def verify_password(self, password):
        return self.__password == password

    def change_password(self, old_password, new_password):

        if self.__password == old_password:
            self.__password = new_password
            print("Password changed successfully.")
        else:
            print("Incorrect old password.")

    def add_money(self, amount):

        if amount > 0:
            self.__wallet += amount
            print(f"₹{amount} added successfully.")

    def deduct_money(self, amount):

        if amount <= self.__wallet:
            self.__wallet -= amount
            return True

        return False

    def show_wallet(self):
        print(f"Wallet Balance : ₹{self.__wallet}")

    def show_profile(self):

        print("\nCustomer Profile")
        print("-" * 40)
        print(f"Username : {self.username}")
        print(f"Phone    : {self.__phone}")
        print(f"Address  : {self.__address}")
        print(f"Wallet   : ₹{self.__wallet}")
        print("-" * 40)

    def update_address(self, new_address):
        self.__address = new_address
        print("Address updated successfully.")

    def browse_products(self, products):
        self.display_all_products(products)


# 5
class Admin(Website):
    """Represents an administrator of the shopping website."""

    def __init__(self, username, password):
        super().__init__(username)
        self.__password = password

    # -----------------------------
    # Login Verification
    # -----------------------------

    def verify_password(self, password):
        return self.__password == password

    # -----------------------------
    # Product Management
    # -----------------------------

    def add_product(self, products, product):

        products.append(product)

        print(f"\n'{product.name}' added successfully.")

    def remove_product(self, products, product_id):

        for product in products:

            if product.product_id == product_id:
                products.remove(product)
                print(f"\n'{product.name}' removed successfully.")
                return

        print("\nProduct not found.")

    def update_stock(self, products, product_id, quantity):

        for product in products:

            if product.product_id == product_id:

                product.update_stock(quantity)

                print(f"\nStock updated successfully.")
                print(f"Current Stock : {product.stock}")

                return

        print("\nProduct not found.")

    def update_price(self, products, product_id, new_price):

        for product in products:

            if product.product_id == product_id:

                product.price = new_price

                print(f"\nPrice updated successfully.")
                print(f"New Price : ₹{new_price}")

                return

        print("\nProduct not found.")

    def view_products(self, products):
        self.display_all_products(products)


# 6
class DeliveryPartner(Website):
    """Represents a delivery partner."""

    def __init__(self, username, phone):

        super().__init__(username)

        self.phone = phone
        self.current_orders = []

    # -----------------------------
    # Order Management
    # -----------------------------

    def accept_order(self, order_id):

        self.current_orders.append(order_id)

        print(f"\nOrder {order_id} accepted.")

    def deliver_order(self, order_id):

        if order_id in self.current_orders:

            self.current_orders.remove(order_id)

            print(f"\nOrder {order_id} delivered successfully.")

        else:

            print("\nOrder not assigned.")

    def update_status(self, order_id, status):

        print(f"\nOrder {order_id}")
        print(f"Status Updated : {status}")

    def view_orders(self):

        print("\nAssigned Orders")

        if len(self.current_orders) == 0:

            print("No active deliveries.")

        else:

            for order in self.current_orders:
                print(order)


# 8
class Cart:
    """Represents a customer's shopping cart."""

    def __init__(self):
        # Encapsulation
        self.__items = {}

    # -----------------------------
    # Add Product
    # -----------------------------
    def add_product(self, product, quantity):

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        if not product.is_available(quantity):
            print(f"Only {product.stock} '{product.name}' available.")
            return

        if product in self.__items:
            self.__items[product] += quantity
        else:
            self.__items[product] = quantity

        print(f"{quantity} x {product.name} added to cart.")

    # -----------------------------
    # Remove Product
    # -----------------------------
    def remove_product(self, product):

        if product in self.__items:
            del self.__items[product]
            print(f"{product.name} removed from cart.")
        else:
            print("Product not found in cart.")

    # -----------------------------
    # Update Quantity
    # -----------------------------
    def update_quantity(self, product, quantity):

        if product not in self.__items:
            print("Product not found.")
            return

        if quantity <= 0:
            self.remove_product(product)
            return

        if not product.is_available(quantity):
            print(f"Only {product.stock} available.")
            return

        self.__items[product] = quantity

        print(f"{product.name} quantity updated.")

    # -----------------------------
    # Total Amount
    # -----------------------------
    def calculate_total(self):

        total = 0

        for product, quantity in self.__items.items():
            total += product.price * quantity

        return total

    # -----------------------------
    # Display Cart
    # -----------------------------
    def display_cart(self):

        print("\n========== YOUR CART ==========")

        if not self.__items:
            print("Cart is Empty.")
            return

        for product, quantity in self.__items.items():

            subtotal = product.price * quantity

            print(
                f"{product.name:15}"
                f"Qty:{quantity:<3}"
                f"Price: ₹{product.price:<5}"
                f"Subtotal: ₹{subtotal}"
            )

        print("--------------------------------")
        print(f"Total Amount : ₹{self.calculate_total()}")
        print("================================")

    # -----------------------------
    # Empty Cart
    # -----------------------------
    def clear_cart(self):

        self.__items.clear()

        print("Cart cleared successfully.")

    # -----------------------------
    # Getter
    # -----------------------------
    def get_items(self):
        return self.__items

    # ==================================================
    # POLYMORPHISM (Operator Overloading)
    # ==================================================

    def __add__(self, other):

        """Merge two carts using + operator."""

        new_cart = Cart()

        for product, quantity in self.__items.items():
            new_cart._Cart__items[product] = quantity

        for product, quantity in other.__items.items():

            if product in new_cart._Cart__items:
                new_cart._Cart__items[product] += quantity
            else:
                new_cart._Cart__items[product] = quantity

        return new_cart

    def __len__(self):

        """Returns total number of products."""

        return len(self.__items)

    def __contains__(self, product):

        """Enables: product in cart"""

        return product in self.__items

    def __str__(self):

        """Nicely prints the cart."""

        if not self.__items:
            return "Cart is Empty."

        output = "\n========== CART ==========\n"

        for product, quantity in self.__items.items():

            subtotal = product.price * quantity

            output += (
                f"{product.name} "
                f"x {quantity} "
                f"= ₹{subtotal}\n"
            )

        output += "-------------------------\n"
        output += f"Total = ₹{self.calculate_total()}"

        return output


# 10
from abc import ABC, abstractmethod

class Payment(ABC):
    """Abstract Base Class for all payment methods."""

    @abstractmethod
    def pay(self, amount):
        """Process the payment."""
        pass

    @abstractmethod
    def refund(self, amount):
        """Refund the payment."""
        pass


# 11
class UPIPayment(Payment):
    """UPI Payment Method."""

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print("\n----- UPI PAYMENT -----")
        print(f"UPI ID : {self.upi_id}")
        print(f"Amount : ₹{amount}")
        print("Payment Successful using UPI.")

    def refund(self, amount):
        print(f"₹{amount} refunded to {self.upi_id}.")


# 12
class CardPayment(Payment):
    """Card Payment Method."""

    def __init__(self, card_number, card_holder):
        self.card_number = card_number
        self.card_holder = card_holder

    def pay(self, amount):

        last_four = self.card_number[-4:]

        print("\n----- CARD PAYMENT -----")
        print(f"Card Holder : {self.card_holder}")
        print(f"Card : **** **** **** {last_four}")
        print(f"Amount : ₹{amount}")
        print("Payment Successful using Card.")

    def refund(self, amount):

        last_four = self.card_number[-4:]

        print(f"₹{amount} refunded to card ending with {last_four}.")


# 13
class CashOnDelivery(Payment):
    """Cash on Delivery Payment."""

    def pay(self, amount):

        print("\n----- CASH ON DELIVERY -----")
        print(f"Amount to Collect : ₹{amount}")
        print("Payment will be collected during delivery.")

    def refund(self, amount):

        print(f"₹{amount} refund will be processed manually.")


# 15
class Order:

    order_counter = 1001

    def __init__(self, customer, cart, payment):

        self.order_id = Order.order_counter
        Order.order_counter += 1

        self.customer = customer
        self.payment = payment

        self.items = cart.get_items().copy()

        self.total_amount = cart.calculate_total()

        self.status = "PLACED"

        self.delivery_partner = None

    def place_order(self):

        print("\nProcessing Payment...")

        self.payment.pay(self.total_amount)

        for product, quantity in self.items.items():
            product.stock -= quantity

        self.status = "CONFIRMED"

        print("\nOrder placed successfully.")

    def assign_delivery_partner(self, partner):

        self.delivery_partner = partner

        partner.accept_order(self.order_id)

        print(
            f"\nOrder assigned to "
            f"{partner.username}"
        )

    def update_status(self, status):

        self.status = status

        print(
            f"\nOrder Status Updated : {status}"
        )

    def cancel_order(self):

        if self.status == "DELIVERED":

            print("Cannot cancel delivered order.")
            return

        for product, quantity in self.items.items():
            product.stock += quantity

        self.payment.refund(self.total_amount)

        self.status = "CANCELLED"

        print("\nOrder cancelled successfully.")

    def track_order(self):

        print(
            f"\nOrder ID : {self.order_id}"
        )

        print(
            f"Status : {self.status}"
        )

    def display_order(self):

        print("\n========== ORDER ==========")

        print(f"Order ID : {self.order_id}")

        print(f"Customer : {self.customer.username}")

        print(f"Status : {self.status}")

        if self.delivery_partner:
            print(
                f"Delivery Partner : "
                f"{self.delivery_partner.username}"
            )

        print("----------------------------")

        for product, quantity in self.items.items():

            subtotal = product.price * quantity

            print(
                f"{product.name:15}"
                f"Qty:{quantity:<3}"
                f"Subtotal: ₹{subtotal}"
            )

        print("----------------------------")

        print(f"Total Amount : ₹{self.total_amount}")


# 16
def display_order(self):

        print("\n" + "=" * 45)
        print(f"Order ID : {self.order_id}")
        print(f"Customer : {self.customer.username}")
        print(f"Status   : {self.status}")

        if self.delivery_partner:
            print(f"Delivery Partner : {self.delivery_partner.username}")

        print("-" * 45)

        for product, quantity in self.items.items():

            subtotal = product.price * quantity

            print(
                f"{product.name:15}"
                f"Qty:{quantity:<3}"
                f"Subtotal: ₹{subtotal}"
            )

        print("-" * 45)
        print(f"Total : ₹{self.total_amount}")
        print("=" * 45)


# 17
def place_order(self):

        print("\nProcessing Payment...")

        self.payment.pay(self.total_amount)

        # Reduce stock only after payment
        for product, quantity in self.items.items():

            product.stock -= quantity

        self.status = "CONFIRMED"

        print("\nOrder placed successfully.")


# 18
def assign_delivery_partner(self, partner):

        self.delivery_partner = partner

        partner.accept_order(self.order_id)

        print(
            f"\nOrder {self.order_id} assigned to "
            f"{partner.username}"
        )


# 19
def update_status(self, status):

        self.status = status

        print(
            f"\nOrder {self.order_id} status updated "
            f"to {status}"
        )


# 20
def cancel_order(self):

        if self.status == "DELIVERED":

            print("\nDelivered orders cannot be cancelled.")
            return

        # Return stock
        for product, quantity in self.items.items():

            product.stock += quantity

        self.payment.refund(self.total_amount)

        self.status = "CANCELLED"

        print("\nOrder cancelled successfully.")


# 21
def track_order(self):

        print(
            f"\nOrder {self.order_id}"
        )

        print(
            f"Current Status : {self.status}"
        )







# 4
# --------------------------
# Sample Products
# --------------------------

# products = [

#     Product(101, "Milk", "Dairy", 30, 50),
#     Product(102, "Rice", "Grocery", 65, 100),
#     Product(103, "Apple", "Fruits", 120, 40),
#     Product(104, "Bread", "Bakery", 45, 25)

# ]

# --------------------------
# Customer
# --------------------------

# customer = Customer(

#     "Ajay",
#     "python123",
#     "9876543210",
#     "Kurnool"

# )

# customer.login()

# customer.show_profile()

# customer.add_money(1000)

# customer.show_wallet()

# customer.browse_products(products)

# customer.search_product(products, "Rice")

# customer.change_password("python123", "NewPassword")

# customer.logout()



# 7

# ------------------------
# Products
# ------------------------

# products = [

#     Product(101, "Milk", "Dairy", 30, 50),
#     Product(102, "Rice", "Grocery", 60, 100)

# ]

# # ------------------------
# # Admin
# # ------------------------

# admin = Admin("Admin", "admin123")

# admin.login()

# admin.view_products(products)

# # Add Product

# new_product = Product(

#     103,
#     "Bread",
#     "Bakery",
#     45,
#     30

# )

# admin.add_product(products, new_product)

# # Update Stock

# admin.update_stock(products, 103, 25)

# # Update Price

# admin.update_price(products, 102, 70)

# admin.view_products(products)

# # Remove Product

# admin.remove_product(products, 101)

# admin.view_products(products)

# admin.logout()

# # ------------------------
# # Delivery Partner
# # ------------------------

# partner = DeliveryPartner(

#     "Rahul",
#     "9876543210"

# )

# partner.login()

# partner.accept_order(1001)

# partner.accept_order(1002)

# partner.view_orders()

# partner.update_status(1001, "Out For Delivery")

# partner.deliver_order(1001)

# partner.view_orders()

# partner.logout()


# 9
# Products

# milk = Product(101, "Milk", "Dairy", 30, 50)

# rice = Product(102, "Rice", "Grocery", 70, 80)

# bread = Product(103, "Bread", "Bakery", 40, 25)

# apple = Product(104, "Apple", "Fruits", 120, 40)


# # Cart 1

# cart1 = Cart()

# cart1.add_product(milk, 2)

# cart1.add_product(rice, 3)

# cart1.display_cart()


# # Cart 2

# cart2 = Cart()

# cart2.add_product(bread, 2)

# cart2.add_product(apple, 1)

# cart2.display_cart()


# # Operator Overloading

# merged_cart = cart1 + cart2

# print(merged_cart)


# # __len__

# print("\nNumber of Different Products:", len(merged_cart))


# # __contains__

# print("\nMilk in Cart ?:\n", milk in merged_cart)

# print("Bread in Cart ?:\n", bread in merged_cart)


# 14
# amount = 650

# upi = UPIPayment("ajay@upi")

# card = CardPayment(
#     "1234567812345678",
#     "Ajay Dinesh"
# )

# cod = CashOnDelivery()

# print("\n=========== UPI ===========")
# upi.pay(amount)
# upi.refund(200)

# print("\n=========== CARD ===========")
# card.pay(amount)
# card.refund(300)

# print("\n=========== COD ===========")
# cod.pay(amount)
# cod.refund(650)


# 22
# Products

milk = Product(
    101,
    "Milk",
    "Dairy",
    30,
    50
)

rice = Product(
    102,
    "Rice",
    "Grocery",
    70,
    40
)

# Customer

customer = Customer(
    "Ajay",
    "python123",
    "9876543210",
    "Kurnool"
)

# Cart

cart = Cart()

cart.add_product(milk, 2)

cart.add_product(rice, 3)

# Payment

payment = UPIPayment("ajay@upi")

# Order

order = Order(
    customer,
    cart,
    payment
)

order.place_order()

# Delivery Partner

partner = DeliveryPartner(
    "Rahul",
    "9876543210"
)

order.assign_delivery_partner(partner)

order.display_order()

order.track_order()

order.update_status("OUT FOR DELIVERY")

order.track_order()

order.update_status("DELIVERED")

order.track_order()