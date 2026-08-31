# PIF/PUF + ClarityGuard

![PIF/PUF Logo](https://raw.githubusercontent.com/PAGSAdmin/PIF-PUF/main/PIF_PUF_Wynn.Logo.png)

**PIF = Population Impact Factor.** News by how many real people are affected (Cat 1–5).  
**ClarityGuard = the calm prompt voice that applies that lens.**

These were always one project. They are together again in this repo.

PIF/PUF is Pauline Gonen-Smith’s framework, developed as a disclosed collaboration with Grok (xAI): she defined the framework; Grok produced the working prompts, examples, and repo text.

Open source (MIT). Use it, copy it, tweak it. Credit is appreciated.

---

## What this is

A simple alternative to algorithmic feeds. Instead of ranking posts by engagement, it asks:

1. **How many real people are affected?** (PIF — Population Impact Factor, Cat 1–5)
2. **What kind of story is the rest?** (PUF: Politics, Policies, Understanding, Fun, Forgotten Conflicts)
3. **What is not news?** (JBSM: Jabber, Blabber, Sour, Misc)

The daily reading is the part that is actually in use. A fresh public copy is written to GitHub each morning.

Idea first noted 29 October 2014. Repo started 18 October 2025. Daily testing with Grok from March 2025.

---

## Read today’s example

Stable link (overwritten each morning):  
[examples/LATEST.md](examples/LATEST.md)

Dated archive stays in `examples/DAILY_YYYY-MM-DD.md`.

---

## Daily reading (the working tool)

```bash
python pif_puf.py
```

Copy the printed prompt into Grok with today’s date. You get:

- **PIF** — top Population Impact Factor stories, Cat 1–5 (`! EMERGENCY WARNING` on Cat 4–5)
- **Mid-PUF Items** — smaller Cat 1–2 items with start dates when known
- **Positive PIF Spotlight** — counters negativity bias on purpose
- **Emerging PIF** — early signals
- **Top Surfacing PUF** — Politics / Policies / Understanding / Fun / Forgotten Conflicts
- **Local Filter** — default Monmouth / Middletown NJ (change it in the script)
- **What changed since yesterday**
- **Signal vs Noise**
- **Story duration**

In `pif_puf.py` you can set `MANUAL_DATE` and turn `INCLUDE_TRACKING` on if you want the optional chart row.

Tone comes from ClarityGuard: calm, no attack mode, impact first, media volume last.

---

## ClarityGuard prompt (any model)

For a single article, post, or idea instead of a full daily scan, use [`CLARITYGUARD_PROMPT.md`](CLARITYGUARD_PROMPT.md).

Paste it into Grok, Claude, or ChatGPT, then add the text and: `Run this through ClarityGuard` or `Apply PIF/PUF to this`.

---

## How others can use it

1. Fork or clone this repo.
2. Read [examples/LATEST.md](examples/LATEST.md) or run `python pif_puf.py` and paste the output into any capable model with search.
3. Change the local filter to your place.
4. Tweak section order or wording in the script. That is the intended way to improve it.
5. Scored examples in this folder (`PIF_CAT*`, `POLITICS_*`, `FUN_*`, `BLABBER_*`, etc.) show how a single post is labelled.

No install beyond Python 3. No API key required for the generator itself.

---

## Repo map

| File | Role |
|---|---|
| `pif_puf.py` | Daily prompt generator |
| `CLARITYGUARD_PROMPT.md` | Single-item prompt |
| `examples/LATEST.md` | Today’s public daily reading |
| `examples/DAILY_YYYY-MM-DD.md` | Dated archive |
| `NOVELTY_STATEMENT.md` | Why the split is different |
| `GROKIPEDIA_INTEGRATION.md` | Proposed sidebar (not built) |
| Scored `*.md` examples | Worked labels, one post each |
| `LICENSE` | MIT, with a note on provisional patent #63/845,773 |

The old [ClarityGuard](https://github.com/PAGSAdmin/ClarityGuard) repo now points here.

---

## Credit

Framework and original PIF idea: **Pauline Gonen-Smith** ([@clarityguard](https://x.com/clarityguard)).  
Prompts, examples, and repo text: disclosed collaboration with **Grok (xAI)**.

Feedback welcome, especially if you use the daily reading and want a calmer feed.
