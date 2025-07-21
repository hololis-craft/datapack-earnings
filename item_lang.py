import yaml
import json

with open("ja_JP.json", "r", encoding="utf-8") as f:
    ja_json = json.load(f)

with open("JobsItems.yml", "r", encoding="utf-8") as f:
    jobs_items = yaml.safe_load(f)

for itemKey in jobs_items["ItemList"].keys():
    jobs_items["ItemList"][itemKey] = ja_json.get(
        f"item.minecraft.{itemKey.lower()}",
        ja_json.get(
            f"block.minecraft.{itemKey.lower()}", jobs_items["ItemList"][itemKey]
        ),
    )

for entityKey in jobs_items["EntityList"].keys():
    k = entityKey.lower()
    k = k.replace("0-", "")
    jobs_items["EntityList"][entityKey] = ja_json.get(
        f"entity.minecraft.{k}",
        jobs_items["EntityList"][entityKey],
    )

with open("JobsItems_ja_JP.yml", "w", encoding="utf-8") as f:
    yaml.dump(jobs_items, f, allow_unicode=True)
