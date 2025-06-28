# Lottery Trend Analyzer

This simple Streamlit app visualizes Powerball drawing data from [NY Open Data](https://data.ny.gov/).
It highlights hot and cold numbers and shows an estimated trend score for user-selected numbers.

## Setup

1. Install Python dependencies:
   ```bash
   pip install -r lottery-analyzer/requirements.txt
   ```
2. Launch the application:
   ```bash
   streamlit run lottery-analyzer/app.py
   ```

The app will fetch recent Powerball drawings and display the results in your browser.

### Development

Run a basic syntax check before committing changes:

```bash
python -m py_compile lottery-analyzer/*.py && echo ok
```

### Contributing

If you plan to push changes to your own GitHub repository, set the remote URL and push:

```bash
git remote add origin https://TOKEN@github.com/tjedawgfan/lottery-analyzer.git
git push -u origin main  # may prompt for your GitHub token
```
