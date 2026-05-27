# Weather Collector

A simple Python script that collects current weather data for UAE cities 
using the Open-Meteo API and saves it to a JSON file.

## What it does

- Fetches current weather (temperature, humidity, wind speed) for multiple cities
- Handles API errors gracefully
- Saves results to a timestamped JSON file

This is a minimal ETL pipeline: **Extract** data from an API, 
**Transform** it into a clean structure, **Load** it into a file.

## Tech stack

- Python 3
- `requests` for HTTP calls
- Open-Meteo API (free, no key required)

## How to run

```bash
pip install -r requirements.txt
python3 weather.py
```

## Example output
```bash
Dubai: 38.5°C, humidity 45%, wind 12 km/h
Abu Dhabi: 39.1°C, humidity 50%, wind 10 km/h
```
---

*Part of my journey into Data Engineering.*