from kafka import KafkaConsumer
import csv
import ast

consumer = KafkaConsumer(
    "course-topic",
    bootstrap_servers=["localhost:9092"],
    auto_offset_reset="latest",
    enable_auto_commit=True,
    group_id="example_group"
)

field_names = ['NAME', 'ADDRESS', 'CREATED_AT']

with open('data_from_topic.csv', 'w', encoding='utf-8') as csv_file:
    writer = csv.DictWriter(csv_file, field_names)
    writer.writeheader()

for message in consumer:
    with open('data_from_topic.csv', 'a', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, field_names)
        writer.writerow(ast.literal_eval(message.value.decode('utf-8')))

