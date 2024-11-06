# Singer.io Studies

## Overview
This repository contains studies and resources focused on **[Singer.io](https://www.singer.io/)**, an open-source framework for data integration that allows you to extract and load data between databases, web APIs, files, and more. The project provides an in-depth look at the features, use cases, and best practices of using **Singer taps** and **targets** to automate data workflows.

## What is Singer.io?
Singer is a simple, composable ETL (Extract, Transform, Load) framework that uses JSON-based, human-readable specifications. It allows you to easily move data between different systems by writing connectors known as "taps" (data extraction) and "targets" (data loading).

- **Taps**: These extract data from APIs, databases, or files.
- **Targets**: These load the extracted data into a storage system or database.

## Studies Covered in This Repository
This repository covers the following topics:

1. **Introduction to Singer**:
   - What is Singer?
   - How it fits into the modern data stack.
   - Key components (taps and targets).

2. **Setting Up a Singer Tap**:
   - How to install and configure taps.
   - Example: Setting up a tap for an API source.

3. **Configuring Singer Targets**:
   - Setting up a target to load data into a database (e.g., Snowflake, PostgreSQL).
   - Example: Writing data to a CSV target.

4. **Data Pipeline Design with Singer**:
   - Best practices for designing ETL pipelines using Singer.
   - Chaining taps and targets together.

5. **Extending and Customizing Taps and Targets**:
   - How to extend existing taps and targets for custom use cases.
   - Writing your own taps and targets.

## Getting Started
To begin using **Singer.io** in your data workflows:

1. **Install Singer**:
   ```bash
   pip install singer-python


2. **Run a Tap**:
 ```
tap-someapi --config config.json
 ```
3. **Run a target**:
 ```
target-someoutput --config config.json
 ```

## References and Resources
Official Website: https://www.singer.io/

GitHub Repository: [Singer Python](https://github.com/singer-io/singer-python)

-------------

Usage:

```bash
# setup virtual envs for singer tap-fixerio
python3 -m venv ~/.virtualenvs/tap-fixerio
source ~/.virtualenvs/tap-fixerio/bin/activate
pip install tap-fixerio
deactivate

# setup virtual envs for singer target-gsheet
python3 -m venv ~/.virtualenvs/target-gsheet
source ~/.virtualenvs/target-gsheet/bin/activate
pip install target-gsheet
deactivate

# usage to run the script properly
~/.virtualenvs/tap-fixerio/bin/tap-fixerio --config fixer_io_config.json | ~/.virtualenvs/target-gsheet/bin/target-gsheet -c config.json >> state.json
tail -1 state.json > state.json.tmp && mv state.json.tmp state.json
```

# usage to run the script to get OMDB data
python3 tap.py -c ../config.json | ~/.virtualenvs/target-gsheet/bin/target-gsheet -c /workspaces/singer-test/config.json
```