import pytest

from src.test_protocol import TestProtocol


class TestProtocolParsing:
    @pytest.mark.parametrize(
        "data,result",
        [
            (
                b'\x00\x01869586748696585\xfa\x12\xedfc.VB\xaa`EB',
                {
                    'num_pack': 0,
                    'type_message': 1,
                    'imei': '869586748696585',
                    'datetime': 1726812922,
                    'lat': 53.5452995300293,
                    'lon': 49.344398498535156
                }
            ),
            (
                b'\x01\x01869586748696585\t\x15\xedf\x1b/VBB`EB',
                {
                    'num_pack': 1,
                    'type_message': 1,
                    'imei': '869586748696585',
                    'datetime': 1726813449,
                    'lat': 53.54600143432617,
                    'lon': 49.34400177001953
                }
            ),
            (
                b'\x02\x02869586748696585+\x15\xedf\x9e/VB\xbe_EB\x03',
                {
                    'num_pack': 2,
                    'type_message': 2,
                    'imei': '869586748696585',
                    'datetime': 1726813483,
                    'lat': 53.54650115966797,
                    'lon': 49.34349822998047,
                    'code_msg': 3
                }
            )
        ]
    )
    def test_protocol_parsing(self, data: bytes, result: dict):
        parsed_data = TestProtocol.parse(data)
        assert parsed_data == result
