import base64
import yfinance as yf
import re
from openai import OpenAI
from datetime import datetime, timedelta

import os
import requests
from dotenv import load_dotenv

load_dotenv('key.env')
api_key = os.getenv('OPENAI_API_KEY')


def get_stock_info(companies):
    stock_data = {}
    for company in companies:
        stock = yf.Ticker(company)
        info = stock.info
        stock_data[company] = {
            "Company Name": info.get('shortName', 'N/A'),
            "P/E Ratio": info.get('forwardPE', 'N/A'),
            "EPS": info.get('trailingEps', 'N/A'),
            "Beta": info.get('beta', 'N/A'),
            "52 Week High": info.get('fiftyTwoWeekHigh', 'N/A'),
            "52 Week Low": info.get('fiftyTwoWeekLow', 'N/A'),
            "Market Cap": info.get('marketCap', 'N/A'),
            "Dividend Yield": info.get('dividendYield', 'N/A'),
            "Revenue": info.get('totalRevenue', 'N/A'),
            "Net Income": info.get('netIncomeToCommon', 'N/A'),
            "Previous Close": info.get('previousClose', 'N/A'),
            "Open": info.get('open', 'N/A'),
            "Volume": info.get('volume', 'N/A'),
            "Average Volume": info.get('averageVolume', 'N/A')
        }
    return stock_data

def format_stock_info(stock_data):
    formatted_data = ""
    for company, data in stock_data.items():
        formatted_data += (f"Stock Information for {company}:\n"
                           f"Company Name: {data['Company Name']}\n"
                           f"P/E Ratio: {data['P/E Ratio']}\n"
                           f"EPS: {data['EPS']}\n"
                           f"Beta: {data['Beta']}\n"
                           f"52 Week High: {data['52 Week High']}\n"
                           f"52 Week Low: {data['52 Week Low']}\n"
                           f"Market Cap: {data['Market Cap']}\n"
                           f"Dividend Yield: {data['Dividend Yield']}\n"
                           f"Revenue: {data['Revenue']}\n"
                           f"Net Income: {data['Net Income']}\n"
                           f"Previous Close: {data['Previous Close']}\n"
                           f"Open: {data['Open']}\n"
                           f"Volume: {data['Volume']}\n"
                           f"Average Volume: {data['Average Volume']}\n"
                           f"{'-' * 40}\n")
    return formatted_data

def get_major_indices():
    indices = ['^GSPC', '^DJI', '^IXIC']  # S&P 500, Dow Jones, NASDAQ
    index_data = {}
    
    for index in indices:
        stock = yf.Ticker(index)
        hist = stock.history(period="5d")
        index_data[index] = hist

    return index_data

def get_sector_performance():
    sectors = ['XLB', 'XLC', 'XLD', 'XLE', 'XLF', 'XLI', 'XLB', 'XLP', 'XLU', 'XLY']  # Materials, Communication, etc.
    sector_data = {}
    
    for sector in sectors:
        stock = yf.Ticker(sector)
        hist = stock.history(period="5d")
        sector_data[sector] = hist

    return sector_data

def format_market_overview(index_data, sector_data):
    overview = "### Weekly Market Overview\n\n"
    
    overview += "#### Major Indices Performance\n"
    for index, data in index_data.items():
        overview += f"- {index}: Last 5 days close prices: {', '.join([str(round(price, 2)) for price in data['Close']])}\n"

    overview += "\n#### Sector Performance\n"
    for sector, data in sector_data.items():
        overview += f"- {sector}: Last 5 days close prices: {', '.join([str(round(price, 2)) for price in data['Close']])}\n"

    return overview

