from datetime import datetime, timedelta
from collections import defaultdict

DAILY_GOAL_MINUTES = 90  # 1.5 hours

def parse_session(line):
    """Parse a line like '2025-10-13 09:00-09:45' into (date, start, end)."""
    date_str, time_range = line.strip().split()
    start_str, end_str = time_range.split('-')
    start = datetime.strptime(f"{date_str} {start_str}", "%Y-%m-%d %H:%M")
    end = datetime.strptime(f"{date_str} {end_str}", "%Y-%m-%d %H:%M")
    return date_str, start, end


def merge_overlaps(sessions):
    """Merge overlapping sessions for a single day."""
    if not sessions:
        return []
    sessions.sort(key=lambda x: x[0])
    merged = [sessions[0]]

    for start, end in sessions[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged


def analyze_coding_hours(file_path):
    sessions_by_day = defaultdict(list)

    # --- Step 1: Read and group sessions ---
    with open(file_path, "r") as file:
        for line in file:
            if line.strip():
                date_str, start, end = parse_session(line)
                sessions_by_day[date_str].append((start, end))

    print("\n📊 Coding Hours Analysis:\n")

    total_minutes = 0
    streak = 0
    best_streak = 0
    last_date = None
    daily_totals = {}

    # --- Step 2: Analyze each day ---
    for date_str in sorted(sessions_by_day.keys()):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        merged = merge_overlaps(sessions_by_day[date_str])
        daily_total = sum(int((end - start).total_seconds() / 60) for start, end in merged)
        daily_totals[date] = daily_total
        total_minutes += daily_total
        diff = daily_total - DAILY_GOAL_MINUTES

        # --- Step 3: Handle streaks ---
        if last_date and (date - last_date).days == 1:
            streak += 1
        else:
            streak = 1
        best_streak = max(best_streak, streak)
        last_date = date

        # --- Step 4: Daily feedback ---
        if daily_total >= DAILY_GOAL_MINUTES:
            print(f"{date_str} → {daily_total} mins ✅ Goal met (+{diff} mins)")
        elif daily_total >= 60:
            print(f"{date_str} → {daily_total} mins ⚠️ Almost there! Just {-diff:.0f} mins short.")
        else:
            print(f"{date_str} → {daily_total} mins ❌ Fell short by {-diff:.0f} mins — try scheduling earlier sessions.")

    # --- Step 5: Totals and averages ---
    days = len(daily_totals)
    avg = total_minutes / days if days else 0
    print(f"\n🧮 Total coded: {total_minutes:.0f} mins ({total_minutes / 60:.2f} hrs)")
    print(f"📅 Average per day: {avg:.1f} mins")
    print(f"🔥 Best streak: {best_streak} days in a row")

    # --- Step 6: Weekly trends ---
    if days >= 7:
        sorted_dates = sorted(daily_totals.keys())
        this_week = [m for d, m in daily_totals.items() if d >= sorted_dates[-1] - timedelta(days=6)]
        last_week = [m for d, m in daily_totals.items() if sorted_dates[-1] - timedelta(days=13) <= d < sorted_dates[-1] - timedelta(days=6)]
        this_avg = sum(this_week) / len(this_week) if this_week else 0
        last_avg = sum(last_week) / len(last_week) if last_week else 0
        diff = this_avg - last_avg

        print("\n📈 Weekly Trend:")
        if diff > 0:
            print(f"✅ You improved your weekly average by {diff:.1f} mins per day — great momentum!")
        elif diff < 0:
            print(f"⚠️ Your weekly average dropped by {-diff:.1f} mins per day — try to reclaim your focus!")
        else:
            print("➖ Your weekly average is consistent — steady progress!")

    # --- Step 7: Overall feedback ---
    print("\n💬 Feedback:")
    if avg >= DAILY_GOAL_MINUTES:
        print("🌟 Excellent consistency! You’re mastering your coding rhythm. Keep pushing your limits!")
    elif avg >= 60:
        print("👍 Great effort! You’re consistent — try stretching each session a bit more to hit your 1.5-hour goal.")
    else:
        print("🚀 Let's pick up the pace — even small, daily sprints will get you back on track.")
    
    if best_streak >= 5:
        print("🏆 You’re on a hot streak! Maintaining this pace will make coding second nature.")
    elif best_streak >= 3:
        print("🔥 Strong momentum — just a few more consistent days to build a long-term habit!")
    else:
        print("💡 Try to code daily, even briefly — consistency beats intensity.")


if __name__ == "__main__":
    analyze_coding_hours("data.txt")
