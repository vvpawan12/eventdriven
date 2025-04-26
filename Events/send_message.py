# send_message.py
from azure.servicebus import ServiceBusClient, ServiceBusMessage

CONNECTION_STR = "https://drivenorders.servicebus.windows.net/orders"
QUEUE_NAME = "orders"

servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)

with servicebus_client:
    sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
    with sender:
        with open("order.csv", "r") as f:
            csv_content = f.read()
        message = ServiceBusMessage(csv_content)
        sender.send_messages(message)
        print("CSV file sent to Service Bus Queue!")
