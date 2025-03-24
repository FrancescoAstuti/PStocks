import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from typing import List

class StockLot:
    def __init__(self, ticker: str, quantity: float, purchase_price: float, current_price: float):
        self.ticker = ticker
        self.quantity = quantity
        self.purchase_price = purchase_price
        self.current_price = current_price

class GUI:
    def __init__(self, stock_lots: List[StockLot]):
        self.stock_lots = stock_lots
        self.fig = plt.figure(figsize=(8, 4))
        self.time_frame = "1M"  # Default time frame
    
    def create_chart_panel(self):
        self.ax = self.fig.add_subplot(111)
        self.update_chart(self.time_frame)
        canvas = FigureCanvasTkAgg(self.fig, master=None)
        return canvas.get_tk_widget()
    
    def update_chart(self, time_frame):
        self.time_frame = time_frame
        self.ax.clear()
        # Here you would add your actual charting logic based on time_frame
        self.ax.set_title(f"Portfolio Performance ({time_frame})")
        self.ax.set_xlabel("Date")
        self.ax.set_ylabel("Value")
        # Placeholder for demonstration
        if time_frame == "1W":
            x = list(range(7))
        elif time_frame == "1M":
            x = list(range(30))
        elif time_frame == "2M":
            x = list(range(60))
        elif time_frame == "3M":
            x = list(range(90))
        elif time_frame == "6M":
            x = list(range(180))
        else:  # 1Y
            x = list(range(365))
        
        # Simulated data - in real app, you'd get actual stock performance
        y = [i * i * 0.1 for i in x]
        self.ax.plot(x, y)
        self.fig.canvas.draw_idle()
    
    def create_and_show_gui(self):
        # Create the Portfolio window
        portfolio_window = tk.Tk()
        portfolio_window.title("Portfolio")
        portfolio_window.geometry("800x600")
        
        # Add your portfolio UI components here
        label = ttk.Label(portfolio_window, text="Portfolio Management")
        label.pack(pady=10)
        
        portfolio_window.mainloop()

class StockScreener:
    def create_and_show_gui(self):
        screener_window = tk.Tk()
        screener_window.title("Stock Screener")
        screener_window.geometry("800x600")
        
        # Add your stock screener UI components here
        label = ttk.Label(screener_window, text="Stock Screener")
        label.pack(pady=10)
        
        screener_window.mainloop()

class Watchlist:
    def create_and_show_gui(self):
        watchlist_window = tk.Tk()
        watchlist_window.title("Watchlist")
        watchlist_window.geometry("800x600")
        
        # Add your watchlist UI components here
        label = ttk.Label(watchlist_window, text="Watchlist")
        label.pack(pady=10)
        
        watchlist_window.mainloop()

class Main:
    def __init__(self):
        self.stock_lots = []
        self.overview_window = None
    
    def show_overview(self):
        if self.overview_window is not None:
            self.overview_window.deiconify()
            return
        
        self.overview_window = tk.Tk()
        self.overview_window.title("Overview")
        self.overview_window.geometry("800x600")
        
        gui = GUI(self.stock_lots)
        chart_panel = gui.create_chart_panel()
        
        # Create buttons
        portfolio_button = ttk.Button(
            self.overview_window, 
            text="Portfolio", 
            command=lambda: [self.overview_window.destroy(), gui.create_and_show_gui()]
        )
        
        stock_screener_button = ttk.Button(
            self.overview_window, 
            text="Stock Screener", 
            command=lambda: StockScreener().create_and_show_gui()
        )
        
        watchlist_button = ttk.Button(
            self.overview_window, 
            text="Watchlist", 
            command=lambda: Watchlist().create_and_show_gui()
        )
        
        # Create time frame buttons
        time_frame_panel = ttk.Frame(self.overview_window)
        time_frames = ["1W", "1M", "2M", "3M", "6M", "1Y"]
        
        for time_frame in time_frames:
            button = ttk.Button(
                time_frame_panel, 
                text=time_frame, 
                command=lambda tf=time_frame: gui.update_chart(tf)
            )
            button.pack(side=tk.LEFT, padx=5)
        
        # Add components to layout
        time_frame_panel.pack(side=tk.TOP, fill=tk.X, pady=5)
        chart_panel.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        button_panel = ttk.Frame(self.overview_window)
        portfolio_button.pack(side=tk.LEFT, padx=10, pady=10)
        stock_screener_button.pack(side=tk.LEFT, padx=10, pady=10)
        watchlist_button.pack(side=tk.LEFT, padx=10, pady=10)
        button_panel.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.overview_window.mainloop()
    
    def add_stock_to_portfolio(self, ticker, quantity, purchase_price, current_price):
        stock_lot = StockLot(ticker, quantity, purchase_price, current_price)
        self.stock_lots.append(stock_lot)

def main():
    app = Main()
    app.show_overview()

if __name__ == "__main__":
    main()