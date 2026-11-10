# Dynamic Python API Client

A flexible, interactive Python script designed to make HTTP GET requests to public REST APIs dynamically based on user input.

## Features

- **Dynamic Query Builder:** Construct custom query parameters interactively via CLI loops.
- **Robust Error Handling:** Safely catch network timeouts, invalid URLs, and HTTP connection errors using `try-except` blocks.
- **Adaptive Data Parsing:** Dynamically detect JSON structure types (`list` vs. `dict`) and print key-value pairs without hardcoded attributes.

## Requirements

- Python 3.x
- `requests` library

```bash
pip install requests