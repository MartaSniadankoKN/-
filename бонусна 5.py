# Патерн Strategy: різні способи оплати
class PaymentStrategy:
    def pay(self, amount):
        pass

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount} грн кредитною карткою.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Оплата {amount} грн через PayPal.")

# Патерн State: стан замовлення
class OrderState:
    def handle(self, order):
        pass

class NewOrderState(OrderState):
    def handle(self, order):
        print("Замовлення нове. Переходимо до оплати.")
        order.set_state(PaidOrderState())

class PaidOrderState(OrderState):
    def handle(self, order):
        print("Замовлення оплачене. Готуємо до доставки.")
        order.set_state(ShippedOrderState())

class ShippedOrderState(OrderState):
    def handle(self, order):
        print("Замовлення вже відправлено. Очікуйте доставку.")

# Клас замовлення
class Order:
    def __init__(self, amount):
        self.amount = amount
        self.state = NewOrderState()
        self.payment_strategy = None

    def set_state(self, state):
        self.state = state

    def set_payment_strategy(self, strategy):
        self.payment_strategy = strategy

    def process(self):
        self.state.handle(self)

    def pay(self):
        if self.payment_strategy:
            self.payment_strategy.pay(self.amount)
        else:
            print("Метод оплати не вибрано.")

# Використання
order = Order(500)

# Strategy — вибір способу оплати
order.set_payment_strategy(CreditCardPayment())
order.pay()

# State — обробка замовлення поетапно
order.process()  # New -> Paid
order.process()  # Paid -> Shipped
order.process()  # Shipped -> кінцевий стан
