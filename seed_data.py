
from sqlalchemy.orm import Session
from models.ms import MSSwitch
from models.mx import MXAppliance
from models.mr import MRAccessPoint
from models.mv import MVCamera
from database import SessionLocal

def seed_data():
    db: Session = SessionLocal()

    # MS Switches
    ms_switches = [
        MSSwitch(model="MS130-48FP", use_case="Access", ports_1gbe=48, ports_mgig=0, uplinks=["1G"], poe_support="PoE+", stackable=False, routing="L2", catalyst=True, notes="Cloud-controlled Catalyst L2 switch"),
        MSSwitch(model="MS250-24P", use_case="Access", ports_1gbe=24, ports_mgig=0, uplinks=["10G"], poe_support="PoE+", stackable=True, routing="Dynamic", catalyst=False, notes="Popular access switch with stacking"),
        MSSwitch(model="MS390-24UX2", use_case="Access/Aggregation", ports_1gbe=24, ports_mgig=8, uplinks=["10G", "40G"], poe_support="UPOE", stackable=True, routing="Dynamic", catalyst=True, notes="Multigig Catalyst with high power"),
    ]

    # MX Appliances
    mx_appliances = [
        MXAppliance(model="MX67", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["1x GbE RJ45"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX67C", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["1x GbE RJ45", "Cat 6 LTE"], has_wireless=False, has_cellular=True),
        MXAppliance(model="MX68", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["2x GbE RJ45"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX68CW", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["2x GbE RJ45", "Cat 6 LTE"], has_wireless=True, has_cellular=True),
    ]

    # MR Access Points
    mr_access_points = [
        MRAccessPoint(model="MR36", wifi_standard="Wi-Fi 6", radios=2, antenna_type="Internal", poe=True, notes="Mid-range AP for general deployments"),
        MRAccessPoint(model="MR46", wifi_standard="Wi-Fi 6", radios=3, antenna_type="Internal", poe=True, notes="High-performance AP with additional scanning radio"),
    ]

    # MV Cameras
    mv_cameras = [
        MVCamera(model="MV2", use_case="Indoor compact", resolution="1080p", onboard_storage=True, wireless=True, notes="Flexible camera with wireless and USB-C"),
        MVCamera(model="MV33", use_case="Indoor wide-angle", resolution="4MP", onboard_storage=True, wireless=True, notes="360° indoor dome with analytics"),
        MVCamera(model="MV52", use_case="Outdoor telephoto", resolution="4K", onboard_storage=True, wireless=False, notes="Outdoor long-range with optical zoom"),
    ]

    db.add_all(ms_switches + mx_appliances + mr_access_points + mv_cameras)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_data()
