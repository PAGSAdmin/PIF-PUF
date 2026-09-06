# PIF/PUF + ClarityGuard

<p align="center">
  <img src="PIF_PUF_Wynn.Logo.png" alt="PIF/PUF logo" width="220">
</p>

**PIF = Population Impact Factor.** News by how many real people are affected (Cat 1–5).  
**PUF = Politics, Policies, Understanding, Fun.**  
**ClarityGuard = the calm prompt voice that applies that lens.**

These were always one project. They are together again in this repo.

PIF/PUF is Pauline Gonen-Smith’s framework, developed as a disclosed collaboration with Grok (xAI): she defined the framework; Grok produced the working prompts, examples, and repo text.

Open source (MIT). Unpaid public good. Use it, copy it, tweak it. Credit is appreciated.

---

## What this is

A simple alternative to algorithmic feeds. Instead of ranking posts by engagement, it asks:

1. **How many real people are affected?** (PIF — Population Impact Factor, Cat 1–5)
2. **What kind of story is the rest?** (PUF: Politics, Policies, Understanding, Fun)
3. **What is not news?** (JBSM: Jabber, Blabber, Sour, Misc)

The daily reading is the part that is actually in use. A fresh public copy is written to GitHub each morning.

Idea first noted 29 October 2014. Repo started 18 October 2025. Daily testing with Grok from March 2025.

---

## Scope and method

This is not a world census.

The watch is the shocks and debates that dominate U.S. platforms that day, plus standing files whose counted caseload has not closed, plus a Monmouth / Middletown glance.

PIF on the public page is split:

- **On the platforms today** — counted shocks that dominate U.S. feeds that day.
- **Still open, platforms moved on** — standing files whose table has not closed (recoveries and forgotten conflicts).

Mid-PIF lines carry a Cat. Social volume is a miss-check, not a ranking.

Each morning around 10:00 a.m. US Eastern, official sitreps and tables are searched first (WHO, Africa CDC, OCHA/ReliefWeb, NDRRMA, Nepal Police, UNGRD, IOM, USDA/APHIS, UKMTO/IMO maritime tables, national registers such as NZ DOC). Wires second, and only to fill a gap or show disagreement. Newspaper features last, never as the reason a story is listed. A story’s population is the people reported affected by that event, not a survey sample and not this author’s network or zip code. Cat 1–5 is an ordinal judgment of that caseload. Snapshot, disclosed Grok help, not a wire service.

---

## PUF lanes

The public [daily reading](examples/LATEST.md) is this watch. To change place or lanes, edit `LOCAL_FILTER` and the prompt block in `pif_puf.py`.

| Lane | What it is | Source |
|---|---|---|
| **Politics** | A named contest over power that is moving today | The actor’s desk first (command, court, filing); wires second |
| **Policies** | A rule, budget, or protocol that changed or was blocked today | Gazette / agency / docket |
| **Understanding** | The mechanism that makes a PIF or Politics item make sense today | Sitrep or specialist agency note |
| **Fun** | An official calendar lift for that calendar day | The register (FIBA, prize body, national calendar). If empty, say none |

---

## Read today’s example

Stable link: [examples/LATEST.md](examples/LATEST.md)

Updated each morning at **about 10:00 a.m. US Eastern Time**.  
That is **14:00 UTC / GMT** while the US is on daylight time, and **15:00 UTC / GMT** when the US is on standard time.

Dated archive stays in `examples/DAILY_YYYY-MM-DD.md`.

---

## Daily reading (the working tool)

```bash
python pif_puf.py
```

Copy the printed prompt into Grok with today’s date. You get:

- **PIF — on the platforms today**
- **PIF — still open, platforms moved on** (includes forgotten conflicts)
- **Mid-PIF** — smaller counted items, each with a Cat
- **Positive PIF Spotlight**
- **Emerging PIF**
- **Top Surfacing PUF** — Politics / Policies / Understanding / Fun
- **Local Filter** — default Monmouth / Middletown NJ
- **What changed since yesterday**
- **Signal vs Noise**
- **Story duration**

In `pif_puf.py` you can set `MANUAL_DATE`, `LOCAL_FILTER`, and which PUF lanes to keep.

Tone comes from ClarityGuard: calm, no attack mode, impact first, media volume last.

---

## ClarityGuard prompt (any model)

For a single article, post, or idea instead of a full daily scan, use [`CLARITYGUARD_PROMPT.md`](CLARITYGUARD_PROMPT.md).

Paste it into Grok, Claude, or ChatGPT, then add the text and: `Run this through ClarityGuard` or `Apply PIF/PUF to this`.

---

## How others can use it

1. Fork or clone this repo.
2. Read [examples/LATEST.md](examples/LATEST.md) or run `python pif_puf.py` and paste the output into any capable model with search.
3. Change `LOCAL_FILTER` to your place.
4. Keep or drop PUF lanes in the script. That is the intended way to improve it.
5. Scored examples in this folder (`PIF_CAT*`, `POLITICS_*`, `FUN_*`, `BLABBER_*`, etc.) show how a single post is labelled.

No install beyond Python 3. No API key required for the generator itself.

---

## Repo map

| File | Role |
|---|---|
| `pif_puf.py` | Daily prompt generator |
| `CLARITYGUARD_PROMPT.md` | Single-item prompt |
| `examples/LATEST.md` | Today’s public daily reading (new file ~10:00 a.m. US Eastern) |
| `examples/DAILY_YYYY-MM-DD.md` | Dated archive |
| `NOVELTY_STATEMENT.md` | Why the split is different |
| `GROKIPEDIA_INTEGRATION.md` | Proposed sidebar (not built) |
| Scored `*.md` examples | Worked labels, one post each |
| `LICENSE` | MIT. A July 2025 provisional (#63/845,773) expired; not for sale. |

The old [ClarityGuard](https://github.com/PAGSAdmin/ClarityGuard) repo now points here.

---

## Credit

Framework and original PIF idea: **Pauline Gonen-Smith** ([@clarityguard](https://x.com/clarityguard)).  
Prompts, examples, and repo text: disclosed collaboration with **Grok (xAI)**.

Feedback welcome, especially if you use the daily reading and want a calmer feed.
