# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from ..object import Object


class BoolFalse(Object):
    ID = 0xbc799737
    value = False

    @classmethod
    def read(cls, *args) -> bool:
        return cls.value

    def __new__(cls) -> bytes:
        return int.to_bytes(cls.ID, 4, "little")


class BoolTrue(BoolFalse):
    ID = 0x997275b5
    value = True


class Bool(Object):
    @classmethod
    def read(cls, b: BytesIO) -> bool:
        value = int.from_bytes(b.read(4), "little")

        return (
            True if value == BoolTrue.ID
            else False if value == BoolFalse.ID
            else None
        )

    def __new__(cls, value: bool) -> BoolTrue or BoolFalse:
        return BoolTrue() if value else BoolFalse()
