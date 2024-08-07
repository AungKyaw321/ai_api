# func.py
import os
import yfinance as yf
import openai
import re
from dotenv import load_dotenv

def load_api_key():
    load_dotenv('key.env')
    return os.getenv('OPENAI_API_KEY')

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
        formatted_data += (f"\nStock Information for {company}:\n"
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
    sectors = ['XLK', 'XLV', 'XLF', 'XLY', 'XLP', 'XLE', 'XLB', 'XLRE', 'XLU']  # Technology, Healthcare, Finance, etc.
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
    api_key = load_api_key()
    openai.api_key = api_key
    
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
         {info}
        - talk about each company briefly as well and news 
       - Insights into how these flight patterns might indicate strategic movements (mergers, acquisitions, expansions).
       - Analysis of stock information, significant changes, and correlations with flight data and market trends.
       - Relevant news or events for investors.
       - Ensure the stock information is readable such as billions and millions and not just digits.


    3. Weekly Market Overview:
       Using the market overview data:
       {market_overview}
       - Key insights from this week's market performance.
       - Performance of major indices (S&P 500, Dow Jones, NASDAQ) and sector performance.
       - Trends in stock prices, highlighting gains and losses.
       - Context on economic indicators and other factors influencing market movements.
       - Guidance for investors on upcoming trends.

    4. Conclusion:
       - Forward-looking perspective on the market.
       - Key takeaways for investors.
       - Insights into potential opportunities and risks.
       - What to look out for next week
 
    Ensure the newsletter is comprehensive, detailed, and investor-focused. Use clear and professional language, no bullet points, only paragraphs  
    and aim to keep the response within 2600 tokens for engagement and thorough insights. Make it similar to a 
    newsletter you would receive via email. 
    Make it professional no bullet points, don't list numbers in the overview section, make it more of a summary. Print section name before each section. Make sure the b tags or <b> are there. 
    """

    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=2600,
        temperature=0.5  # creativity, higher = more creative
    )

    output_text = response.choices[0].text.strip()

    def split(text):
        headers = ["Introduction:", "Company Flights and Stock Information:", "Weekly Market Overview:", "Conclusion:"]
        for header in headers:
            text = re.sub(re.escape(header), "split", text)
        
        return text
    
    formatted_text = split(output_text)
    
    file_path = "output.txt"
    with open(file_path, "w") as file:
        file.write(formatted_text)

    return file_path
