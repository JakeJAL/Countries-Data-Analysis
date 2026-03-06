# Countries Data Analysis

A Python project that fetches and visualizes country data from the [REST Countries API](https://restcountries.com/).

## Features

- Fetches country information including names, UN membership status, and languages
- Visualizes the top 10 most common languages across countries
- Shows distribution of UN member vs non-member countries
- Exports processed data to CSV format

## Project Structure

```
.
├── work/
│   ├── fetch.py      # Data fetching and processing
│   ├── draw.py       # Visualization functions
│   └── main.py       # Main execution script
├── wrokings.ipynb    # Jupyter notebook with exploratory analysis
└── README.md
```

## Requirements

- Python 3.x
- requests
- pandas
- matplotlib

## Installation

1. Clone this repository
2. Install required packages:

```bash
pip install requests pandas matplotlib
```

## Usage

Run the main script to fetch data, generate visualizations, and save results:

```bash
python work/main.py
```

This will:
1. Fetch country data from the REST Countries API
2. Display bar charts showing:
   - Top 10 most common languages
   - UN membership distribution
3. Save the processed data to `data.csv`

## API Reference

This project uses the [REST Countries API v3.1](https://restcountries.com/):
- Endpoint: `https://restcountries.com/v3.1/all`
- Fields: `name`, `unMember`, `languages`

## License

This project is open source and available for educational purposes.
