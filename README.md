# PIF/PUF: A Narrative Filter Framework for X

![Logo](logo.png) <!-- Placeholder for future logo -->

PIF/PUF, a narrative filter framework, processes X’s 500M daily posts, born from my novel idea of defining “real” news as PIF (Physical Impact Filter) for tangible events, while all other news falls under PUF (Politics Understanding Fun), with JBSM (SOUR, BLABBER, JABBER, MISC) as non-news for research.

## Purpose
PIF highlights real impacts (Category 1–5) with Confidence (High ≥80%, Medium 70–79%, Low <70%), Scope, and Impacts, tagged **★ HIGH-IMPACT AHA!** or **! EMERGENCY WARNING**. PUF categorizes: PIF (5%), POLITICS (27%), UNDERSTANDING (24.5%), FUN (27.5%); JBSM (21%) includes SOUR (5%), BLABBER (7%), JABBER (4%), MISC (5%). Users drag/overlay posts, preview grades, and toggle subcategories. The dashboard offers: (1) country selection for top PIF events, (2) world clock, (3) notebook. Developed over months, 100% ready.

## Quick Guide
- **CAT (1–10)**: Fit strength (1=weak, 10=strong).
- **Grade (A+ to F)**: Reliability (A+ ≥95%, F <60%).
- **Confidence**: Certainty (High ≥80%, Low <70%).

## Licensing
PIF/PUF, including a provisional patent application (#63/845,773) for the PIF methodology filed July 2025, is available for potential acquisition. Interested parties can contact paulinea.gonensmith@gmail.com to discuss offers, with credit to Pauline Gonen-Smith optional based on agreement.

## Dashboard Features
(1) Country selection for PIF, (2) world clock, (3) notebook.

Uses multi-RSS for sentiment, ML (BERT-expandable). Upload October 18.

## Origin Story
On October 29, 2014, I first envisioned PIF, noting: “I’ve been thinking about how many individuals are affected by media big stories... I would love a standard practice to gauge how personally relevant the story is.” This idea, inspired by events like Ebola NYC to reduce fear-mongering evolved into PIF/PUF’s framework over months with Grok’s support.

## Getting Started
To use PIF/PUF, follow these steps:
1. **Request Code**: Email paulinea.gonensmith@gmail.com to request the PIF/PUF Python script.
2. **Install Python**: Ensure Python 3.8+ is installed (download from python.org, verify with `python --version`).
3. **Run Script**: Save the received `pif_puf.py`, navigate to its folder in a terminal, and run `python pif_puf.py`. It categorizes X posts (e.g., PIF for impacts >1K) and outputs CAT scores (1–10).
4. **Customize**: Adjust the script for your X API key or dashboard preferences (e.g., country filters).

## Example Files
The following 17 files provide sample stories categorized by PIF/PUF, showcasing its application:
- `shutdown.md`: Example of a PIF event (shutdown impacting 500K, Category 4).
- `nc_camp_flood_warning_pif.md`: Example of a PIF warning (flood affecting 10K, Category 2).
- `nj_pride_parade_pif.md`: Example of a PIF celebration (parade with 20K attendees, Category 3).
- `musk_starlink.md`: Example of a POLITICS opinion (Starlink policy debate).
- `cr_bill_johnson.md`: Example of a POLITICS policy discussion (infrastructure funding).
- `nj_hindu_vandalism_understanding.md`: Example of UNDERSTANDING insight (temple vandalism analysis).
- `florence_antisemitism_understanding.md`: Example of UNDERSTANDING historical insight (Florence antisemitism).
- `nj_cherry_blossom_pif.md`: Example of FUN event (cherry blossom festival with 3K attendees).
- `boss_meme_fun.md`: Example of FUN humor (boss meme trend).
- `british_jews_jabber.md`: Example of JABBER venting (British Jews’ experiences).
- `child_cops_jabber.md`: Example of JABBER rumor (child police claim).
- `big_pharma_conspiracy.md`: Example of BLABBER speculation (Big Pharma cover-up).
- `nj_pesticide_misinfo.md`: Example of BLABBER misinformation (NJ pesticide hoax).
- `vaccine_conspiracy_sour.md`: Example of SOUR hoax (vaccine infertility claim).
- `election_rigging_sour.md`: Example of SOUR conspiracy (election rigging claim).
- `cr_page57.md`: Example of MISC nonsense (cryptic CR page 57).
- `robbery_scare_misc.md`: Example of MISC prank (robbery scare incident).

The tool is 100% ready, with all tasks completed; upload planned for October 18, guided by non-tech vision with engaging authenticity; developed over months. Uses multi-RSS (Full Fact, AFP, Washington Post, Poynter, BBC, AP, Reuters, Snopes, FactCheck.org, PolitiFact, NASA Earth, EPA, NOAA, IPCC, USGS) for X sentiment (PIF/PUF - Grade A+ to F reliability), with ML bias detection (BERT-expandable). The Narrative Dynamics Tracker enhances filtering, shift tracking, pre-post previews, and JBSM research, boosting Grok and X.