def generate_newsletter(company_a, company_b, company_c):
    companies = [company_a["name"], company_b["name"], company_c["name"]]
    stock_info = get_stock_info(companies)
    info = format_stock_info(stock_info)

    index_data = get_major_indices()
    sector_data = get_sector_performance()
    market_overview = format_market_overview(index_data, sector_data)

    prompt = f"""
    You are the chief writer for "SkyHigh Insights," a premier weekly newsletter that analyzes corporate 
    flight patterns and their implications for the investment landscape. Your task is to craft a detailed and
    engaging newsletter covering the following sections, put <b> tags around the ticker symbols in the output if printed as mentioned in the prompt, dont list anything and make it more of a paragraph style. Print the header sections as well without b tags:

    1. Introduction: Provide a warm and concise welcome around only two sentences, setting the stage for this week's insights.

    2. Company Flights and Stock Information:
       Using the provided data for <b>{company_a['name']}</b>, <b>{company_b['name']}</b>, and <b>{company_c['name']}</b>, include:
       - Flight details:
         - <b>{company_a['name']}</b>: From <b>{company_a['departure']}</b> to <b>{company_a['arrival']}</b>.
         - <b>{company_b['name']}</b>: From <b>{company_b['departure']}</b> to <b>{company_b['arrival']}</b>.
         - <b>{company_c['name']}</b>: From <b>{company_c['departure']}</b> to <b>{company_c['arrival']}</b>.
       - Stock performance for each company over the past week:
         - {info}
       - Talk about each company briefly as well and news.
       - Insights into how these flight patterns might indicate strategic movements (mergers, acquisitions, expansions).
       - Analysis of stock information, significant changes, and correlations with flight data and market trends.
       - Relevant news or events for investors.
       - Ensure the stock information is readable such as billions and millions and not just digits.

    3. Weekly Market Overview:
       Using the market overview data:
       - {market_overview}
       - Key insights from this week's market performance.
       - Performance of major indices (S&P 500, Dow Jones, NASDAQ) and sector performance.
       - Trends in stock prices, highlighting gains and losses.
       - Context on economic indicators and other factors influencing market movements.
       - Guidance for investors on upcoming trends.

    4. Conclusion:
       - Forward-looking perspective on the market.
       - Key takeaways for investors.
       - Insights into potential opportunities and risks.
       - What to look out for next week.

    Ensure the newsletter is comprehensive, detailed, and investor-focused. Use clear and professional language, no bullet points, only paragraphs and aim to keep the response within 2600 tokens for engagement and thorough insights. Make it similar to a newsletter you would receive via email. Make it professional no bullet points, don't list numbers in the overview section, make it more of a summary. Print section name before each section. Make sure the b tags or <b> are there.
    """

    client = OpenAI(api_key=api_key)


    response = client.completions.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=2600,
        temperature=0.5
    )
    output_text = response.choices[0].text.strip()

    def split(text):
        headers = ["Introduction:", "Company Flights and Stock Information:", "Weekly Market Overview:", "Conclusion:"]
        for header in headers:
            text = re.sub(re.escape(header), "split", text)
        return text.split("split")

    lines = split(output_text)

    html_content_p1 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Professional Email</title>
    <style>
      body {
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
        text-align: center;
        background-color: #f9f9f9;
      }
      .header {
        display: flex;
        align-items: center;
        justify-content: center;
        border: 1px solid #dddddd;
        padding: 20px;
        background-color: #222831;
        color: whitesmoke;
      }
      .header img {
        max-width: 30px;
        margin-right: 20px;
        height: auto;
      }
      .container {
        margin: 0 auto;
        max-width: 600px;
        display: flex;
        flex-direction: column;
        gap: 0;
      }
      .box {
        border: 1px solid #dddddd;
      }
      header,
      .content {
        padding: 30px;
        text-align: left;
        background-color: #f9f9f9;
      }
      .colors {
        color: darkblue;
      }
      footer {
        padding: 30px;
        text-align: left;
        background-color: #222831;
      }
      header h1,
      footer p {
        margin: 0;
        font-size: 16px;
        color: #333;
      }
      p {
        font-size: 12px;
        color: #333;
        margin-bottom: 10px;
      }
      .social-media {
        display: flex;
        justify-content: center;
        margin-top: 20px;
      }
      .social-media a {
        margin: 0 10px;
      }
      .social-media img {
        width: 30px;
        height: auto;
      }
      .section-with-image {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
      }
      .section-with-image img {
        max-width: 150px;
        height: auto;
        margin-right: 50px;
      }
      .section-with-image h5 {
        margin: 0;
        font-size: 16px;
        color: #333;
      }
      .section-with-image-right {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 20px;
      }
      .section-with-image-right img {
        max-width: 150px;
        height: auto;
        margin-left: 50px;
      }
      .section-with-image-right h5 {
        margin: 0;
        font-size: 16px;
        color: #333;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <div class="header">
        <img src="./img/Logo.png" alt="Newsletter Logo" />
        <h3>SkyHigh Insights</h3>
      </div>
      <div class="box">
        <div class="content">
          <div class="section-with-image">
            <img src="./img/flight.png" alt="Image" />
            <div>
            """

    html_content_p2 = f"""
              <h5 class="colors">Company Flights and Stock Information:</h5>
              <p>{''.join(lines[2])}</p>
            </div>
          </div>
          <div class="section-with-image-right" style="flex-direction: row-reverse">
            <img src="./img/stock-market.png" alt="Image" />
            <div>
              <h5 class="colors">Weekly Market Overview</h5>
              <p>{''.join(lines[3])}</p>
            </div>
          </div>
          <div class="section-with-image">
            <img src="./img/statistics.png" alt="Image" />
            <div>
              <h5 class="colors">Conclusion</h5>
              <p>{''.join(lines[4])}</p>
            </div>
          </div>
        </div>
      </div>
      <div class="box">
        <footer>
          <div class="social-media">
            <a href="#"><img src="./img/facebook-icon.png" alt="Facebook" /></a>
            <a href="#"><img src="./img/twitter-icon.png" alt="Twitter" /></a>
            <a href="#"><img src="./img/linkedin-icon.png" alt="LinkedIn" /></a>
            <a href="#"><img src="./img/instagram-icon.png" alt="Instagram" /></a>
          </div>
        </footer>
      </div>
    </div>
  </body>
</html>
"""

    html_content = html_content_p1 + html_content_p2
    base64encoded = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')

    return base64encoded