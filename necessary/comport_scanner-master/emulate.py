"""
Script for emulating Card ID requests to the database server
Run to test functionality of the whole system without actually scanning QR codes
"""

import asyncio
import re
import main as core
import config

async def main() -> None:
    input_pattern = re.compile(config.REGEX_EMULATE_INPUT)
    print("Type 'q' to exit the program.")
    while True:
        text = input("Input Card ID and Station ID separated by a space: ")
        if text.strip() == "q":
            break

        input_match = input_pattern.search(text)
        if input_match is None:
            print("Wrong syntax!")
        else:
            card_id = input_match.group(1)
            station_id = input_match.group(2)
            await core.send_card_id(card_id, station_id)


if __name__ == "__main__":
    asyncio.run(main())
