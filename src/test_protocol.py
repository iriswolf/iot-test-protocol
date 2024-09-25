from typing import Any

from src.structures import Data


class TestProtocol:

    @staticmethod
    def parse(data: bytes) -> dict[str, Any]:
        parsed_data = Data.unpack_b(data)

        output = dict(
            num_pack = parsed_data.num_pack,
            type_message = parsed_data.type_message,
            imei = parsed_data.imei.decode('utf-8'),
            datetime = parsed_data.datetime,
            lat = parsed_data.lat,
            lon = parsed_data.lon
        )

        if parsed_data.code_msg is not None:
            output['code_msg'] = parsed_data.code_msg

        return output
