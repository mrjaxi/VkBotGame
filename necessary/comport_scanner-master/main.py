from serial.tools.list_ports import comports
from serial.tools.list_ports_common import ListPortInfo
from serial import Serial, SerialException
from time import time
import asyncio
import aiohttp
import config
import re

station_ids: dict[str, int] = dict()
error_counter: dict[str, int] = dict()

def str_comport(comport: ListPortInfo) -> str:
    res = f"Устройство: {comport.device}"
    if comport.description.strip() != "":
        res += f"\nОписание: {comport.description.strip()}"
    return res


def debug(device_name: str, data: str) -> None:
    station_id = str(station_ids.get(device_name, None))
    if station_id is None:
        station_id = "нет станции"
    else:
        station_id = f"станция {station_id}"
    if data.strip() != "":
        print(f"Новые данные с устройства {device_name} ({station_id}): {data}")
        print("")


def detect_com_ports(print_out: bool = False) -> list[ListPortInfo]:
    ports = comports()
    if print_out:
        if len(ports) > 0:
            print("Обнаруженные COM-порты:")
            for ind, port in enumerate(ports):
                print(f"- Port {ind + 1}")
                print(str_comport(port))
        else:
            print("COM-порты не обнаружены.")
    return ports


def connect_com_ports(ports: list[ListPortInfo]) -> list[Serial]:
    print("")
    print("Подключение к COM-портам...")

    serials: list[Serial] = []
    for ind, port in enumerate(ports):
        try:
            ser = Serial(port=port.device, baudrate=config.BAUDRATE, timeout=config.TIMEOUT)
        except Exception as e:
            print(f"Не удалось подключиться к COM-порту {ind + 1}, устройству {port.device}.")
            print("Детали ошибки:", e)
            print("")
        else:
            serials.append(ser)
    print(f"Выполнено успешное подключение к {len(serials)} портам.")
    return serials


def update_station_id(device_name: str, station_id: int) -> None:
    station_ids[device_name] = station_id
    print(f"Устройству {device_name} присвоен номер станции {station_id}")


async def process_card_id(device_name: str, card_id: int) -> None:
    station_id = station_ids.get(device_name, None)
    if station_id is None:
        print(f"Устройству {device_name} не присвоена станция, но на нем была отсканирован ID игрока {card_id}. Отклонено")
        return
    print(f"ID игрока {card_id} отсканировали на станции {station_id} (устройство {device_name})")
    await send_card_id(card_id, station_id)


async def send_card_id(card_id: int, station_id: int) -> None:
    post_data = {"cardid": card_id, "position": station_id}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url=config.DATABASE_IP, data=post_data) as resp:
                status_code = resp.status
                text_response = (await resp.text()).strip()
    except Exception as e:
        print(f"Не удалось отправить данные об ID игрока и станции на сервер. Детали ошибки: {e}")
        print("")
    else:
        if status_code == 200:
            print("Данные об ID игрока и станции успешно отправлены на сервер.")
        else:
            print(f"Данные об ID игрока и станции были отправлены на сервер, но сервер вернул код ошибки {status_code}.")
            if text_response != "":
                print("Текстовый ответ сервера:", text_response)


def update_serials(ports: list[ListPortInfo], serials: list[Serial]) -> None:
    active_ports = {port.device for port in ports}
    queue_to_remove: list[Serial] = list()
    for serial in serials:
        if serial.port not in active_ports:
            queue_to_remove.append(serial)
    
    for serial in queue_to_remove:
        print(f"Устройство {serial.port} было удалено из списка COM-портов, т.к. не является активным.")
        error_counter.pop(serial.port, None)
        station_ids.pop(serial.port, None)
        serials.remove(serial)
    
    current_ports = {serial.port for serial in serials}
    for port_name in active_ports:
        if port_name not in current_ports:
            print(f"Обнаружен новый COM-порт на устройстве {port_name}, пытаемся подключиться...")
            try:
                ser = Serial(port=port_name, baudrate=config.BAUDRATE, timeout=config.TIMEOUT)
            except Exception as e:
                print(f"Не удалось подключиться к COM-порту на устройстве {port_name}.")
                print("Детали ошибки:", e)
                print("")
            else:
                print(f"Новый COM-порт на устройстве {port_name} успешно подключен.")
                serials.append(ser)



async def main() -> None:
    pattern_station = re.compile(config.REGEX_STATION)
    pattern_card = re.compile(config.REGEX_CARD)

    ports = detect_com_ports(print_out=True)
    if len(ports) == 0:
        return

    serials = connect_com_ports(ports)
    if len(serials) == 0:
        return

    print("Scanning mode turned on.")
    last_update_time = time()
    while True:
        # updating list of com ports and connected serials
        if time() - last_update_time > 1:
            ports = detect_com_ports()
            update_serials(ports, serials)
            last_update_time = time()

        # reading data from existing serials
        for serial in serials:
            try:
                data = serial.read(config.READ_BYTES).decode("utf-8", "ignore").strip()
            except SerialException as e:
                print(f"Ошибка работы с COM-портом на устройстве {serial.port}: {e}")

                # if there is a error related to reading from serial, count errors, when it's >3, stop reading from com port
                if error_counter.get(serial.port, None) is None:
                    error_counter[serial.port] = 0
                error_counter[serial.port] += 1
                if error_counter[serial.port] > 3:
                    print(f"Устройство {serial.port} было отключено, т.к. выдало ошибку чтения более 3 раз.")
                    print("")
                    error_counter.pop(serial.port, None)
                    station_ids.pop(serial.port, None)
                    serials.remove(serial)
                    continue

                print("Если такая ошибка возникнет более 3 раз, программа перестанет взаимодействовать с ним.")
                print("")
            except Exception as e:
                print(f"Не удалось прочитать данные с устройства {serial.port}. Ошибка: {e}")
                print("")
            else:
                debug(serial.port, data)

                station_match = pattern_station.search(data)
                card_match = pattern_card.search(data)
                if station_match is not None:
                    update_station_id(serial.port, int(station_match.group(1)))
                elif card_match is not None:
                    await process_card_id(serial.port, int(card_match.group(1)))


if __name__ == "__main__":
    asyncio.run(main())