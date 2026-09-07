"""
PIF/PUF + ClarityGuard — daily prompt generator
-----------------------------------------------
PIF = Population Impact Factor.
PUF = Politics, Policies, Understanding, Fun.
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

PIF = Population Impact Factor (Cat 1–5). Always distinct from PUF.
PUF = Politics, Policies, Understanding, Fun only.

Two PIF blocks only. No Mid-PIF heading.
1) On the platforms today: up to 8. Counted caseload AND loud on U.S. feeds. Cat 1 belongs here if it is actually on U.S. homepages. Do not pad.
2) Still open, platforms moved on: roster. Every line still carries a Cat. Do not drop a standing file for a new headline.

TRANSFER: files move between blocks as feeds change. Leave the page only when the agency closes the caseload.

SIGNAL VS NOISE: name what is actually loud on U.S. homepages that morning. Do not call the largest PIF the feed unless it is also the U.S. lead.

SOURCE ORDER: sitreps first; wires second; features last.
SCAN: world brief; impact search; roster vs headlines; local pass ({LOCAL_FILTER} + {date_str}); positive pass; Fun on TODAY's official calendar.

Standing: Nepal–Tibet floods; DRC Ebola while listed active; Hormuz since 28 Feb 2026; Venezuela 24 June 2026; Colombia 10 August 2026; Ceuta 30–31 July 2026.

Output: PIF on platforms today; PIF still open; Positive PIF; Emerging PIF; PUF; Local; What changed; Signal vs Noise; Story duration; How this page is made.
Header: PIF = Population Impact Factor. PUF = Politics, Policies, Understanding, Fun.
"""


if __name__ == "__main__":
    print(generate_daily_prompt())
