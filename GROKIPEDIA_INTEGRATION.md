# PIF/PUF + Grokipedia Integration Demo

> **A real-time narrative filter for Grokipedia entries**  
> *Built by Pauline Gonen-Smith – 40 years of research-administration expertise*  
> *Provisional patent #63/845,773 – filed 17 July 2025*  

---

## What This Demo Does

1. **User opens a Grokipedia page** (e.g., “Hurricane Melissa 2025”).  
2. **PIF/PUF filter (optional toggle)** appears next to the article.  
3. When activated, Grok calls the PIF/PUF engine and **injects a live sidebar** with:
   - **PIF Impact Level** (1–5)  
   - **Confidence** (High / Medium / Low)  
   - **Grade** (A+ … F)  
   - **Key Impacts** (personal, social, economic, environmental)  
   - **Emergency Badge** (`! EMERGENCY WARNING`)  
   - **Actionable Suggestion** (evacuate, monitor NHC, etc.)  
   - **Live X chatter** (Community Pulse Check) filtered by Clarity Guard  

The result: **encyclopedic knowledge + verified, urgent social context** in one glance.

---

## Why It Works

| Grokipedia | PIF/PUF |
|------------|---------|
| **Static, authoritative facts** (NOAA, Reuters, peer-reviewed) | **Dynamic, real-time social narrative** (X posts, pre-post triage) |
| Strong on *obscure data* | Strong on *impact urgency* & *noise reduction* |
| Weak on *countering widely-distributed myths* | **Clarity Guard** removes 21 % junk (JABBER, BLABBER, SOUR, MISC) |
| Needs **contextual verification** | Supplies **Confidence ≥ 80 %**, **Grade**, **audit logs** |

Together they become a **truth-maximising loop** for NGOs, journalists, and everyday users.

---

## Architecture (High-Level)


1. **Grokipedia** sends the article title + key entities to Grok.  
2. **Grok** queries the **PIF/PUF service** (your Python script).  
3. **PIF/PUF** returns a JSON payload (example below).  
4. **Sidebar** renders the payload with badge icons, colour-coded confidence, and a “Learn more” link back to the full PIF/PUF analysis.

---

## JSON Payload Example (Hurricane Melissa)

```json
{
  "pif": {
    "level": 5,
    "description": "Catastrophic – >1 M affected",
    "confidence": "High",
    "confidence_pct": 92,
    "grade": "A",
    "badge": "! EMERGENCY WARNING",
    "haptic": true
  },
  "impacts": {
    "personal": "7 vulnerable communities evacuated, shelters open",
    "social": "Isolated rural areas, rescue ops overwhelmed",
    "economic": "Estimated $2 B+ damage, power out for 300 k homes",
    "environmental": "15-40 in rain, landslides, coastal erosion"
  },
  "suggestion": "Evacuate low-lying areas immediately. Monitor NHC updates.",
  "pulse": {
    "volume": 12_400,
    "trend": "rising",
    "top_hashtags": ["#MelissaEvac", "#JamaicaStorm"]
  }
}

