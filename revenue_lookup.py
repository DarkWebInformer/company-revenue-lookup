import yfinance as yf

def validate_ticker(ticker):
    """Validates whether a given ticker is alphanumeric and within a reasonable length."""
    return ticker.isalnum() and 1 <= len(ticker) <= 5

def get_company_revenue(ticker):
    """Retrieves the revenue of a company using its stock ticker via yfinance."""
    try:
        company = yf.Ticker(ticker)
        info = company.info

        # Check if the ticker corresponds to a valid company
        if 'longName' not in info:
            return f"'{ticker}' does not appear to be a valid stock ticker."
        
        # Check if 'totalRevenue' is available
        if 'totalRevenue' in info and info['totalRevenue']:
            revenue = info['totalRevenue']
            revenue_in_billions = revenue / 1e9  # Convert to billions for readability
            return f"The current revenue for {info['longName']} ({ticker}) is approximately ${revenue_in_billions:.2f} billion."
        else:
            return f"Revenue data not found for {info['longName']} ({ticker})."
    except KeyError:
        return f"Invalid data format received for {ticker}."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

def ascii_banner():
    print("""
 ___                                                 _                    _                   
|  _`\\                                              ( )                  ( )                  
| (_) )   __   _   _    __    ___   _   _    __     | |       _      _   | |/')  _   _  _ _   
| ,  /  /'__`\\( ) ( ) /'__`\\/\' _ `\\( ) ( ) /'__`\\   | |  _  /'_`\\  /'_`\\ | , <  ( ) ( )( '_`\\ 
| |\\ \\ (  ___/| \\_/ |(  ___/| ( ) || (_) |(  ___/   | |_( )( (_) )( (_) )| |\\`\\ | (_) || (_) )
(_) (_)`\\____)`\\___/'`\\____)(_) (_)`\\___/'`\\____)   (____/'`\\___/'`\\___/'(_) (_)`\\___/'| ,__/'
                                                                                       | |    
                                                                                       (_)    

Created by Dark Web Informer
\033]8;;https://x.com/DarkWebInformer\033\\x.com/DarkWebInformer\033]8;;\033\\ | \033]8;;https://darkwebinformer.com\033\\darkwebinformer.com\033]8;;\033\\
    """)

def main():
    ascii_banner()
    try:
        while True:
            company_ticker = input("Enter the stock ticker of the company (e.g., AAPL for Apple): ").strip().upper()
            
            if validate_ticker(company_ticker):
                print(get_company_revenue(company_ticker))
            else:
                print("Invalid ticker. Please enter a valid alphanumeric ticker (1–5 characters).")
            
            again = input("\nWould you like to look up another company? Enter 'yes' or 'no' (or 'y'/'n'): ").strip().lower()
            if again not in ['yes', 'y']:
                print("\nExiting...")
                break
    except KeyboardInterrupt:
        print("\n\nProcess interrupted. Exiting gracefully...")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()