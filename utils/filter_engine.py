from sqlalchemy.orm import Session
from sqlalchemy import func
from database import SessionLocal
from models.mx import MXAppliance
from models.ms import MSSwitch
from models.mr import MRAccessPoint
from models.mv import MVCamera

def at_least_one_filter_applied(filters: dict) -> bool:
    return any(v not in [None, "", "false"] for v in filters.values())

def filter_mx_models(filters):
    mx_keys = ["has_cellular", "has_wireless", "use_case", "min_throughput", "min_users", "uplink_ports"]
    mx_filters = {k: filters.get(k) for k in mx_keys}
    if not at_least_one_filter_applied(mx_filters):
        return None, "Please select at least one filter to continue."

    db: Session = SessionLocal()
    query = db.query(MXAppliance)

    if filters.get("has_cellular") == "true":
        query = query.filter(MXAppliance.has_cellular.is_(True))
    if filters.get("has_wireless") == "true":
        query = query.filter(MXAppliance.has_wireless.is_(True))
    if filters.get("use_case"):
        query = query.filter(func.lower(MXAppliance.use_case) == filters["use_case"].lower())
    if filters.get("min_throughput"):
        query = query.filter(MXAppliance.throughput_mbps >= int(filters["min_throughput"]))
    if filters.get("min_users"):
        query = query.filter(MXAppliance.max_users >= int(filters["min_users"]))
    if filters.get("uplink_ports"):
        query = query.filter(func.lower(MXAppliance.uplink_ports).like(f"%{filters['uplink_ports'].lower()}%"))

    results = query.all()
    db.close()
    return results, None

def filter_ms_models(filters):
    ms_keys = ["poe_support", "routing", "min_ports_1gbe", "min_ports_mgig", "stackable", "catalyst"]
    ms_filters = {k: filters.get(k) for k in ms_keys}
    if not at_least_one_filter_applied(ms_filters):
        return None, "Please select at least one filter to continue."

    db: Session = SessionLocal()
    query = db.query(MSSwitch)

    if filters.get("poe_support"):
        query = query.filter(func.lower(MSSwitch.poe_support) == filters["poe_support"].lower())
    if filters.get("routing"):
        query = query.filter(func.lower(MSSwitch.routing) == filters["routing"].lower())
    if filters.get("min_ports_1gbe"):
        query = query.filter(MSSwitch.ports_1gbe >= int(filters["min_ports_1gbe"]))
    if filters.get("min_ports_mgig"):
        query = query.filter(MSSwitch.ports_mgig >= int(filters["min_ports_mgig"]))
    if filters.get("stackable") == "true":
        query = query.filter(MSSwitch.stackable.is_(True))
    if filters.get("catalyst") == "true":
        query = query.filter(MSSwitch.catalyst.is_(True))

    results = query.all()
    db.close()
    return results, None

def filter_mr_models(filters):
    mr_keys = ["wifi_standard", "radios", "antenna_type", "poe", "catalyst"]
    mr_filters = {k: filters.get(k) for k in mr_keys}
    if not at_least_one_filter_applied(mr_filters):
        return None, "Please select at least one filter to continue."

    db: Session = SessionLocal()
    query = db.query(MRAccessPoint)

    if filters.get("wifi_standard"):
        query = query.filter(func.lower(MRAccessPoint.wifi_standard) == filters["wifi_standard"].lower())
    if filters.get("radios"):
        query = query.filter(MRAccessPoint.radios == int(filters["radios"]))
    if filters.get("antenna_type"):
        query = query.filter(func.lower(MRAccessPoint.antenna_type) == filters["antenna_type"].lower())
    if filters.get("poe") == "true":
        query = query.filter(MRAccessPoint.poe.is_(True))
    if filters.get("catalyst") == "true":
        query = query.filter(MRAccessPoint.catalyst.is_(True))

    results = query.all()
    db.close()
    return results, None

def filter_mv_models(filters):
    mv_keys = ["location", "fov", "max_fps", "resolution"]
    mv_filters = {k: filters.get(k) for k in mv_keys}
    if not at_least_one_filter_applied(mv_filters):
        return None, "Please select at least one filter to continue."

    db: Session = SessionLocal()
    query = db.query(MVCamera)

    if filters.get("location"):
        query = query.filter(func.lower(MVCamera.location) == filters["location"].lower())
    if filters.get("fov"):
        query = query.filter(func.lower(MVCamera.fov) == filters["fov"].lower())
    if filters.get("max_fps"):
        query = query.filter(MVCamera.max_fps == int(filters["max_fps"]))
    if filters.get("resolution"):
        query = query.filter(func.lower(MVCamera.resolution) == filters["resolution"].lower())

    results = query.all()
    db.close()
    return results, None