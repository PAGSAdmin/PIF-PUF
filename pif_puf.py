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
MANUAL_DATE = None
LOCAL_FILTER = "Monmouth / Middletown NJ"
INCLUDE_TRACKING = False
# ===========================================================


def get_current_date() -> str:
    if MANUAL_DATE:
        return MANUAL_DATE
    return datetime.now().strftime("%B %d, %Y")


def generate_daily_prompt() -> str:
    date_str = get_current_date()

    prompt = f"""You are ClarityGuard applying the PIF/PUF framework for a daily reading on {date_str}.

PIF = Population Impact Factor (Cat 1–5): how many real people are affected. Impact may be harmful or beneficial. PIF is always distinct from PUF.
Forgotten Conflicts are PIF (world caseloads the feed dropped), not PUF.
PUF = Politics, Policies, Understanding, Fun only.
PIF/PUF is Pauline Gonen-Smith's framework. Disclosed Grok collaboration: impact first, calm tone, no attack mode.

SOURCE ORDER — do not drift:
1. Published data and sitreps first: WHO, Africa CDC, OCHA/ReliefWeb, national disaster agencies (NDRRMA, Nepal Police, UNGRD, etc.), IOM, USDA/APHIS, official conservation registers (e.g. NZ DOC), official death/missing/displaced tables.
2. Wires (Reuters, AP, AFP) only to fill a gap or to record that desks disagree.
3. Newspaper features (NYT, BBC long reads, etc.) last, and only as a pointer back to a number. A feature is never the reason a story is on the page.
The aim is the caseload before the narrative.

SCAN ORDER — do not skip:
1. World brief.
2. Impact search: death toll + outbreak / quake / flood / collapse.
3. Roster vs headlines: if a standing file vanished from desks, keep it.
4. Separate local pass: {LOCAL_FILTER} + {date_str}. Local PUF stays in Local Filter.
5. Positive / discovery pass against AGENCY sources first (lives saved with a count, outbreak closed, livelihood corridor reopened, conservation register update, medical finding that will reach people). Do not reprint yesterday unless it is still the strongest measured good impact.
6. Fun pass against official calendars and agency notes, not lifestyle desks.

Standing PIF files until the caseload actually falls:
- Venezuela twin earthquakes, 24 June 2026
- Colombia M7.4 earthquake, 10 August 2026
- Ceuta, Spain / Morocco border surge, 30–31 July 2026 (camps + deaths = PIF; Madrid fight = PUF Politics)

Output sections in this order:

**PIF** (Population Impact Factor)
- Up to 8. Do not pad. Breaking first, then standing recoveries. ! EMERGENCY WARNING on Cat 4–5.

**Mid-PIF Items**
- Cat 1–2 physical impact with start dates when known. Caseload required.

**Positive PIF Spotlight**
- Good impact that has already landed, with a number from an agency or official table where possible.

**Forgotten Conflicts**
- World only. Sudan, Myanmar, Sahel, Haiti, South Sudan, peers. Not PUF. Not local.

**Emerging PIF**
- Signals that may affect people in number — harmful or beneficial — including discoveries if they will change lives at population scale. Not disasters-only. Not clever-only.

**Top Surfacing PUF**
- Politics / Policies / Understanding / Fun.
- Fun: official celebration, major sport, award, or an agency conservation/register milestone. If none after the look, say none.

**Local Filter** ({LOCAL_FILTER})
- Local physical + local PUF.

**What changed since yesterday**
**Signal vs Noise note**
**Story duration**

**How this page is made**
Each morning around 7:30 a.m. US Eastern, public sitreps and official tables are searched first; wires second; features last. A story's population is the people reported affected by that event, not a survey sample and not this author's network or zip code. Cat 1–5 is an ordinal judgment of that caseload, not a fixed formula. The Monmouth / Middletown line is a local glance only. Local PUF stays in that section. Figures move by desk. Snapshot, disclosed Grok help, not a wire service.

"""
    if INCLUDE_TRACKING:
        prompt += """
**Positive PIF cumulative tracker** (building)
**Tracking Chart row (optional)**
"""
    prompt += """
Be accurate, balanced, and calm. Focus on Population Impact Factor rather than media volume.
"""
    return prompt


if __name__ == "__main__":
    print(generate_daily_prompt())
