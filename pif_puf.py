# pif_puf.py - PIF/PUF Prototype (October 18, 2025)
def calculate_pif_impact(affected_people):
    """Calculate PIF category based on number of people affected."""
    if affected_people > 1000000:
        return 5, 'Catastrophic'
    elif affected_people > 100000:
        return 4, 'Major'
    elif affected_people > 10000:
        return 3, 'Significant'
    elif affected_people > 1000:
        return 2, 'Moderate'
    else:
        return 1, 'Negligible'

def categorize_story(story_text):
    """Categorize story into PIF, PUF, or JBSM based on content."""
    lower_text = story_text.lower()
    if 'shutdown' in lower_text or 'flood' in lower_text or 'parade' in lower_text:
        return 'PIF'
    elif 'policy' in lower_text or 'debate' in lower_text:
        return 'POLITICS'
    elif 'insight' in lower_text or 'historical' in lower_text:
        return 'UNDERSTANDING'
    elif 'festival' in lower_text or 'meme' in lower_text:
        return 'FUN'
    elif 'venting' in lower_text or 'rumor' in lower_text:
        return 'JABBER'
    elif 'conspiracy' in lower_text or 'misinfo' in lower_text:
        return 'BLABBER'
    elif 'hoax' in lower_text:
        return 'SOUR'
    else:
        return 'MISC'

# Test example
story = "Trump commutes George Santos sentence, affecting 50,000 people."
category = categorize_story(story)
cat_num, cat_desc = calculate_pif_impact(50000)
print(f"Category: {category}, PIF Impact: Category {cat_num} - {cat_desc}")
Upload pif_puf.py script
