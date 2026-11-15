"""Offline template-based story generator for Cheshire Code."""
import argparse
import json
import random
from datetime import datetime, timezone
from pathlib import Path

SEEDS = {
    "mystery": ("a silver key", "an abandoned library", "the key whispered a forgotten name", "the name belonged to its owner"),
    "wonder": ("a glass star", "a garden above the clouds", "the star glowed whenever someone told the truth", "it had been waiting for one honest heart"),
    "eerie": ("a pocket watch", "a silent train station", "its hands moved only when nobody looked", "the final train was arriving from tomorrow"),
}
HOOKS = [
    "The forest had one rule: never follow the lights.",
    "At midnight, the old book opened by itself.",
    "Everyone heard the clock. Only one person saw it move backwards.",
    "The door appeared every night — but never in the same place.",
]
STYLE = "cinematic fantasy, magical realism, atmospheric mist, dramatic lighting, vertical 9:16, no text, no watermark"

def build_story(theme="mystery", mood="wonder", duration=30, title=None, seed=None):
    if theme not in SEEDS:
        raise ValueError("theme must be mystery, wonder, or eerie")
    if duration not in (15, 30, 45, 60):
        raise ValueError("duration must be 15, 30, 45, or 60")
    rng = random.Random(seed)
    obj, place, turn, reveal = SEEDS[theme]
    hook = rng.choice(HOOKS)
    beats = [
        ("HOOK", hook),
        ("DISCOVERY", f"Inside {place}, a traveller discovered {obj}."),
        ("ESCALATION", f"Then {turn}."),
        ("REVEAL", f"At last, the truth appeared: {reveal}."),
        ("ENDING", "Some doors are not meant to be opened. Others are waiting for you."),
    ]
    count = min(5, max(3, round(duration / 8)))
    selected = beats[:count]
    base, extra = divmod(duration, count)
    cameras = ["slow push-in", "gentle tracking shot", "macro detail", "wide reveal", "slow pull-back"]
    scenes = []
    for i, (beat, line) in enumerate(selected):
        scenes.append({
            "scene": i + 1,
            "beat": beat,
            "duration_seconds": base + (1 if i < extra else 0),
            "voiceover": line,
            "visual_prompt": f"{line} Show {obj} in {place}; clear focal point, rich depth, subtle magical particles; {STYLE}.",
            "camera": cameras[i],
        })
    return {
        "project": "Cheshire Code AI Factory",
        "account": "@cheshire193",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "DRAFT — review before production or publishing",
        "title": title or f"The Secret of {obj.title()}",
        "theme": theme, "mood": mood, "duration_seconds": duration, "language": "en",
        "hook": hook,
        "script": " ".join(line for _, line in selected),
        "scenes": scenes,
        "caption": f"What would you do if you found {obj}? ✨",
        "hashtags": ["#CheshireCode", "#FantasyTok", "#MysteryStory", "#MagicalWorld", "#StoryTok"],
        "review_checklist": [
            "Check story originality and clarity",
            "Proofread all on-screen text",
            "Verify image, music, and sound usage rights",
            "Review final video manually before publishing",
        ],
    }

def main():
    parser = argparse.ArgumentParser(description="Generate a Cheshire Code TikTok story draft")
    parser.add_argument("--theme", choices=sorted(SEEDS), default="mystery")
    parser.add_argument("--mood", default="wonder")
    parser.add_argument("--duration", type=int, choices=(15, 30, 45, 60), default=30)
    parser.add_argument("--title")
    parser.add_argument("--seed", type=int)
    parser.add_argument("--out", default="output/story-draft.json")
    args = parser.parse_args()
    data = build_story(args.theme, args.mood, args.duration, args.title, args.seed)
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Draft saved: {path} | {len(data['scenes'])} scenes | {args.duration}s")

if __name__ == "__main__":
    main()
