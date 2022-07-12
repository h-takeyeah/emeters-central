import asyncio
import logging
from bleak import BleakClient, BleakScanner

SERVICE_UUID = "0000ffe0-0000-1000-8000-00805f9b34fb"
CHARACTERISTIC_UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(levelname)s:%(asctime)s:%(funcName)s:%(lineno)s:%(message)s"))
logger.addHandler(handler)


def on_notify(sender: int, data: bytearray):
    logger.info(f"[{sender}] {data.hex(':')}")
    return


async def main(*, service_uuid: str, char_uuid: str):
    logger.info("scanning device...")
    device = await BleakScanner.discover(service_uuids=[service_uuid])
    assert isinstance(device, list) and len(device) == 1, \
        f"no device found by this service UUID({service_uuid})"
    assert isinstance(device[0].address, str)

    addr = device[0].address
    async with BleakClient(address_or_ble_device=addr) as client:
        logger.info(f"connected to {client}")
        await client.start_notify(char_specifier=char_uuid, callback=on_notify)

        try:
            while True:
                await asyncio.sleep(2.0)
                pass
        except KeyboardInterrupt:
            await client.stop_notify(char_specifier=char_uuid)
            logger.info(f"connection end")
            return


#async def main():
#    async with BleakScanner(service_uuids=[UUID_SERVICE]) as scanner: # with filter
#    #async with BleakScanner() as scanner: # w/o filter
#        await asyncio.sleep(5.0)
#
#    for d in scanner.discovered_devices:
#        print(d.details)


#async def main():
#    """scan using filter"""
#    device = await BleakScanner.find_device_by_filter(
#        lambda d, ad: UUID_SERVICE in ad.service_uuids, 10.0
#    )
#    if device is None:
#        print("Not found")
#        return
#
#    print(device)


if __name__ == "__main__":
    #logging.basicConfig(level=logging.DEBUG) # enable logging for other module as well
    asyncio.run(main(service_uuid=SERVICE_UUID, char_uuid=CHARACTERISTIC_UUID))
