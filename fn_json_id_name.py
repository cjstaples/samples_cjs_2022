#  samples
#
#

import sys

some_json = [
    {
        "id": "57ead194e4b024b21e43ec8e",
        "displayName": "Duplicate of Centage Default"
    },
    {
        "id": "589c74f1e4b004c69fb4128f",
        "displayName": "Centage Test Connection"
    },
    {
        "id": "589dc9bde4b020d405b670c2",
        "displayName": "Centage Default Destinations (Copy)"
    },
    {
        "id": "589dca24e4b020d405b670d4",
        "displayName": "Centage Default Destinations (Copy) (Copy)"
    },
    {
        "id": "590c92b5e4b06059774a8187",
        "displayName": "SQL-SSAS-2016"
    },
    {
        "id": "59664142e4b06294da4d3a30",
        "displayName": "SQL-SSAS-2014"
    },
    {
        "id": "59664142e4b06294da4d3b30",
        "displayName": "Centage Default"
    }
]


def main():
    print('(id_name) main:')
    print()
    print(f":::::::::::::::::::::::::::::::::::")

    for item in some_json:
        # or simply print(f"{item}")
        print(f"  id = {item['id']}, displayName = {item['displayName']}")

    print(f":::::::::::::::::::::::::::::::::::")
    print()
    print('(id_name) end::')

    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(0)
