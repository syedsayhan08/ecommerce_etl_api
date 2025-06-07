
# ecommerce_etl_api

# Daily ETL Pipeline with FastAPI + SQLite

## Folder Structure

```
your_project/
│
├── data/
│   └── sales_data.csv           # Source data file (CSV)
│
├── db.py                        # DB models and setup
├── etl.py                       # ETL logic (extract, transform, load)
├── etl_job.py                   # Daily runner using while loop + sleep
├── main.py                      # FastAPI server with API routes
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Process Flow Diagram

![ETL Process Flow](etl_process_flow.png)

## Setup Instructions

1. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. **Install dependencies**

```bash
pip install fastapi uvicorn sqlalchemy pandas faker
```

3. **Prepare your data**

Place `sales_data.csv` in the `data/` folder.

4. **Run the ETL job manually (one-time)**

```bash
python etl.py
```

5. **Run the ETL job daily using a loop**

```bash
python etl_job.py
```

6. **Start the FastAPI server**

```bash
uvicorn main:app --reload
```

Visit: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Example (FastAPI)

| Method | Endpoint | Description           |
|--------|----------|-----------------------|
| GET    | /sales   | List all sales        |
| POST   | /sales   | Add a new sale record |

## Running ETL Daily (while loop approach)

Since you are using the `while True` loop in `etl_job.py`:

- Run your ETL job by:

```bash
python etl_job.py
```

- **Keep this terminal window open and running.**  
  If you close it, the script stops and ETL won't run the next day.

- To run the script in the background (Linux/Mac), use:

```bash
nohup python etl_job.py &
```

This keeps the ETL running even if you close the terminal.
