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

TRANSFER RULE: a file can move back and forth between the two blocks as the feeds change. Quiet is not closure. A file leaves the page entirely only when the responsible agency has closed the caseload (outbreak declared over; search ended and totals frozen; recovery file formally closed). Uganda Ebola is the model for a closed file (Positive Spotlight, not a PIF line).

Mid-PIF: smaller counted items, separate from both caps. Every Mid-PIF line MUST carry a Cat.

SOURCE ORDER — do not drift:
1. Official sitreps and tables: WHO, Africa CDC, OCHA/ReliefWeb, NDRRMA, Nepal Police, UNGRD, IOM, USDA/APHIS, UKMTO/IMO, FIBA/FIFA/World Athletics/IOC calendars, national registers (e.g. NZ DOC).
2. Wires only to fill a gap or show disagreement.
3. Features last. Never the reason a story is listed.

SCAN ORDER — do not skip:
World brief; impact search; roster vs headlines; local pass ({LOCAL_FILTER} + {date_str}); positive pass; Fun pass on TODAY's official calendar.

Standing files until the caseload is closed:
- Nepal–Tibet floods while search or totals still move
- DRC Bundibugyo Ebola while Africa CDC/WHO/ECDC list it active (move to still-open when U.S. platforms have dropped it)
- Hormuz / Iran since 28 Feb 2026 while UKMTO/IMO show suppressed transits or CENTCOM/IRGC record a new exchange
- Venezuela 24 June 2026; Colombia 10 August 2026; Ceuta 30–31 July 2026

PUF lanes — only what moved TODAY.
The public LATEST is this watch. Users change place and lanes in this file.

WHAT CHANGED: compare only to yesterday's examples/DAILY_YYYY-MM-DD.md. Name block transfers.

Output sections in order: PIF on the platforms today; PIF still open, platforms moved on; Mid-PIF (with Cats); Positive PIF Spotlight; Emerging PIF; Top Surfacing PUF; Local Filter; What changed since yesterday; Signal vs Noise; Story duration; How this page is made.

Header: PIF = Population Impact Factor. PUF = Politics, Policies, Understanding, Fun.
Tone: calm, impact first. Snapshot, not a wire service.
"""


if __name__ == "__main__":
    print(generate_daily_prompt())
