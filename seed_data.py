
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
        MSSwitch(model="MS120-8LP-HW", use_case="compact", ports_1gbe=8, ports_mgig=0, uplinks="2x 1G SFP", poe_support="PoE", stackable=False, routing="dhcp relay", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS120_Overview_and_Specifications"),
        MSSwitch(model="MS120-8FP-HW", use_case="compact", ports_1gbe=8, ports_mgig=0, uplinks="2x 1G SFP", poe_support="PoE+", stackable=False, routing="dhcp relay", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS120_Overview_and_Specifications"),
        MSSwitch(model="MS120-24P-HW", use_case="branch", ports_1gbe=24, ports_mgig=0, uplinks="4x 1G SFP", poe_support="PoE+", stackable=False, routing="dhcp relay", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS120_Overview_and_Specifications"),
        MSSwitch(model="MS120-48FP-HW", use_case="branch", ports_1gbe=48, ports_mgig=0, uplinks="4x 1G SFP", poe_support="PoE+", stackable=False, routing="dhcp relay", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS120_Overview_and_Specifications"),

        # MS130 Series
        MSSwitch(model="MS130-8X-HW", use_case="compact", ports_1gbe=6, ports_mgig=2, uplinks="2x 10G SFP+", poe_support="PoE+", stackable=False, routing="dhcp relay", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS130_Datasheet"),
        MSSwitch(model="MS130-24X-HW", use_case="branch", ports_1gbe=18, ports_mgig=6, uplinks="4x 10G SFP+", poe_support="PoE+", stackable=False, routing="dhcp relay", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS130_Datasheet"),
        MSSwitch(model="MS130-48X-HW", use_case="branch", ports_1gbe=40, ports_mgig=8, uplinks="4x 10G SFP+", poe_support="PoE+", stackable=False, routing="dhcp relay", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS130_Datasheet"),

        # MS210/MS225/MS250
        MSSwitch(model="MS210-24P-HW", use_case="branch", ports_1gbe=24, ports_mgig=0, uplinks="4x 1G SFP", poe_support="PoE+", stackable=True, routing="dhcp relay", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS210_Overview_and_Specifications"),
        MSSwitch(model="MS225-48LP-HW", use_case="branch", ports_1gbe=48, ports_mgig=0, uplinks="4x 10G SFP+", poe_support="PoE", stackable=True, routing="dhcp relay", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS225_Overview_and_Specifications"),
        MSSwitch(model="MS250-48FP-HW", use_case="branch", ports_1gbe=48, ports_mgig=0, uplinks="4x 10G SFP+", poe_support="PoE+", stackable=True, routing="dynamic", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS250_Overview_and_Specifications"),

        # MS350/MS355/MS390
        MSSwitch(model="MS355-24X2-HW", use_case="campus", ports_1gbe=8, ports_mgig=16, uplinks="4x 10G SFP+", poe_support="UPOE", stackable=True, routing="dynamic", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS355_Overview_and_Specifications"),
        MSSwitch(model="MS390-48UX2-HW", use_case="campus", ports_1gbe=0, ports_mgig=48, uplinks="8x 10G SFP+, 2x 40G QSFP+", poe_support="UPOE+", stackable=True, routing="dynamic", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS390_Datasheet"),

        # MS410/MS425/MS450
        MSSwitch(model="MS410-16-HW", use_case="aggregation", ports_1gbe=0, ports_mgig=0, uplinks="2x 10G SFP+", poe_support="none", stackable=True, routing="dynamic", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS410_Overview_and_Specifications"),
        MSSwitch(model="MS425-32-HW", use_case="aggregation", ports_1gbe=0, ports_mgig=0, uplinks="2x 100G QSFP28", poe_support="none", stackable=True, routing="dynamic", catalyst=False, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/MS425_Overview_and_Specifications"),

        # Catalyst 9300 Series (Meraki-managed)
        # Catalyst 9300 Series (Meraki-managed)
        # C9300-M (1G RJ45)
        MSSwitch(model="C9300-24T-M", use_case="secure wi-fi 6/7", ports_1gbe=24, ports_mgig=0, uplinks="4x 1G/10G SFP/SFP+", poe_support="none", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300-M_Datasheet"),
        MSSwitch(model="C9300-24P-M", use_case="secure wi-fi 6/7", ports_1gbe=24, ports_mgig=0, uplinks="4x 1G/10G SFP/SFP+", poe_support="PoE+", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300-M_Datasheet"),
        MSSwitch(model="C9300-24U-M", use_case="secure wi-fi 6/7", ports_1gbe=24, ports_mgig=0, uplinks="4x 1G/10G SFP/SFP+", poe_support="UPOE", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300-M_Datasheet"),
        MSSwitch(model="C9300-48T-M", use_case="secure wi-fi 6/7", ports_1gbe=48, ports_mgig=0, uplinks="4x 1G/10G SFP/SFP+", poe_support="none", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300-M_Datasheet"),
        MSSwitch(model="C9300-48P-M", use_case="secure wi-fi 6/7", ports_1gbe=48, ports_mgig=0, uplinks="4x 1G/10G SFP/SFP+", poe_support="PoE+", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300-M_Datasheet"),
        MSSwitch(model="C9300-48U-M", use_case="secure wi-fi 6/7", ports_1gbe=48, ports_mgig=0, uplinks="4x 1G/10G SFP/SFP+", poe_support="UPOE", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300-M_Datasheet"),

        # C9300L-M (1G RJ45)
        MSSwitch(model="C9300L-24T-4X-M", use_case="secure wi-fi 6/7", ports_1gbe=24, ports_mgig=0, uplinks="4x 10G SFP+", poe_support="none", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300L-M_Datasheet"),
        MSSwitch(model="C9300L-24P-4X-M", use_case="secure wi-fi 6/7", ports_1gbe=24, ports_mgig=0, uplinks="4x 10G SFP+", poe_support="PoE+", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300L-M_Datasheet"),
        MSSwitch(model="C9300L-48T-4X-M", use_case="secure wi-fi 6/7", ports_1gbe=48, ports_mgig=0, uplinks="4x 10G SFP+", poe_support="none", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300L-M_Datasheet"),
        MSSwitch(model="C9300L-48P-4X-M", use_case="secure wi-fi 6/7", ports_1gbe=48, ports_mgig=0, uplinks="4x 10G SFP+", poe_support="PoE+", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300L-M_Datasheet"),
        MSSwitch(model="C9300L-48PF-4X-M", use_case="secure wi-fi 6/7", ports_1gbe=48, ports_mgig=0, uplinks="4x 10G SFP+", poe_support="UPOE", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300L-M_Datasheet"),

        # C9300-M (multigig)
        MSSwitch(model="C9300-24UX-M", use_case="secure wi-fi 7", ports_1gbe=0, ports_mgig=24, uplinks="4x 10G SFP+", poe_support="UPOE", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300-M_Datasheet"),
        MSSwitch(model="C9300-48UXM-M", use_case="secure wi-fi 7", ports_1gbe=0, ports_mgig=48, uplinks="8x 10G SFP+, 2x 40G QSFP", poe_support="UPOE", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300-M_Datasheet"),
        MSSwitch(model="C9300-48UN-M", use_case="secure wi-fi 7", ports_1gbe=0, ports_mgig=48, uplinks="8x 10G SFP+, 2x 40G QSFP", poe_support="UPOE+", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300-M_Datasheet"),

        # C9300L-M (multigig)
        MSSwitch(model="C9300L-24UXG-4X-M", use_case="secure wi-fi 7", ports_1gbe=0, ports_mgig=24, uplinks="4x 10G SFP+", poe_support="UPOE", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300L-M_Datasheet"),
        MSSwitch(model="C9300L-48UXG-4X-M", use_case="secure wi-fi 7", ports_1gbe=0, ports_mgig=48, uplinks="4x 10G SFP+", poe_support="UPOE", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300L-M_Datasheet"),

        # C9300X-M (multigig)
        MSSwitch(model="C9300X-24HX-M", use_case="secure wi-fi 7", ports_1gbe=0, ports_mgig=24, uplinks="8x 10/25G SFP28, 2x 40G/100G QSFP28", poe_support="UPOE+", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300X-M_Datasheet"),
        MSSwitch(model="C9300X-48HX-M", use_case="secure wi-fi 7", ports_1gbe=0, ports_mgig=48, uplinks="8x 10/25G SFP28, 2x 40G/100G QSFP28", poe_support="UPOE+", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300X-M_Datasheet"),
        MSSwitch(model="C9300X-48HXN-M", use_case="secure wi-fi 7", ports_1gbe=0, ports_mgig=48, uplinks="8x 10/25G SFP28, 2x 40G/100G QSFP28", poe_support="UPOE+", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300X-M_Datasheet"),

        # C9300-M (fiber)
        MSSwitch(model="C9300-24S-M", use_case="aggregation", ports_1gbe=0, ports_mgig=0, uplinks="8x 10G SFP+, 2x 40G QSFP", poe_support="none", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300-M_Datasheet"),
        MSSwitch(model="C9300-48S-M", use_case="aggregation", ports_1gbe=0, ports_mgig=0, uplinks="8x 10G SFP+, 2x 40G QSFP", poe_support="none", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300-M_Datasheet"),

        # C9300X-M (fiber)
        MSSwitch(model="C9300X-12Y-M", use_case="aggregation", ports_1gbe=0, ports_mgig=0, uplinks="8x 25G SFP28, 2x 100G QSFP28", poe_support="none", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300X-M_Datasheet"),
        MSSwitch(model="C9300X-24Y-M", use_case="aggregation", ports_1gbe=0, ports_mgig=0, uplinks="8x 25G SFP28, 2x 100G QSFP28", poe_support="none", stackable=True, routing="dynamic", catalyst=True, datasheet_url="https://documentation.meraki.com/MS/MS_Overview_and_Specifications/Catalyst_9300X-M_Datasheet"),
    ]

    mx_appliances = [
        # Desktop/small branch models
        MXAppliance(model="MX67", use_case="small branch", throughput_mbps=700, max_users=50, uplink_ports=["1x GbE RJ45"], has_wireless=False, has_cellular=False, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX67_and_MX68_Datasheet"),
        MXAppliance(model="MX67W", use_case="small branch", throughput_mbps=700, max_users=50, uplink_ports=["1x GbE RJ45"], has_wireless=True, has_cellular=False, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX67_and_MX68_Datasheet"),
        MXAppliance(model="MX67C", use_case="small branch", throughput_mbps=700, max_users=50, uplink_ports=["1x GbE RJ45", "Cat 6 LTE"], has_wireless=False, has_cellular=True, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX67_and_MX68_Datasheet"),
        MXAppliance(model="MX68", use_case="small branch", throughput_mbps=700, max_users=50, uplink_ports=["2x GbE RJ45"], has_wireless=False, has_cellular=False, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX67_and_MX68_Datasheet"),
        MXAppliance(model="MX68W", use_case="small branch", throughput_mbps=700, max_users=50, uplink_ports=["2x GbE RJ45"], has_wireless=True, has_cellular=False, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX67_and_MX68_Datasheet"),
        MXAppliance(model="MX68CW", use_case="small branch", throughput_mbps=700, max_users=50, uplink_ports=["2x GbE RJ45", "Cat 6 LTE"], has_wireless=True, has_cellular=True, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX67_and_MX68_Datasheet"),

        # Medium branch
        MXAppliance(model="MX75", use_case="medium branch", throughput_mbps=1000, max_users=200, uplink_ports=["2x GbE RJ45", "1x GbE SFP"], has_wireless=False, has_cellular=False, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX75_Datasheet"),
        MXAppliance(model="MX85", use_case="medium branch", throughput_mbps=1000, max_users=200, uplink_ports=["2x GbE RJ45", "2x GbE SFP"], has_wireless=False, has_cellular=False, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX85_Datasheet"),

        # Large branch
        MXAppliance(model="MX95", use_case="large branch", throughput_mbps=2500, max_users=500, uplink_ports=["2x 10G SFP+"], has_wireless=False, has_cellular=False, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX95%2F%2F105_Datasheet"),
        MXAppliance(model="MX105", use_case="large branch", throughput_mbps=5000, max_users=750, uplink_ports=["2x 10G SFP+", "2x 2.5G RJ45"], has_wireless=False, has_cellular=False, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX95%2F%2F105_Datasheet"),

        # Campus and VPN Concentrators
        MXAppliance(model="MX250", use_case="campus or VPN concentrator", throughput_mbps=7500, max_users=2000, uplink_ports=["8x RJ45", "8x SFP", "8x 10G SFP+"], has_wireless=False, has_cellular=False, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX250_Datasheet"),
        MXAppliance(model="MX450", use_case="campus or VPN concentrator", throughput_mbps=10000, max_users=10000, uplink_ports=["8x RJ45", "8x SFP", "8x 10G SFP+"], has_wireless=False, has_cellular=False, datasheet_url="https://documentation.meraki.com/MX/MX_Overviews_and_Specifications/MX450_Datasheet"),

        # Virtual appliances
        MXAppliance(model="vMX Small", use_case="cloud VPN", throughput_mbps=250, max_users=50, uplink_ports=["virtual"], has_wireless=False, has_cellular=False, datasheet_url="https://meraki.cisco.com/product-collateral/mx-family-datasheet/"),
        MXAppliance(model="vMX Medium", use_case="cloud VPN", throughput_mbps=500, max_users=250, uplink_ports=["virtual"], has_wireless=False, has_cellular=False, datasheet_url="https://meraki.cisco.com/product-collateral/mx-family-datasheet/"),
        MXAppliance(model="vMX Large", use_case="cloud VPN", throughput_mbps=1000, max_users=1000, uplink_ports=["virtual"], has_wireless=False, has_cellular=False, datasheet_url="https://meraki.cisco.com/product-collateral/mx-family-datasheet/"),
    ]

    mr_access_points = [
        # Wi-Fi 6
        MRAccessPoint(model="MR28", wifi_standard="Wi-Fi 6", radios=2, antenna_type="internal", poe=True, catalyst=False, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR28_Datasheet"),
        MRAccessPoint(model="MR36", wifi_standard="Wi-Fi 6", radios=2, antenna_type="internal", poe=True, catalyst=False, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR36_Datasheet"),
        MRAccessPoint(model="MR36H", wifi_standard="Wi-Fi 6", radios=2, antenna_type="internal", poe=True, catalyst=False, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR36H_Datasheet"),
        MRAccessPoint(model="MR44", wifi_standard="Wi-Fi 6", radios=2, antenna_type="internal", poe=True, catalyst=False, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR44_Datasheet"),
        MRAccessPoint(model="MR46", wifi_standard="Wi-Fi 6", radios=3, antenna_type="internal", poe=True, catalyst=False, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR46_Datasheet"),
        MRAccessPoint(model="MR46E", wifi_standard="Wi-Fi 6", radios=3, antenna_type="external", poe=True, catalyst=False, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR46E_Datasheet"),
        MRAccessPoint(model="MR55", wifi_standard="Wi-Fi 6", radios=3, antenna_type="internal", poe=True, catalyst=False, datasheet_url="https://meraki.cisco.com/product-collateral/mr55-datasheet/"),
        MRAccessPoint(model="MR56", wifi_standard="Wi-Fi 6", radios=3, antenna_type="internal", poe=True, catalyst=False, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR56_Datasheet"),
        MRAccessPoint(model="MR70", wifi_standard="Wi-Fi 5", radios=2, antenna_type="internal", poe=True, catalyst=False, datasheet_url="https://meraki.cisco.com/product-collateral/mr70-datasheet/"),
        MRAccessPoint(model="MR76", wifi_standard="Wi-Fi 6", radios=2, antenna_type="external", poe=True, catalyst=False, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR76_Datasheet"),
        MRAccessPoint(model="MR78", wifi_standard="Wi-Fi 6", radios=2, antenna_type="internal", poe=True, catalyst=False, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR78_Datasheet"),
        MRAccessPoint(model="MR86", wifi_standard="Wi-Fi 6", radios=2, antenna_type="external", poe=True, catalyst=False, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR86_Datasheet"),

        # Wi-Fi 6E Catalyst
        MRAccessPoint(model="MR57", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="internal", poe=True, catalyst=False, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/MR57_Datasheet"),
        MRAccessPoint(model="CW9162", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="internal", poe=True, catalyst=True, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/CW9162_Datasheet"),
        MRAccessPoint(model="CW9163E", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="external", poe=True, catalyst=True, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/CW9163E_Datasheet"),
        MRAccessPoint(model="CW9164", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="internal", poe=True, catalyst=True, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/CW9164_Datasheet"),
        MRAccessPoint(model="CW9166", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="internal", poe=True, catalyst=True, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/CW9166_Datasheet"),
        MRAccessPoint(model="CW9166D1", wifi_standard="Wi-Fi 6E", radios=3, antenna_type="internal", poe=True, catalyst=True, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/CW9166D1_Datasheet"),

        # Wi-Fi 7 Catalyst
        MRAccessPoint(model="CW9172H", wifi_standard="Wi-Fi 7", radios=3, antenna_type="internal", poe=True, catalyst=True, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/CW9172H_Datasheet"),
        MRAccessPoint(model="CW9172I", wifi_standard="Wi-Fi 7", radios=3, antenna_type="internal", poe=True, catalyst=True, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/CW9172I_Datasheet"),
        MRAccessPoint(model="CW9176I", wifi_standard="Wi-Fi 7", radios=3, antenna_type="internal", poe=True, catalyst=True, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/CW9176I_Datasheet"),
        MRAccessPoint(model="CW9176D1", wifi_standard="Wi-Fi 7", radios=3, antenna_type="internal", poe=True, catalyst=True, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/CW9176D1_Datasheet"),
        MRAccessPoint(model="CW9178I", wifi_standard="Wi-Fi 7", radios=3, antenna_type="internal", poe=True, catalyst=True, datasheet_url="https://documentation.meraki.com/MR/MR_Overview_and_Specifications/CW9178I_Datasheet"),
    ]

    mv_cameras = [
        MVCamera(model="MV2-HW", use_case="indoor compact", resolution="4mp", onboard_storage=False, location="indoor", fov="wide", max_fps=15, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV2_Datasheet"),
        MVCamera(model="MV12WE-HW", use_case="indoor mini dome", resolution="1080p", onboard_storage=True, location="indoor", fov="wide", max_fps=15, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV12_Series_Datasheet"),
        MVCamera(model="MV12W-HW", use_case="indoor mini dome", resolution="1080p", onboard_storage=True, location="indoor", fov="wide", max_fps=15, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV12_Series_Datasheet"),
        MVCamera(model="MV12N-HW", use_case="indoor narrow dome", resolution="1080p", onboard_storage=True, location="indoor", fov="narrow", max_fps=15, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV12_Series_Datasheet"),
        MVCamera(model="MV13-HW", use_case="indoor fixed dome", resolution="4k", onboard_storage=True, location="indoor", fov="wide", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV13_Datasheet"),
        MVCamera(model="MV13M-HW", use_case="indoor fixed dome", resolution="4k", onboard_storage=True, location="indoor", fov="wide", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV13_Datasheet"),
        MVCamera(model="MV22-HW", use_case="indoor varifocal dome", resolution="4mp", onboard_storage=True, location="indoor", fov="wide", max_fps=15, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV22_Series_Datasheet"),
        MVCamera(model="MV22X-HW", use_case="indoor varifocal dome", resolution="4mp", onboard_storage=True, location="indoor", fov="wide", max_fps=15, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV22_Series_Datasheet"),
        MVCamera(model="MV23M-HW", use_case="indoor varifocal dome", resolution="4k", onboard_storage=True, location="indoor", fov="wide", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV23_Series_Datasheet"),
        MVCamera(model="MV23X-HW", use_case="indoor varifocal dome", resolution="4k", onboard_storage=True, location="indoor", fov="wide", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV23_Series_Datasheet"),
        MVCamera(model="MV32-HW", use_case="indoor fisheye", resolution="4.2mp", onboard_storage=True, location="indoor", fov="fisheye", max_fps=15, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV32_Datasheet"),
        MVCamera(model="MV33-HW", use_case="indoor fisheye", resolution="8mp", onboard_storage=True, location="indoor", fov="fisheye", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV33_Datasheet"),
        MVCamera(model="MV33M-HW", use_case="indoor fisheye", resolution="8mp", onboard_storage=True, location="indoor", fov="fisheye", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV33_Datasheet"),
        MVCamera(model="MV52-HW", use_case="outdoor telephoto bullet", resolution="4k", onboard_storage=True, location="outdoor", fov="narrow", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV52_Datasheet"),
        MVCamera(model="MV53X", use_case="outdoor telephoto bullet", resolution="4k", onboard_storage=True, location="outdoor", fov="narrow", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV53X_Datasheet"),
        MVCamera(model="MV63-HW", use_case="outdoor fixed dome", resolution="4k", onboard_storage=True, location="outdoor", fov="wide", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV63_Series_Datasheet"),
        MVCamera(model="MV63M-HW", use_case="outdoor fixed dome", resolution="4k", onboard_storage=True, location="outdoor", fov="wide", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV63_Series_Datasheet"),
        MVCamera(model="MV63X-HW", use_case="outdoor fixed dome", resolution="4k", onboard_storage=True, location="outdoor", fov="wide", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV63_Series_Datasheet"),
        MVCamera(model="MV72-HW", use_case="outdoor dome", resolution="4mp", onboard_storage=True, location="outdoor", fov="wide", max_fps=15, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV72_Series_Datasheet"),
        MVCamera(model="MV72X-HW", use_case="outdoor dome", resolution="4mp", onboard_storage=True, location="outdoor", fov="wide", max_fps=15, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV72_Series_Datasheet"),
        MVCamera(model="MV73M-HW", use_case="outdoor varifocal dome", resolution="4k", onboard_storage=True, location="outdoor", fov="wide", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV73_Series_Datasheet"),
        MVCamera(model="MV73X-HW", use_case="outdoor varifocal dome", resolution="4k", onboard_storage=True, location="outdoor", fov="wide", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV73_Series_Datasheet"),
        MVCamera(model="MV84X", use_case="outdoor multi-imager", resolution="4x5mp", onboard_storage=True, location="outdoor", fov="wide", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV84X_Datasheet"),
        MVCamera(model="MV93-HW", use_case="outdoor fisheye", resolution="8mp", onboard_storage=True, location="outdoor", fov="fisheye", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV93_Series_Datasheet"),
        MVCamera(model="MV93M-HW", use_case="outdoor fisheye", resolution="8mp", onboard_storage=True, location="outdoor", fov="fisheye", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV93_Series_Datasheet"),
        MVCamera(model="MV93X-HW", use_case="outdoor fisheye", resolution="8mp", onboard_storage=True, location="outdoor", fov="fisheye", max_fps=24, datasheet_url="https://documentation.meraki.com/MV/MV_Datasheets/MV93_Series_Datasheet"),
    ]

    db.add_all(ms_switches + mx_appliances + mr_access_points + mv_cameras)
    db.commit()
    db.close()

if __name__ == "__main__":
    seed_data()
