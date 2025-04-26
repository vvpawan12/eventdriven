# function_app/__init__.py
import logging
import azure.functions as func


def main(msg: func.ServiceBusMessage):
    csv_content = msg.get_body().decode('utf-8')
    logging.info(f"Received CSV: {csv_content}")

    # Save CSV to a Storage Blob (optional)
    # or directly process and save to database or file

    # If saving to blob storage:
    # (You can use Azure SDK for Blob Storage to upload)

    # For now, let's write it to a simple file locally
    with open('/tmp/order.csv', 'w') as f:
        f.write(csv_content)

    logging.info("CSV file saved successfully!")
