# PIF/PUF: A Narrative Filter Framework for X

[Logo: PIF_PUF_Wynn_Logo.png](#) *(Coming soon: A Wynn rune (ᚹ) with a faint AI circuit trace on a black-gray-white gradient, symbolizing clarity's rediscovery, designed by Pauline Gonen-Smith)*

[Novelty Statement](./NOVELTY_STATEMENT.md)  
*Pre-read this to understand PIF/PUF's groundbreaking approach before diving in!*

Rooted in 40 years of admin expertise, PIF/PUF delivers an innovative framework incorporating best practices from pre-computer and AI eras, restoring them in this new age to establish clarity in social media chaos. It processes X’s 500M daily posts, offering a novel starting point to define “real” news as PIF (Physical Impact Filter) for tangible events, while all other news falls under PUF (Politics Understanding Fun), with JBSM (SOUR, BLABBER, JABBER, MISC) as non-news for research.

## Purpose
PIF/PUF provides an 8-category adaptive narrative filter (PIF, POLITICS, UNDERSTANDING, FUN, SOUR, BLABBER, JABBER, MISC) for users to adapt and expand with subcategories as needed. PIF scores real news impacts (Category 1=Negligible <1K affected; 5=Catastrophic >1M affected), accounting for approximately 5% of posts, including joyful events and crises, with Confidence (High ≥80%, Medium 70–79%, Low <70%), Scope (Worldwide/Country/U.S./State), [Personal/Social/Economic/Environmental Impacts], and Data Maturity (Speculative/Ongoing Trials/Mature). Badges include: ! EMERGENCY WARNING for verified disasters (with haptic buzz option for urgent alerts, e.g., NC floods), ★ HIGH-IMPACT AHA! for High Confidence, Mature stories (earned with a subtle "Great job!" for consistent quality posts), and ★ MISLEADING with “BREAKING: Caution” (for PIF, unverified within 6 hours, shifting to SOUR if untrue). PUF categorizes other news: POLITICS (27%), UNDERSTANDING (24.5%), FUN (22.5%), totaling 74%; JBSM (21%) includes SOUR (5%), BLABBER (7%), JABBER (4%), MISC (5%) for research. *User Features*: Drag/overlay posts, preview grades pre-post with suggestions, toggle subcategories (hidden unless “Show Details”), and track shifts on a dashboard with: (1) country selection, (2) world clock, (3) notebook. *Technical Enhancements*: Multi-RSS and ML bias detection (BERT-expandable) boost accuracy, with potential AI integration for real-time insights. For posts by users with >100K followers, PIF/PUF uses influence as a tiebreaker (e.g., Grade C), prioritizing PIF, POLITICS, UNDERSTANDING, FUN if intent aligns, defaulting to JBSM for harm/speculation. Developed over months, 100% ready as an adaptive narrative filter for adaptation.

## Quick Guide
- CAT (1–10): Fit strength (1=weak, 10=strong).
- Grade (A+ to F): Reliability (A+ ≥95%, F <60%).
- Confidence: Certainty (High ≥80%, Low <70%).

## Licensing
PIF/PUF, including a provisional patent application (#63/845,773) filed July 2025, is available for potential acquisition. Interested parties can contact paulinea.gonensmith@gmail.com to discuss offers, with credit to Pauline Gonen-Smith optional based on agreement.

## Dashboard Features
1. Country selection for top PIF events, enhanced by real-time X updates for geo-targeted alerts.
2. World clock for global scope, tracking story timing with live web data.
3. Notebook for user notes, auto-populated with fresh web facts for context.
4. Pre-post feedback: Preview category (PIF, PUF, JBSM), grade (A+ to F), and insights (e.g., ★ HIGH-IMPACT AHA! for learning, ! EMERGENCY WARNING with haptic option), supported by the Narrative Dynamics Tracker for filtering and shift tracking.

## Narrative Framework
PIF/PUF categorizes X’s 500M posts using a human storytelling lens:
- PIF: Agency-driven impact stories (e.g., floods, parades) where control shapes outcomes.
- POLITICS: Agency and communion debates (e.g., policy opinions) shaping community views.
- UNDERSTANDING: Redemption through insight (e.g., cultural data) turning chaos into growth.
- FUN: Communion and agency in joy (e.g., festivals, memes) fostering connection.
- JBSM: Distorted narratives—SOUR (failed agency in hoaxes), BLABBER (speculative communion), JABBER (emotional redemption), MISC (narrative breakdown)—for research. This contrasts with engagement metrics, grounding categories in narrative identity.

## Self-Reflection via Questionnaire
- Intent: Opt in to explore your story style with a future 20–50 yes/no questionnaire (to be crafted by experts), personalizing your PIF/PUF experience with insights tied to filter preferences.
- Description: Proposed enhancement clusters users into ~100 narrative types, offering self-reflection with opt-in consent, no data sharing.

## Getting Started
To use PIF/PUF, follow these steps:
1. Request Code: Email paulinea.gonensmith@gmail.com to request the PIF/PUF Python script.
2. Install Python: Ensure Python 3.8+ is installed (download from python.org, verify with `python --version` if comfortable).
3. Run Script: Save the received `pif_puf.py` and use it with provided support to categorize X posts (e.g., PIF for impacts >1K), outputting CAT scores (1–10).
4. Customize: Adjust the script with help for your X API key or dashboard preferences (e.g., country filters).

## Example Files
The following 16 files provide sample stories categorized by PIF/PUF, showcasing its application:
- [PIF_CAT4_shutdown.md](./PIF_CAT4_shutdown.md): Example of a PIF event (shutdown impacting 500K, Category 4).
- [PIF_CAT2_nc_camp_flood_warning_pif.md](./PIF_CAT2_nc_camp_flood_warning_pif.md): Example of a PIF warning (flood affecting 10K, Category 2).
- [PIF_CAT3_nj_pride_parade_pif.md](./PIF_CAT3_nj_pride_parade_pif.md): Example of a PIF celebration (parade with 20K attendees, Category 3).
- [POLITICS_musk_starlink.md](./POLITICS_musk_starlink.md): Example of a POLITICS opinion (Starlink policy debate).
- [POLITICS_cr_bill_johnson.md](./POLITICS_cr_bill_johnson.md): Example of a POLITICS policy discussion (infrastructure funding).
- [UNDERSTANDING_nj_hindu_vandalism_understanding.md](./UNDERSTANDING_nj_hindu_vandalism_understanding.md): Example of UNDERSTANDING insight (temple vandalism analysis).
- [UNDERSTANDING_florence_antisemitism_understanding.md](./UNDERSTANDING_florence_antisemitism_understanding.md): Example of UNDERSTANDING historical insight (Florence antisemitism).
- [FUN_nj_cherry_blossom_pif.md](./FUN_nj_cherry_blossom_pif.md): Example of FUN event (cherry blossom festival with 3K attendees).
- [FUN_boss_meme_fun.md](./FUN_boss_meme_fun.md): Example of FUN humor (boss meme trend).
- [JABBER_child_cops_jabber.md](./JABBER_child_cops_jabber.md): Example of JABBER rumor (child police claim).
- [BLABBER_big_pharma_conspiracy.md](./BLABBER_big_pharma_conspiracy.md): Example of BLABBER speculation (Big Pharma cover-up).
- [BLABBER_nj_pesticide_misinfo.md](./BLABBER_nj_pesticide_misinfo.md): Example of BLABBER misinformation (NJ pesticide hoax).
- [SOUR_vaccine_conspiracy_sour.md](./SOUR_vaccine_conspiracy_sour.md): Example of SOUR hoax (vaccine infertility claim).
- [SOUR_election_rigging_sour.md](./SOUR_election_rigging_sour.md): Example of SOUR conspiracy (election rigging claim).
- [MISC_cr_page57.md](./MISC_cr_page57.md): Example of MISC nonsense (cryptic CR page 57).
- [MISC_robbery_scare_misc.md](./MISC_robbery_scare_misc.md): Example of MISC prank (robbery scare incident).

The tool is 100% ready, with all tasks completed; uploaded on October 18, guided by non-tech vision with engaging authenticity; developed over months. Uses multi-RSS (Full Fact, AFP, Washington Post, Poynter, BBC, AP, Reuters, Snopes, FactCheck.org, PolitiFact, NASA Earth, EPA, NOAA, IPCC, USGS) for X sentiment (PIF/PUF - Grade A+ to F reliability), with ML bias detection (BERT-expandable). The Narrative Dynamics Tracker enhances filtering, shift tracking, pre-post previews, and JBSM research, boosting Grok and X.

## About
Open-source adaptive narrative filter for X posts.

## Releases
No releases published

## Packages
No packages published

## Footer
© 2025 GitHub, Inc.
