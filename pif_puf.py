"""
PIF/PUF Framework — ClarityGuard
Created by Pauline Gonen-Smith (@clarityguard)
Open source - MIT License
"""

import re
from typing import Dict, Any

# ====================== PIF/PUF Core ======================

def analyze_text(text: str) -> Dict[str, Any]:
    if not text or not text.strip():
        return {"error": "No text provided"}

    t = text.lower()

    # ==================== 1. PIF - ALWAYS FIRST ====================
    # Simple impact detection (expand with real ML/API later)
    impact_score = 0
    impact_desc = ""
    impact_type = "neutral"
    location = "Global"

    if any(word in t for word in ["tornado", "hurricane", "flood", "earthquake", "war", "strike", "disaster", "casualty"]):
        impact_score = 4
        impact_type = "negative"
        impact_desc = "Major population impact - safety, infrastructure, or humanitarian"
    elif any(word in t for word in ["lithium", "discovery", "breakthrough", "vaccine", "trade deal", "major investment"]):
        impact_score = 3
        impact_type = "positive"
        impact_desc = "Emerging positive impact - economic or technological"
    elif any(word in t for word in ["shooting", "attack", "protest", "protest", "election"]):
        impact_score = 3
        impact_type = "negative"
        impact_desc = "Significant localized or national security impact"

    # ==================== 2. Bucket Classification ====================
    if impact_score >= 3:
        bucket = "HIGH_PIF"
    elif impact_score > 0:
        bucket = "EMERGING_PIF"
    elif any(word in t for word in ["trump", "biden", "harris", "putin", "israel", "gaza", "iran", "ukraine", "election", "tariff", "tax"]):
        bucket = "POLITICS"
    elif any(word in t for word in ["law", "policy", "executive order", "regulation", "budget"]):
        bucket = "POLICIES"
    elif any(word in t for word in ["study", "discovery", "research", "breakthrough", "what is", "explain"]):
        bucket = "UNDERSTANDING"
    elif any(word in t for word in ["fun", "meme", "festival", "sports", "celebrity"]):
        bucket = "FUN"
    elif re.search(r'(!{3,}|\b(all|every|never|always)\b)', text) or text.isupper():
        bucket = "JABBER"
    elif any(word in t for word in ["nigger", "faggot", "kike", "cunt", "retard", "kill yourself"]):
        bucket = "SOUR"
    elif any(word in t for word in ["flat earth", "chemtrails", "cabal", "adrenochrome"]):
        bucket = "BLABBER"
    else:
        bucket = "MISC"

    # ==================== 3. Output ====================
    return {
        "bucket": bucket,
        "pif_cat": impact_score,
        "impact_type": impact_type,
        "impact_desc": impact_desc,
        "location": location,
        "raw_text": text[:200] + "..." if len(text) > 200 else text
    }


# Simple demo
if __name__ == "__main__":
    sample = "Iran proposes reopening Strait of Hormuz amid rising oil prices affecting global supply chains."
    result = analyze_text(sample)
    print(result)
