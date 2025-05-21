
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

    mx_appliances = [
        MXAppliance(model="MX67", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["1x GbE RJ45"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX67C", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["1x GbE RJ45", "Cat 6 LTE"], has_wireless=False, has_cellular=True),
        MXAppliance(model="MX67W", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["1x GbE RJ45"], has_wireless=True, has_cellular=False),
        MXAppliance(model="MX68", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["2x GbE RJ45"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX68CW", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["2x GbE RJ45", "Cat 6 LTE"], has_wireless=True, has_cellular=True),
        MXAppliance(model="MX68W", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["2x GbE RJ45"], has_wireless=True, has_cellular=False),
        MXAppliance(model="MX75", use_case="Medium branch", throughput_mbps=1000, max_users=200, uplink_ports=["2x GbE RJ45", "1x GbE SFP"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX85", use_case="Medium branch", throughput_mbps=1000, max_users=200, uplink_ports=["2x GbE RJ45", "2x SFP"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX95", use_case="Large branch", throughput_mbps=2000, max_users=500, uplink_ports=["2x 10 GbE SFP+"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX105", use_case="Large branch", throughput_mbps=5000, max_users=750, uplink_ports=["2x 10 GbE SFP+", "2x 2.5GbE RJ45"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX250", use_case="Campus or VPN concentrator", throughput_mbps=7500, max_users=2000, uplink_ports=["8x GbE RJ45", "8x GbE SFP", "8x 10 GbE SFP+"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX450", use_case="Campus or VPN concentrator", throughput_mbps=10000, max_users=10000, uplink_ports=["8x GbE RJ45", "8x GbE SFP", "8x 10 GbE SFP+"], has_wireless=False, has_cellular=False),
        MXAppliance(model="vMX Small", use_case="Cloud VPN", throughput_mbps=500, max_users=100, uplink_ports=["Virtual"], has_wireless=False, has_cellular=False),
        MXAppliance(model="vMX Medium", use_case="Cloud VPN", throughput_mbps=1000, max_users=250, uplink_ports=["Virtual"], has_wireless=False, has_cellular=False),
        MXAppliance(model="vMX Large", use_case="Cloud VPN", throughput_mbps=1500, max_users=500, uplink_ports=["Virtual"], has_wireless=False, has_cellular=False),
    ]

    # MR Access Points
    mr_access_points = [
        MRAccessPoint(model="MR36", wifi_standard="Wi-Fi 6", radios=2, antenna_type="Internal", poe=True, catalyst=False, notes="Mid-range AP for general deployments"),
        MRAccessPoint(model="MR36H", wifi_standard="Wi-Fi 6", radios=2, antenna_type="Internal", poe=True, catalyst=False, notes="Wall-mounted AP for hospitality and dorms"),
        MRAccessPoint(model="MR44", wifi_standard="Wi-Fi 6", radios=2, antenna_type="Internal", poe=True, catalyst=False, notes="Balanced performance and affordability"),
        MRAccessPoint(model="MR46", wifi_standard="Wi-Fi 6", radios=3, antenna_type="Internal", poe=True, catalyst=False, notes="High-performance AP with scanning radio"),
        MRAccessPoint(model="MR46E", wifi_standard="Wi-Fi 6", radios=3, antenna_type="External", poe=True, catalyst=False, notes="High-performance with external antenna support"),
        MRAccessPoint(model="MR55", wifi_standard="Wi-Fi 6", radios=3, antenna_type="Internal", poe=True, catalyst=False, notes="Ultra-high performance with 5 Gbps uplink"),
        MRAccessPoint(model="MR70", wifi_standard="Wi-Fi 5", radios=2, antenna_type="Internal", poe=True, catalyst=False, notes="Entry-level outdoor AP"),
        MRAccessPoint(model="MR76", wifi_standard="Wi-Fi 6", radios=2, antenna_type="External", poe=True, catalyst=False, notes="Rugged outdoor AP with external antennas"),
        MRAccessPoint(model="MR86", wifi_standard="Wi-Fi 6", radios=2, antenna_type="External", poe=True, catalyst=False, notes="Outdoor AP for high-density deployments"),

        # Catalyst Cloud-Controlled
        MRAccessPoint(model="CW9162", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="6 GHz Catalyst with tri-radio"),
        MRAccessPoint(model="CW9164", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Higher throughput Catalyst AP"),
        MRAccessPoint(model="CW9166", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Flagship Catalyst AP"),
        MRAccessPoint(model="CW9204", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Next-gen Catalyst AP"),
        MRAccessPoint(model="CW9206", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Compact 6E Catalyst AP"),
        MRAccessPoint(model="CW9224", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Advanced security and mesh"),
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
