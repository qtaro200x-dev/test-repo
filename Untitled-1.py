from datetime import datetime

def show_current_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current time: {current_time}")

show_current_time()