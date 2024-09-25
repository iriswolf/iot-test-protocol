from typing import Optional

from struc2 import Struct, Tag, LittleEndian, DTR
from struc2.SerializedImpl import u8, u32, f32


class Data(Struct):

    def get_code_msg_dtr(self):
        return ['u8'] if self.type_message == 2 else None

    num_pack: Tag[int, u8]
    type_message: Tag[int, u8]
    imei: Tag[bytes, 15, 'cstring']
    datetime: Tag[int, LittleEndian, u32]
    lat: Tag[float, LittleEndian, f32]
    lon: Tag[float, LittleEndian, f32]
    code_msg: Tag[Optional[int], DTR[get_code_msg_dtr]]  # This appears when type_message == 2
