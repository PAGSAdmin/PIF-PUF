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
Forgotten Conflicts are PIF (world caseloads the feed dropped), not PUF.
PUF = Politics, Policies, Understanding, Fun only.
PIF/PUF is Pauline Gonen-Smith's framework. Apply it as a disclosed Grok collaboration: impact first, calm tone, no attack mode.

Perform a genuine real-time scan using your available search tools.
Then do these three checks so high-impact files are not dropped:
1. After the world brief, run an impact search (death toll + outbreak / quake / flood / collapse), not only top headlines.
2. Compare the front page to the standing roster. If a roster item vanished from headlines, keep it under PIF recoveries or Forgotten Conflicts.
3. Local is a separate pass: {LOCAL_FILTER} + {date_str}. Local PUF items belong in Local Filter, not in world PUF.

Output the following sections:

**PIF** (Population Impact Factor)
- List up to 8 stories with Cat level (1–5) and a short description. Do not pad to 8 if the signal is thinner.
- Put breaking or still-escalating shocks first.
- Then list standing high-caseload recoveries that the feed has already dropped. Current standing files until the caseload has actually fallen:
  - Venezuela twin earthquakes, 24 June 2026
  - Colombia M7.4 earthquake, 10 August 2026 (Chocó / Valle del Cauca / Risaralda)
  - Ceuta, Spain / Morocco border surge, 30–31 July 2026
- Add **! EMERGENCY WARNING** for Cat 4 or 5 where appropriate (including recoveries that are still Cat 4–5 by bodies, not by novelty).

**Mid-PIF Items**
- Smaller Cat 1–2 physical-impact items with start dates when known. Caseload required. Debates go under PUF, not here.

**Positive PIF Spotlight**
- Highlight clearly positive high-impact developments.

**Forgotten Conflicts**
- World only. Wars and high-caseload files the feed has dropped (Sudan, Myanmar, Sahel, Haiti, South Sudan, and any peer). Not local. Not PUF.

**Emerging PIF**
- Note any developing future signals worth watching.

**Top Surfacing PUF**
- **Politics**
- **Policies**
- **Understanding** (use sub-tags where helpful)
- **Fun** — Only stories that genuinely break through about large celebrations, major sports/games, awards, or reasonable positive PIF-level joyful events.

**Local Filter** ({LOCAL_FILTER})
- Local physical files and any local PUF (hearings, town politics, local fun).

**What changed since yesterday**
- One short paragraph summarizing the main shifts from the previous day.

**Signal vs Noise note**
- One line noting how concentrated or sparse the real high-impact signal feels today.

**Story duration**
- Note how long the main dominant stories have been active, including standing recoveries.

**How this page is made**
Each morning around 7:30 a.m. US Eastern, public wires and sitreps are searched. A story's population is the people reported affected by that event (killed, injured, missing, displaced), not a survey sample and not this author's network or zip code. Cat 1–5 is an ordinal judgment of that caseload, not a fixed formula. The Monmouth / Middletown line is a local glance only; it does not set the ranking. Figures move by desk. This is a snapshot, written with disclosed Grok help, not a wire service.

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
