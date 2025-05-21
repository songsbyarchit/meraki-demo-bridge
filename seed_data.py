
from sqlalchemy.orm import Session
from models.ms import MSSwitch
from models.mx import MXAppliance
from models.mr import MRAccessPoint
from models.mv import MVCamera
from database import SessionLocal

def seed_data():
    db: Session = SessionLocal()

    ms_switches = [
        # MS120 Series
        MSSwitch(model="MS120-8LP-HW", use_case="Compact", ports_1gbe=8, ports_mgig=0, uplinks=["2x 1G SFP"], poe_support="PoE", stackable=False, routing="DHCP relay", catalyst=False, notes="Compact PoE access switch"),
        MSSwitch(model="MS120-8FP-HW", use_case="Compact", ports_1gbe=8, ports_mgig=0, uplinks=["2x 1G SFP"], poe_support="PoE+", stackable=False, routing="DHCP relay", catalyst=False, notes="Compact PoE+ access switch"),
        MSSwitch(model="MS120-24P-HW", use_case="Branch", ports_1gbe=24, ports_mgig=0, uplinks=["4x 1G SFP"], poe_support="PoE+", stackable=False, routing="DHCP relay", catalyst=False, notes="Standard 24-port access switch"),
        MSSwitch(model="MS120-48FP-HW", use_case="Branch", ports_1gbe=48, ports_mgig=0, uplinks=["4x 1G SFP"], poe_support="PoE+", stackable=False, routing="DHCP relay", catalyst=False, notes="High-power 48-port access switch"),

        # MS130 Series
        MSSwitch(model="MS130-8X-HW", use_case="Compact", ports_1gbe=6, ports_mgig=2, uplinks=["2x 10G SFP+"], poe_support="PoE+", stackable=False, routing="DHCP relay", catalyst=False, notes="mGig compact access switch"),
        MSSwitch(model="MS130-24X-HW", use_case="Branch", ports_1gbe=18, ports_mgig=6, uplinks=["4x 10G SFP+"], poe_support="PoE+", stackable=False, routing="DHCP relay", catalyst=False, notes="24-port mGig access switch"),
        MSSwitch(model="MS130-48X-HW", use_case="Branch", ports_1gbe=40, ports_mgig=8, uplinks=["4x 10G SFP+"], poe_support="PoE+", stackable=False, routing="DHCP relay", catalyst=False, notes="48-port mGig access switch"),

        # MS210/MS225/MS250
        MSSwitch(model="MS210-24P-HW", use_case="Branch", ports_1gbe=24, ports_mgig=0, uplinks=["4x 1G SFP"], poe_support="PoE+", stackable=True, routing="DHCP relay", catalyst=False, notes="Stackable 24-port L2 switch"),
        MSSwitch(model="MS225-48LP-HW", use_case="Branch", ports_1gbe=48, ports_mgig=0, uplinks=["4x 10G SFP+"], poe_support="PoE", stackable=True, routing="DHCP relay", catalyst=False, notes="Stackable L2 switch"),
        MSSwitch(model="MS250-48FP-HW", use_case="Branch", ports_1gbe=48, ports_mgig=0, uplinks=["4x 10G SFP+"], poe_support="PoE+", stackable=True, routing="Dynamic", catalyst=False, notes="Layer 3 PoE+ switch"),

        # MS350/MS355/MS390
        MSSwitch(model="MS355-24X2-HW", use_case="Campus", ports_1gbe=8, ports_mgig=16, uplinks=["4x 10G SFP+"], poe_support="UPOE", stackable=True, routing="Dynamic", catalyst=False, notes="High-performance multigig switch"),
        MSSwitch(model="MS390-48UX2-HW", use_case="Campus", ports_1gbe=0, ports_mgig=48, uplinks=["8x 10G SFP+", "2x 40G QSFP+"], poe_support="UPOE+", stackable=True, routing="Dynamic", catalyst=False, notes="Flagship multigig stackable switch"),

        # MS410/MS425/MS450
        MSSwitch(model="MS410-16-HW", use_case="Aggregation", ports_1gbe=0, ports_mgig=0, uplinks=["2x 10G SFP+"], poe_support="None", stackable=True, routing="Dynamic", catalyst=False, notes="16-port 1G SFP aggregation"),
        MSSwitch(model="MS425-32-HW", use_case="Aggregation", ports_1gbe=0, ports_mgig=0, uplinks=["2x 100G QSFP28"], poe_support="None", stackable=True, routing="Dynamic", catalyst=False, notes="32-port 10G aggregation switch"),

        # Catalyst 9300-M series (Meraki-managed)
        MSSwitch(model="C9300-48UXM-M", use_case="Secure Wi-Fi 6/7", ports_1gbe=0, ports_mgig=48, uplinks=["2x 40G QSFP", "8x 10G SFP+"], poe_support="UPOE", stackable=True, routing="Dynamic", catalyst=True, notes="Catalyst mGig switch for Wi-Fi 7"),
    ]

    mx_appliances = [
        # Small branch models
        MXAppliance(model="MX67", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["1x GbE RJ45"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX67W", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["1x GbE RJ45"], has_wireless=True, has_cellular=False),
        MXAppliance(model="MX67C", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["1x GbE RJ45", "Cat 6 LTE"], has_wireless=False, has_cellular=True),

        # Small branch with more ports / PoE
        MXAppliance(model="MX68", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["2x GbE RJ45"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX68W", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["2x GbE RJ45"], has_wireless=True, has_cellular=False),
        MXAppliance(model="MX68CW", use_case="Small branch", throughput_mbps=700, max_users=50, uplink_ports=["2x GbE RJ45", "Cat 6 LTE"], has_wireless=True, has_cellular=True),

        # Medium branch
        MXAppliance(model="MX75", use_case="Medium branch", throughput_mbps=1000, max_users=200, uplink_ports=["2x GbE RJ45", "1x GbE SFP"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX85", use_case="Medium branch", throughput_mbps=1000, max_users=200, uplink_ports=["2x GbE RJ45", "2x SFP"], has_wireless=False, has_cellular=False),

        # Large branch
        MXAppliance(model="MX95", use_case="Large branch", throughput_mbps=2500, max_users=500, uplink_ports=["2x 10 GbE SFP+"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX105", use_case="Large branch", throughput_mbps=5000, max_users=750, uplink_ports=["2x 10 GbE SFP+", "2x 2.5 GbE RJ45"], has_wireless=False, has_cellular=False),

        # Campus / VPN Concentrators
        MXAppliance(model="MX250", use_case="Campus or VPN concentrator", throughput_mbps=7500, max_users=2000, uplink_ports=["8x GbE RJ45", "8x GbE SFP", "8x 10 GbE SFP+"], has_wireless=False, has_cellular=False),
        MXAppliance(model="MX450", use_case="Campus or VPN concentrator", throughput_mbps=10000, max_users=10000, uplink_ports=["8x GbE RJ45", "8x GbE SFP", "8x 10 GbE SFP+"], has_wireless=False, has_cellular=False),

        # Virtual MX
        MXAppliance(model="vMX Small", use_case="Cloud VPN", throughput_mbps=250, max_users=50, uplink_ports=["Virtual"], has_wireless=False, has_cellular=False),
        MXAppliance(model="vMX Medium", use_case="Cloud VPN", throughput_mbps=500, max_users=250, uplink_ports=["Virtual"], has_wireless=False, has_cellular=False),
        MXAppliance(model="vMX Large", use_case="Cloud VPN", throughput_mbps=1000, max_users=1000, uplink_ports=["Virtual"], has_wireless=False, has_cellular=False),
    ]

    # MR Access Points
    mr_access_points = [
        # Wi-Fi 6
        MRAccessPoint(model="MR28", wifi_standard="Wi-Fi 6", radios=2, antenna_type="Internal", poe=True, catalyst=False, notes="Entry-level indoor AP"),
        MRAccessPoint(model="MR36", wifi_standard="Wi-Fi 6", radios=2, antenna_type="Internal", poe=True, catalyst=False, notes="Mid-range AP for general deployments"),
        MRAccessPoint(model="MR36H", wifi_standard="Wi-Fi 6", radios=2, antenna_type="Internal", poe=True, catalyst=False, notes="Wall-mounted AP for hospitality"),
        MRAccessPoint(model="MR44", wifi_standard="Wi-Fi 6", radios=2, antenna_type="Internal", poe=True, catalyst=False, notes="Balanced indoor AP"),
        MRAccessPoint(model="MR46", wifi_standard="Wi-Fi 6", radios=3, antenna_type="Internal", poe=True, catalyst=False, notes="High-performance indoor AP"),
        MRAccessPoint(model="MR46E", wifi_standard="Wi-Fi 6", radios=3, antenna_type="External", poe=True, catalyst=False, notes="High-performance AP with external antennas"),
        MRAccessPoint(model="MR55", wifi_standard="Wi-Fi 6", radios=3, antenna_type="Internal", poe=True, catalyst=False, notes="Ultra-high performance with 5 Gbps uplink"),
        MRAccessPoint(model="MR56", wifi_standard="Wi-Fi 6", radios=3, antenna_type="Internal", poe=True, catalyst=False, notes="Indoor AP with high-density support"),
        MRAccessPoint(model="MR70", wifi_standard="Wi-Fi 5", radios=2, antenna_type="Internal", poe=True, catalyst=False, notes="Rugged outdoor entry-level AP"),
        MRAccessPoint(model="MR76", wifi_standard="Wi-Fi 6", radios=2, antenna_type="External", poe=True, catalyst=False, notes="Outdoor AP with external antennas"),
        MRAccessPoint(model="MR78", wifi_standard="Wi-Fi 6", radios=2, antenna_type="Internal", poe=True, catalyst=False, notes="Cost-effective outdoor AP"),
        MRAccessPoint(model="MR86", wifi_standard="Wi-Fi 6", radios=2, antenna_type="External", poe=True, catalyst=False, notes="Outdoor high-density AP"),

        # Wi-Fi 6E (Catalyst)
        MRAccessPoint(model="MR57", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="Internal", poe=True, catalyst=False, notes="Wi-Fi 6E indoor AP"),
        MRAccessPoint(model="CW9162", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Entry-level Catalyst AP"),
        MRAccessPoint(model="CW9163E", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="External", poe=True, catalyst=True, notes="External-antenna Catalyst AP"),
        MRAccessPoint(model="CW9164", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Higher-throughput Catalyst AP"),
        MRAccessPoint(model="CW9166", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Flagship Catalyst indoor AP"),
        MRAccessPoint(model="CW9166D1", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Low-profile Catalyst AP"),

        # Wi-Fi 7 (Catalyst)
        MRAccessPoint(model="CW9172H", wifi_standard="Wi-Fi 7", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Wall-mount Catalyst AP with Wi-Fi 7"),
        MRAccessPoint(model="CW9172I", wifi_standard="Wi-Fi 7", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Indoor Catalyst AP with Wi-Fi 7"),
        MRAccessPoint(model="CW9176I", wifi_standard="Wi-Fi 7", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="High-performance Catalyst with multigig uplinks"),
        MRAccessPoint(model="CW9176D1", wifi_standard="Wi-Fi 7", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Slim-profile Wi-Fi 7 Catalyst AP"),
        MRAccessPoint(model="CW9178I", wifi_standard="Wi-Fi 7", radios=3, antenna_type="Internal", poe=True, catalyst=True, notes="Advanced Catalyst AP with 2x 10G uplinks"),
    ]

        # MV Cameras
    mv_cameras = [
        # Indoor
        MVCamera(model="MV2-HW", use_case="Indoor compact", resolution="4MP", onboard_storage=False, wireless=True, notes="Wide angle flex camera (Cloud Archive only)"),
        MVCamera(model="MV12WE-HW", use_case="Indoor mini dome", resolution="1080p", onboard_storage=True, wireless=False, notes="128GB onboard storage"),
        MVCamera(model="MV12W-HW", use_case="Indoor mini dome", resolution="1080p", onboard_storage=True, wireless=False, notes="256GB onboard storage"),
        MVCamera(model="MV12N-HW", use_case="Indoor narrow dome", resolution="1080p", onboard_storage=True, wireless=False, notes="256GB narrow FoV dome"),
        MVCamera(model="MV13-HW", use_case="Indoor fixed dome", resolution="4K", onboard_storage=True, wireless=False, notes="256GB storage, 103° FoV"),
        MVCamera(model="MV13M-HW", use_case="Indoor fixed dome", resolution="4K", onboard_storage=True, wireless=False, notes="512GB storage"),
        MVCamera(model="MV22-HW", use_case="Indoor varifocal dome", resolution="4MP", onboard_storage=True, wireless=False, notes="256GB storage, varifocal"),
        MVCamera(model="MV22X-HW", use_case="Indoor varifocal dome", resolution="4MP", onboard_storage=True, wireless=False, notes="512GB storage"),
        MVCamera(model="MV23M-HW", use_case="Indoor varifocal dome", resolution="4K", onboard_storage=True, wireless=False, notes="512GB storage"),
        MVCamera(model="MV23X-HW", use_case="Indoor varifocal dome", resolution="4K", onboard_storage=True, wireless=False, notes="1TB storage"),
        MVCamera(model="MV32-HW", use_case="Indoor fisheye", resolution="4.2MP", onboard_storage=True, wireless=False, notes="360° view"),
        MVCamera(model="MV33-HW", use_case="Indoor fisheye", resolution="8MP", onboard_storage=True, wireless=False, notes="360° view, 256GB storage"),
        MVCamera(model="MV33M-HW", use_case="Indoor fisheye", resolution="8MP", onboard_storage=True, wireless=False, notes="360° view, 512GB storage"),

        # Outdoor
        MVCamera(model="MV52-HW", use_case="Outdoor telephoto bullet", resolution="4K", onboard_storage=True, wireless=False, notes="1TB storage, 12–37° FoV"),
        MVCamera(model="MV53X", use_case="Outdoor telephoto bullet", resolution="4K", onboard_storage=True, wireless=False, notes="1TB storage"),
        MVCamera(model="MV63-HW", use_case="Outdoor fixed dome", resolution="4K", onboard_storage=True, wireless=False, notes="256GB storage"),
        MVCamera(model="MV63M-HW", use_case="Outdoor fixed dome", resolution="4K", onboard_storage=True, wireless=False, notes="512GB storage"),
        MVCamera(model="MV63X-HW", use_case="Outdoor fixed dome", resolution="4K", onboard_storage=True, wireless=False, notes="1TB storage"),
        MVCamera(model="MV72-HW", use_case="Outdoor dome", resolution="4MP", onboard_storage=True, wireless=False, notes="256GB storage"),
        MVCamera(model="MV72X-HW", use_case="Outdoor dome", resolution="4MP", onboard_storage=True, wireless=False, notes="512GB storage"),
        MVCamera(model="MV73M-HW", use_case="Outdoor varifocal dome", resolution="4K", onboard_storage=True, wireless=False, notes="512GB storage"),
        MVCamera(model="MV73X-HW", use_case="Outdoor varifocal dome", resolution="4K", onboard_storage=True, wireless=False, notes="1TB storage"),
        MVCamera(model="MV84X", use_case="Outdoor multi-imager", resolution="4x5MP", onboard_storage=True, wireless=False, notes="4x imagers, 4TB total storage"),
        MVCamera(model="MV93-HW", use_case="Outdoor fisheye", resolution="8MP", onboard_storage=True, wireless=False, notes="256GB storage, 360° FoV"),
        MVCamera(model="MV93M-HW", use_case="Outdoor fisheye", resolution="8MP", onboard_storage=True, wireless=False, notes="512GB storage, 360° FoV"),
        MVCamera(model="MV93X-HW", use_case="Outdoor fisheye", resolution="8MP", onboard_storage=True, wireless=False, notes="1TB storage, 360° FoV"),
    ]

    db.add_all(ms_switches + mx_appliances + mr_access_points + mv_cameras)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_data()
