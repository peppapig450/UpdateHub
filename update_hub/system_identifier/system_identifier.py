import platform
from typing import Self
from dataclasses import dataclass, field
import uuid
import os


@dataclass
class SystemInfo:
    ip_address: str = field(default_factory=str)
    os_platform: str = field(default_factory=platform.platform)
    os_version: str = field(default_factory=platform.version)
    system_architecture: str = field(default_factory=platform.machine)
    user_name: str = field(default_factory=os.getlogin)
    computer_name: str = field(default_factory=platform.node)
    system_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    mac_address: str = field(
        default_factory=lambda: ":".join(
            f"{(uuid.getnode() >> i) & 0xff:02x}" for i in range(0, 2 * 6, 8)
        )[::-1]
    )


# TODO: add properties here and a repr etc for proper data storage
class SystemIdentifier:
    def __new__(cls, *args, **kwargs) -> Self:
        system = platform.system()
        if cls is SystemIdentifier:
            if system == "Windows":
                return WindowsIdentifier(*args, **kwargs)
            elif system == "Darwin":
                return MacosIdentifier(*args, **kwargs)
            elif system == "Linux":
                return LinuxIdentifier(*args, **kwargs)

        return super().__new__(cls)

    def __init__(self):
        self.system_info = SystemInfo()

    def set_system_info(self):
        """Set the common system information."""
        self.system_info.os_platform = platform.system()
        self.system_info.os_version = platform.release()
        self.system_info.system_architecture = platform.machine()
        self.system_info.user_name = os.getlogin()
        self.system_info.computer_name = platform.node()
        self.system_info.system_id = str(uuid.uuid4())
        self.system_info.mac_address = ":".join(
            f"{(uuid.getnode() >> i) & 0xff:02x}" for i in range(0, 2 * 6, 8)
        )[::-1]
