import csv

def csv_data_reader(file):
    data_read = []
    with open(file, newline="") as csvfile:
        data = csv.DictReader(csvfile)
        for share in data:
            if float(share["price"]) > 0 and float(share["profit"]) > 0:
                data_read.append(
                    (
                        share["name"],
                        int(share["price"]),
                        int(share["profit"]),
                    )
                )
    return data_read