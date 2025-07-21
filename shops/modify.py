import random
import yaml


def modify_yaml(file_path):
    # YAMLファイルを読み込む
    with open(file_path, "r") as file:
        data = yaml.safe_load(file)

    MATCH_ID = ["leggings", "boots", "chestplate", "helmet"]
    ARMOR_TYPE = {
        "leggings": "legs",
        "boots": "feet",
        "chestplate": "chest",
        "helmet": "head",
    }
    # items_for_saleの各値を更新
    if "items_for_sale" in data:
        for item in data["items_for_sale"].keys():
            value = data["items_for_sale"][item]

            if any(match in value["item"]["id"] for match in MATCH_ID):
                # "minecraft:unbreakable"を追加
                if "components" not in value["item"]:
                    value["item"]["components"] = {}
                value["item"]["components"]["minecraft:unbreakable"] = "{}"
                armor_type = ""
                for type_key, type_value in ARMOR_TYPE.items():
                    if type_key in value["item"]["id"]:
                        armor_type = type_value
                        break
                random_value = str(random.randint(1, 100000000))
                value["item"]["components"]["minecraft:attribute_modifiers"] = (
                    '[{id:"1'
                    + random_value
                    + '",type:"armor",amount:4,operation:"add_value",slot:"'
                    + armor_type
                    + '"},{id:"2'
                    + random_value
                    + '",type:"armor_toughness",amount:2.5,operation:"add_value",slot:"'
                    + armor_type
                    + '"}]'
                )

    # YAMLファイルを保存
    with open(file_path, "w") as file:
        yaml.dump(data, file, allow_unicode=True)


# 使用例
file_path = "hololive-goods.yml"  # 対象のYAMLファイルのパスを指定
modify_yaml(file_path)
