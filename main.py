# main.py
def run_sample():
    print("Starting sample ETL process...")
    data = [{"id": 1, "value": 10}, {"id": 2, "value": 20}]
    transformed = [{"id": d["id"], "value": d["value"] * 2} for d in data]
    print("Transformed Data:", transformed)

if __name__ == "__main__":
    run_sample()
