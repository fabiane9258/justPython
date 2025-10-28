import sys
from datetime import datetime
import subprocess
import os

def log_session(time_range):
    """Append today's session to data.txt and run analyzer."""
    today = datetime.now().strftime("%Y-%m-%d")
    log_entry = f"{today} {time_range}\n"

    file_path = "data.txt"
    with open(file_path, "a") as file:
        file.write(log_entry)

    print(f"✅ Logged session: {log_entry.strip()}")

    # Run analyzer.py right after
    analyzer_path = os.path.join(os.path.dirname(__file__), "analyzer.py")
    subprocess.run(["python3", analyzer_path])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("⚠️  Usage: python3 log.py <start-end>  (e.g. 09:00-10:45)")
    else:
        log_session(sys.argv[1])
