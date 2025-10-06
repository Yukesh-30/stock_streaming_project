import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import glob
import os

# Set a GUI backend for pop-up windows
matplotlib.use('TkAgg')  # or 'Qt5Agg' if you have PyQt installed
plt.ion()  # Enable interactive mode

# Path to your Spark output folder
output_path = "./output"

# Get all micro-batch files sorted by creation time
all_files = sorted(
    glob.glob(os.path.join(output_path, "part-00000-*.csv")),
    key=os.path.getctime
)

# Select last 5 files
last_5_files = all_files[-5:]

# Read and combine
df_list = [pd.read_csv(f) for f in last_5_files]
full_df = pd.concat(df_list, ignore_index=True)

print("Combined data from last 5 micro-batches:")
print(full_df)

# -----------------------------
# Bar plot: last batch
# -----------------------------
last_batch_df = df_list[-1]

plt.figure(figsize=(10,6))
plt.bar(last_batch_df['symbol'], last_batch_df['avg_price'], color='skyblue')
plt.title("Average Stock Price per Symbol (Last Batch)")
plt.xlabel("Stock Symbol")
plt.ylabel("Average Price")
plt.tight_layout()
plt.draw()  # Draw the figure
plt.pause(0.1)  # Pause to allow GUI event loop
plt.show()  # Pop-up interactive window

# -----------------------------
# Line plot: trend over last 5 batches
# -----------------------------
# Add batch number to each DataFrame
for i, df in enumerate(df_list):
    df['batch'] = i + 1

trend_df = pd.concat(df_list, ignore_index=True)
plt.figure(figsize=(12,6))

symbols = trend_df['symbol'].unique()
for symbol in symbols:
    symbol_data = trend_df[trend_df['symbol'] == symbol]
    plt.plot(symbol_data['batch'], symbol_data['avg_price'], marker='o', label=symbol)

plt.title("Average Stock Price Over Last 5 Micro-batches")
plt.xlabel("Batch Number")
plt.ylabel("Average Price")
plt.xticks(range(1, 6))
plt.legend()
plt.tight_layout()
plt.draw()
plt.pause(0.1)
plt.show(block=True)  # Pop-up interactive window

