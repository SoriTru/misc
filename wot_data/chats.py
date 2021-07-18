import pandas as pd
from datetime import datetime


if __name__ == "__main__":
    session_df = pd.read_csv("data/Activity_history/WOT_Game_Sessions.csv", sep=";", error_bad_lines=False)

    starts = [item for item in session_df.STARTED_AT]
    ends = [item for item in session_df.FINISHED_AT]

    total_secs = 0
    for count in range(len(starts)):
        start = datetime.strptime(starts[count], '%Y-%m-%d %H:%M:%S').timestamp()
        end = datetime.strptime(ends[count], '%Y-%m-%d %H:%M:%S').timestamp()
        total_secs += end - start

    print(f"You've played for a total of: {total_secs / (60 * 60 * 24)} days")