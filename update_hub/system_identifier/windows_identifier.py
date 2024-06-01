from .system_identifier import SystemIdentifier, SystemInfo
from dataclasses import dataclass, field
from collections import namedtuple
from typing import NamedTuple
import platform


class WindowsVersion(NamedTuple):
    major: int
    minor: int
    build: int


@dataclass
class WindowsInfo(SystemInfo):
    os_vesion: WindowsVersion = field(default_factory=lambda: WindowsVersion(0, 0, 0))
    ip_address: str = field(default_factory=str)
    windows_release: int = field(default_factory=int)


class WindowsIdentifier(SystemIdentifier):
    def __init__(self):
        super().__init__()
        self.system_info = WindowsInfo()
        self.set_system_info()

    def set_windows_info(self):
        """Set the Windows-specific system information."""
        pass

    def _get_windows_version(self) -> WindowsVersion:
        """Retrieve detailed Windows version information."""
        version_str = platform.version()
        major, minor, build = (int(part) for part in version_str.split("."))
        return WindowsVersion(major=major, minor=minor, build=build)
