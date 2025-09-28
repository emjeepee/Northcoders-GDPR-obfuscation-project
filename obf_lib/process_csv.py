import io
import csv





def process_csv(file, pii_fields):
    input_stream = io.StringIO(file)
    reader = csv.DictReader(input_stream)

    output_stream = io.StringIO()
    writer = csv.DictWriter(output_stream, fieldnames=reader.fieldnames)
    writer.writeheader()

    for row in reader:
        for field in pii_fields:
            if field in row:
                row[field] = "***"
        writer.writerow(row)

    # Convert to byte stream
    return output_stream.getvalue().encode("utf-8")