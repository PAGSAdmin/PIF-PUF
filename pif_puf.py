"""
PIF/PUF Daily Prompt Generator
------------------------------
Generates a ready-to-use daily PIF/PUF prompt.

Created by Pauline Gonen-Smith
This is an open-source project.

Usage:
    python pif_puf.py

The script outputs a complete, detailed daily prompt you can copy and paste to Grok.

Features:
- Full current structure (PIF, Mid-PUF, Positive PIF Spotlight, Emerging PIF, PUF layers)
- Includes: What changed since yesterday, Signal vs Noise, Story duration
- Tracking chart / Positive PIF tracker is OPTIONAL (toggle below)
- Date handling: tries to use today's date automatically, with manual override option
"""

from datetime import datetime

# ====================== USER SETTINGS ======================
# Set a specific date here if you don't want to use today's date
# Format: "June 9, 2026"   Leave as None to use current date automatically.
MANUAL_DATE = None

# Set to True if you want the tracking chart + Positive PIF tracker included
# (useful for demonstrations or when you want to update the chart)
INCLUDE_TRACKING = False
# ===========================================================


def get_current_date() -> str:
    if MANUAL_DATE:
        return MANUAL_DATE
    return datetime.now().strftime("%B %d, %Y")


def generate_daily_prompt() -> str:
    date_str = get_current_date()

    prompt = f"""You are my PIF/PUF daily analyst for {date_str}.

Perform a genuine real-time scan using your available search tools.

Output the following sections using the established PIF/PUF format:

**PIF** (Real Population Impacts)
- List the top 2–3 stories with Cat level (1–5) and a short description.
- Add **! EMERGENCY WARNING** for Cat 4 or 5 where appropriate.

**Mid-PUF Items**
- List relevant Cat 2 and Cat 1 items with start dates when known.

**Positive PIF Spotlight**
- Highlight clearly positive high-impact developments.

**Emerging PIF**
- Note any developing future signals worth watching.

**Top Surfacing PUF**
- **Politics**
- **Policies**
- **Understanding** (use sub-tags where helpful)
- **Fun** — Only stories that genuinely break through about large celebrations, major sports/games, awards, or reasonable positive PIF-level joyful events.
- **Forgotten Conflicts**

**Local Filter** (Monmouth / Middletown NJ or your chosen location)

**What changed since yesterday**
- One short paragraph summarizing the main shifts from the previous day.

**Signal vs Noise note**
- One line noting how concentrated or sparse the real high-impact signal feels today.

**Story duration**
- Note how long the main dominant stories have been active.

"""

    if INCLUDE_TRACKING:
        prompt += """
**Positive PIF cumulative tracker** (building)
- Briefly note any positive high-impact developments observed so far.

**Tracking Chart row (optional)**
- Provide a suggested row for the tracking chart in markdown format.
"""

    prompt += """
Be accurate, balanced, and calm. Focus on real population impact rather than media volume or noise.
"""
    return prompt


if __name__ == "__main__":
    print(generate_daily_prompt())