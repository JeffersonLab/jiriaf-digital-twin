import queue
import time

# Set up a queue to simulate a stream of data
data_stream = queue.Queue()

# Add some messages to the queue with current timestamp
for i in range(100):  # Increase the number of messages to create a larger backlog
    data_stream.put((f"Message {i}", time.time()))

def process_message(message):
    # Convert the message to uppercase
    processed_message = message.upper()
    time.sleep(0.1)  # Introduce a delay in processing each message
    return processed_message, time.time()

# Stream processing loop
start_time = time.time()
processed_messages = 0
while True:
    try:
        # Get the next message from the queue
        message, input_time = data_stream.get_nowait()
        print(f"input_time: {input_time}")
    except queue.Empty:
        # No more messages in the queue
        print("No more messages in the queue")
        break

    # Process the message and print the result
    processed_message, process_time = process_message(message)
    print(f"process_time: {process_time}")
    print(processed_message)

    processed_messages += 1

end_time = time.time()

# Calculate and print the input and output rate
input_rate = 100 / (input_time - start_time)
output_rate = processed_messages / (end_time - start_time)
print(f"Input rate: {input_rate} messages per second")
print(f"Output rate: {output_rate} messages per second")
print(f"Ratio: {output_rate/input_rate}")
print(f"Processed {processed_messages} messages in {end_time - input_time} seconds")