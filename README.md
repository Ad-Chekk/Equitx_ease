📊 Stock Market Insights Dashboard
An interactive multi-page Streamlit web application for analyzing stock market data, visualizing trends, extracting financial news, and comparing equities across Indian and international exchanges.

🧠 Project Overview
This project offers a visual dashboard to:

Analyze stock trends for Indian and international markets.

View real-time stock news and sentiment.

Visualize key indicators like price change, trading volume, and volatility.

Customize the dashboard layout and interact with multiple pages.

Built using Streamlit, Plotly, and yfinance, this app allows both technical and non-technical users to gain actionable insights into equity performance.

🚀 Features
📈 Single Stock Analysis: Track stock prices, volume, and indicators.

📰 News Sentiment: Scrape and visualize the latest headlines for selected stocks.

🌐 Exchange Support: Supports NSE/BSE for Indian stocks and Nasdaq/NYSE for international.

📊 Dashboards:

Line and volume charts

Donut charts for price-volume relationship

Gauge charts for average volume

Max-Min indicator comparisons

📦 Modular Design: Organized using separate scripts for different functionalities.

🏗️ Project Structure
bash
Copy
Edit
.
├── app.py                  # Main entry point (Streamlit app)
├── 1_stock_news.py         # News extraction and display
├── 2_Single_equity.py      # Single stock analysis logic
├── 3_Default_Dashboard.py  # Default landing dashboard
├── dataset.py              # Data fetching and preprocessing
├── variables.py            # Shared constants and variables
├── requirements.txt        # Python dependencies
├── devcontainer.json       # Development environment settings
🛠️ Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/Ad-Chekk/Equitx_ease

Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
💻 Usage
Launch the application using:

bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501.

Use the sidebar to:

Select stock type (Indian or International)

Choose NSE or BSE for Indian stocks

Input the stock symbol (e.g., TCS, AAPL)

Set start and end dates for analysis

🔍 Example Screenshots
(Include relevant screenshots of different pages of the dashboard.)

🧩 Technologies Used
Streamlit – Frontend UI

Plotly – Interactive charts

Pandas – Data manipulation

yfinance – Financial data retrieval

BeautifulSoup – News scraping

[Python datetime & numpy] – Data utilities

📌 Future Enhancements
Add machine learning predictions for stock trends.

Integrate real-time trading signals.

Deploy on cloud platforms (e.g., Streamlit Cloud, Heroku, or AWS).

Add user authentication for personalized dashboards.

