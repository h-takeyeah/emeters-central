"""
Receive data on notification until device disconnects

https://github.com/hbldh/bleak/discussions/658
https://github.com/hbldh/bleak/blob/7e9b00954baa1538a2d9098be336402ecb7534db/examples/disconnect_callback.py
"""
import asyncio
import logging
from bleak import BleakClient, BleakScanner

SERVICE_UUID = "0000ffe0-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
fmt = logging.Formatter("%(levelname)s:%(asctime)s:%(funcName)s:%(lineno)s:%(message)s")
shandler = logging.StreamHandler()
shandler.setFormatter(fmt)
logger.addHandler(shandler)
# fhandler = logging.FileHandler(filename="app.log", mode='a', encoding="utf8", delay=True)
# fhandler.setFormatter(fmt)
# logger.addHandler(fhandler)


def on_notify(sender: int, data: bytearray):
    logger.info(f"[{sender}] {data.hex(':')}")
    return


async def main(*, service_uuid: str, char_uuid: str):
    print("scanning device...")
    device = await BleakScanner.discover(service_uuids=[service_uuid])
    if not isinstance(device, list) or len(device) != 1:
        logger.error(f"no device found (service {service_uuid})")
        return

    assert isinstance(device[0].address, str)
    addr = device[0].address

    disconnected_event = asyncio.Event() # not thread-safe

    def on_disconnect(client: BleakClient):
        print("disconnected")
        disconnected_event.set()

    async with BleakClient(address_or_ble_device=addr, disconnected_callback=on_disconnect) as client:
        logger.info(f"connected to {client}")
        await client.start_notify(char_specifier=char_uuid, callback=on_notify)
        print("sleeping until device disconnects...")
        await disconnected_event.wait() # sleep until set() is called


if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG) # enable logging for other module as well
    asyncio.run(main(service_uuid=SERVICE_UUID, char_uuid=CHARACTERISTIC_UUID))
