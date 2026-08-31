"""
PIF/PUF + ClarityGuard — daily prompt generator
-----------------------------------------------
Generates a ready-to-paste daily reading prompt.

PIF = Population Impact Factor.
PIF/PUF is Pauline Gonen-Smith's framework, developed as a
disclosed collaboration with Grok (xAI): she defined the framework;
Grok produced the working prompts, examples, and repo text.

Usage:
    python pif_puf.py

Copy the output into Grok (or another model with search) for today's date.
"""

from datetime import datetime

# ====================== USER SETTINGS ======================
# Example: "August 31, 2026"   Leave as None for today's date.
MANUAL_DATE = None

# Change this to your place.
LOCAL_FILTER = "Monmouth / Middletown NJ"

# Optional tracking chart row + positive PIF cumulative tracker
INCLUDE_TRACKING = False
# ===========================================================


def get_current_date() -> str:
    if MANUAL_DATE:
        return MANUAL_DATE
    return datetime.now().strftime("%B %d, %Y")


def generate_daily_prompt() -> str:
    date_str = get_current_date()

    prompt = f"""You are ClarityGuard applying the PIF/PUF framework for a daily reading on {date_str}.

PIF = Population Impact Factor (Cat 1–5): how many real people are affected.
PIF/PUF is Pauline Gonen-Smith's framework. Apply it as a disclosed Grok collaboration: impact first, calm tone, no attack mode.

Perform a genuine real-time scan using your available search tools.

Output the following sections:

**PIF** (Population Impact Factor)
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

**Local Filter** ({LOCAL_FILTER})

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
Be accurate, balanced, and calm. Focus on Population Impact Factor rather than media volume or noise.
"""
    return prompt


if __name__ == "__main__":
    print(generate_daily_prompt())
