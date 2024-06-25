import os

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import pandas as pd


def main():
    add_data_for_set("./stocks/data/apple.csv", "C0")
    add_data_for_set("./stocks/data/nvidia.csv", "C1")
    add_data_for_set("./stocks/data/alphabet_a.csv", "C2")
    add_data_for_set("./stocks/data/amd.csv", "C3")
    add_data_for_set("./stocks/data/microsoft.csv", "C4")

    ax = plt.gca()
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    plt.subplots_adjust(bottom=0.2)

    plt.xlabel("Date", fontsize=9)
    plt.ylabel("Closing Price ($)")
    plt.xticks(rotation=90)
    plt.title("Historical Stock Price")
    plt.legend()

    output_file = os.path.join(os.path.dirname(__file__), "output.png")
    plt.savefig(output_file)
    plt.show()


def add_data_for_set(file, colour):
    data = pd.read_csv(file)

    # Clean data set
    data["Date"] = pd.to_datetime(data["Date"])
    data["Close/Last"] = (
        data["Close/Last"].replace("[$,]", "", regex=True).astype(float)
    )
    data["Close/Last"] = pd.to_numeric(data["Close/Last"])

    label = get_filename_without_path_and_extension(file)
    plt.plot(data["Date"], data["Close/Last"], color=colour, label=label)


def get_filename_without_path_and_extension(file_path):
    filename = os.path.basename(file_path)
    filename_without_extension = os.path.splitext(filename)[0]
    return filename_without_extension


if __name__ == "__main__":
    main()
