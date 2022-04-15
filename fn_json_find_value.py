#  samples
#
#

import sys

some_json = [
    {"id": "57ead194e4b024b21e43ec8e", "displayName": "Duplicate of Centage Default"},
    {"id": "589c74f1e4b004c69fb4128f", "displayName": "Centage Test Connection"},
    {
        "id": "589dc9bde4b020d405b670c2",
        "displayName": "Centage Default Destinations (Copy)",
    },
    {
        "id": "589dca24e4b020d405b670d4",
        "displayName": "Centage Default Destinations (Copy) (Copy)",
    },
    {"id": "590c92b5e4b06059774a8187", "displayName": "SQL-SSAS-2016"},
    {"id": "59664142e4b06294da4d3a30", "displayName": "SQL-SSAS-2014"},
    {"id": "59664142e4b06294da4d3b30", "displayName": "Centage Default"},
]


def find_items(input_string):
    """find a search string within json data; return all matches

    :param input_string: string to search for
    :type input_string: str
    :returns: result: collection of id / displayName values
    :rtype: list
    """

    find_result = []
    # requires the sample json data in outer scope
    for item in some_json:
        if (
            input_string in item["id"] or input_string in item["displayName"]
        ) and input_string != "":
            # found a desired matching entry
            find_result.append(item)

    return find_result


def main():
    print("(id_name) main:")
    print()
    print(":::::::::::::::::::::::::::::::::::")

    # SANITY
    # Q:  search case-sensitive ?
    search_item = "e4b0"  # id item, 7 (all) occurrences
    print(f"\n :: search_item :: {search_item}")
    search_result = find_items(search_item)
    for item in search_result:
        print(f" id = {item['id']}, displayName = {item['displayName']}")

    search_item = "Centage"  # displayName item, 5 occurrences
    print(f"\n :: search_item :: {search_item}")
    search_result = find_items(search_item)
    for item in search_result:
        print(f" id = {item['id']}, displayName = {item['displayName']}")

    print(":::::::::::::::::::::::::::::::::::")
    print()
    print("(id_name) end::")

    return 0


# ----------------------------------------
if __name__ == "__main__":
    result = main()
    sys.exit(0)
