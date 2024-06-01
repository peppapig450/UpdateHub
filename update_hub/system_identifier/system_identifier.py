import platform
from typing import Self


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
        self.os_name = platform.system()
        self.os_version = platform.system()

    def identify_os(self):
        """Identify the operating system."""
        return self.os_name

    def identify_os_version(self):
        """Identify the operating system version."""
        return self.os_version
