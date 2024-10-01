import speedtest
import time
import tabulate

st = speedtest.Speedtest()
print("Running speed test. Please wait...")
st.get_best_server()

download_speed = st.download() / 1024 / 1024 # Convert to Mbps
upload_speed = st.upload() / 1024 / 1024    # Convert to Mbps
ping = st.results.ping

table_data = [
    ["Download Speed", f"{download_speed:.2f} Mbps"],
    ["Upload Speed", f"{upload_speed:.2f} Mbps"],
    ["Ping", f"{ping:.2f} ms"]
]

table = tabulate.tabulate(table_data, headers=["Metric", "Result"], tablefmt="grid")
print(table)

    

    
