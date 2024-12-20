import plotly.graph_objects as go
import requests
from datetime import datetime, timezone

# Fetch Glassnode data (ensure you have an API key)
api_key = "2BKRA1m0T5y6oHwgG2EqSnFH6Ds"
endpoint = "https://api.glassnode.com/v1/metrics/addresses/active_count"
params = {'a': 'BTC', 'api_key': api_key}
response = requests.get(endpoint, params=params)

data = response.json()

# Extract timestamps and values, converting timestamps to ISO 8601 format
timestamps = [datetime.fromtimestamp(item['t'], tz=timezone.utc).isoformat() for item in data]
values = [item['v'] for item in data]

# Create the chart
fig = go.Figure(data=go.Scatter(x=timestamps, y=values, mode='lines'))
fig.update_layout(title="Bitcoin Active Addresses Count", xaxis_title="Date", yaxis_title="Count")

# Save as HTML
fig.write_html("chart.html")
