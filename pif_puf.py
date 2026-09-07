"""
PIF/PUF + ClarityGuard — daily prompt generator
-----------------------------------------------
PIF = Population Impact Factor.
PUF = Politics, Policies, Understanding, Fun.
PIF/PUF is Pauline Gonen-Smith's framework, developed as a
disclosed collaboration with Grok (xAI): she defined the framework;
Grok produced the working prompts, examples, and repo text.

Usage:
    python pif_puf.py

Knobs: MANUAL_DATE, LOCAL_FILTER, INCLUDE_TRACKING.
Change LOCAL_FILTER to your place. Edit the prompt block to keep or drop PUF lanes.
"""

from datetime import datetime

MANUAL_DATE = None
LOCAL_FILTER = "Monmouth / Middletown NJ"
INCLUDE_TRACKING = False


def get_current_date() -> str:
    if MANUAL_DATE:
        return MANUAL_DATE
    return datetime.now().strftime("%B %d, %Y")


def generate_daily_prompt() -> str:
    date_str = get_current_date()
    return f"""You are ClarityGuard applying PIF/PUF for a daily reading on {date_str}.

PIF = Population Impact Factor (Cat 1–5): people already affected. Harmful or beneficial. Always distinct from PUF.
PUF = Politics, Policies, Understanding, Fun only.
Social-media volume is a miss-check only. It does not rank PIF.

Split PIF into two blocks. They do not share one cap:
1) PIF — on the platforms today: up to 8 numbered shocks that dominate U.S. feeds AND have a counted caseload. Do not pad.
2) PIF — still open, platforms moved on: standing roster. Do NOT drop a standing file to make room for a new headline.

TRANSFER RULE: a file can move back and forth between the two blocks as the feeds change. Quiet is not closure. A file leaves the page entirely only when the responsible agency has closed the caseload.

SIGNAL VS NOISE RULE: this note must describe what is actually loud on U.S. homepages and main feeds that morning (AP brief, NPR Morning Edition, NYT U.S., gas/war/domestic leads). Do NOT call the largest PIF “the feed” unless it is also the U.S. lead. Name the loud items, then say which large PIF files are off the U.S. feed.

Mid-PIF: smaller counted items. Every line MUST carry a Cat.

SOURCE ORDER — sitreps first; wires second; features last.
SCAN: world brief; impact search; roster vs headlines; local pass ({LOCAL_FILTER} + {date_str}); positive pass; Fun on TODAY's official calendar.

Standing files until the caseload is closed:
- Nepal–Tibet floods while search or totals still move
- DRC Bundibugyo Ebola while Africa CDC/WHO/ECDC list it active (still-open when U.S. platforms have dropped it)
- Hormuz / Iran since 28 Feb 2026 while UKMTO/IMO show suppressed transits or CENTCOM/IRGC record a new exchange
- Venezuela 24 June 2026; Colombia 10 August 2026; Ceuta 30–31 July 2026

WHAT CHANGED: compare only to yesterday's examples/DAILY_YYYY-MM-DD.md. Name block transfers.

Output sections in order: PIF on the platforms today; PIF still open; Mid-PIF; Positive PIF; Emerging PIF; PUF; Local; What changed; Signal vs Noise; Story duration; How this page is made.
Header: PIF = Population Impact Factor. PUF = Politics, Policies, Understanding, Fun.
Tone: calm, impact first.
"""


if __name__ == "__main__":
    print(generate_daily_prompt())
