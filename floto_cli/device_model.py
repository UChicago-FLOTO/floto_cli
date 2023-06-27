from dataclasses import dataclass
import datetime
import uuid

import rich.table


@dataclass
class Device:
    created_at: datetime.datetime
    modified_at: datetime.datetime
    id: int
    actor: int
    api_heartbeat_state: str
    uuid: uuid.UUID
    local_id: None
    device_name: str
    note: None
    is_of__device_type: {}
    belongs_to__application: {}
    is_online: bool
    last_connectivity_event: datetime.datetime
    is_connected_to_vpn: bool
    last_vpn_event: datetime.datetime
    is_locked_until__date: None
    logs_channel: None
    public_address: None
    vpn_address: None
    ip_address: str
    mac_address: str
    memory_usage: 559
    memory_total: int
    storage_block_device: str
    storage_usage: int
    storage_total: int
    cpu_usage: int
    cpu_temp: int
    is_undervolted: bool
    cpu_id: int
    is_running__release: {}
    download_progress: None
    status: str
    os_version: str
    os_variant: str
    supervisor_version: str
    provisioning_progress: None
    provisioning_state: str
    api_port: int
    api_secret: str
    is_managed_by__service_instance: {}
    should_be_running__release: {}
    should_be_operated_by__release: None
    is_managed_by__device: None
    should_be_managed_by__release: None
    is_web_accessible: bool
    overall_status: str
    overall_progress: None

    def make_row(self) -> ():
        print((str(self.id), str(self.device_name), str(self.api_heartbeat_state), str(self.is_online), str(self.uuid), str(self.is_of__device_type), str(self.status)))
        return (str(self.id), str(self.device_name), str(self.api_heartbeat_state), str(self.is_online), str(self.uuid), str(self.is_of__device_type), str(self.status))


def make_devices_table() -> rich.table.Table:
    table = rich.table.Table(title="Devices")
    table.add_column("Id")
    table.add_column("Device Name")
    table.add_column("HeartBeat")
    table.add_column("Is Online")
    table.add_column("UUID")
    table.add_column("Device Type")
    table.add_column("Status")
    return table
