from sqlalchemy.orm import Session
from database import SessionLocal
from models.mx import MXAppliance
from models.ms import MSSwitch
from models.mr import MRAccessPoint
from models.mv import MVCamera

def at_least_one_filter_applied(filters: dict) -> bool:
    return any(v not in [None, "", "false"] for v in filters.values())

def filter_mx_models(filters):
    if not at_least_one_filter_applied(filters):
        return None, "Please select at least one filter to continue."
    
    db: Session = SessionLocal()
    query = db.query(MXAppliance)

    if filters.get("has_cellular") == "true":
        query = query.filter(MXAppliance.has_cellular.is_(True))
    if filters.get("has_wireless") == "true":
        query = query.filter(MXAppliance.has_wireless.is_(True))

    results = query.all()
    db.close()
    return results, None

def filter_ms_models(filters):
    # Define only MS-relevant filter keys
    ms_keys = ["poe_support", "routing", "min_ports_1gbe", "min_ports_mgig", "stackable", "catalyst"]
    ms_filters = {k: filters.get(k) for k in ms_keys}

    # Check if any relevant MS filter is applied
    if not at_least_one_filter_applied(ms_filters):
        return None, "Please select at least one filter to continue."

    db: Session = SessionLocal()
    query = db.query(MSSwitch)

    if filters.get("poe_support"):
        query = query.filter(MSSwitch.poe_support == filters["poe_support"])
    if filters.get("routing"):
        query = query.filter(MSSwitch.routing == filters["routing"])
    if filters.get("min_ports_1gbe"):
        query = query.filter(MSSwitch.ports_1gbe >= int(filters["min_ports_1gbe"]))
    if filters.get("min_ports_mgig"):
        query = query.filter(MSSwitch.ports_mgig >= int(filters["min_ports_mgig"]))
    if filters.get("stackable") == "true":
        query = query.filter(MSSwitch.stackable == True)
    if filters.get("catalyst") == "true":
        query = query.filter(MSSwitch.catalyst == True)

    results = query.all()
    db.close()
    return results, None

def filter_mr_models(filters):
    if not at_least_one_filter_applied(filters):
        return None, "Please select at least one filter to continue."

    db: Session = SessionLocal()
    query = db.query(MRAccessPoint)

    if filters.get("wifi_standard"):
        query = query.filter(MRAccessPoint.wifi_standard == filters["wifi_standard"])
    if filters.get("radios"):
        query = query.filter(MRAccessPoint.radios == int(filters["radios"]))
    if filters.get("antenna_type"):
        query = query.filter(MRAccessPoint.antenna_type == filters["antenna_type"].lower())
    if filters.get("poe") == "true":
        query = query.filter(MRAccessPoint.poe.is_(True))
    if filters.get("poe") == "false":
        query = query.filter(MRAccessPoint.poe.is_(False))
    if filters.get("catalyst") == "true":
        query = query.filter(MRAccessPoint.catalyst.is_(True))

    results = query.all()
    db.close()
    return results, None

def filter_mv_models(filters):
    if not at_least_one_filter_applied(filters):
        return None, "Please select at least one filter to continue."

    db: Session = SessionLocal()
    query = db.query(MVCamera)

    if filters.get("location"):
        query = query.filter(MVCamera.location == filters["location"].lower())
    if filters.get("fov"):
        query = query.filter(MVCamera.fov == filters["fov"].lower())
    if filters.get("onboard_storage") == "true":
        query = query.filter(MVCamera.onboard_storage.is_(True))
    if filters.get("onboard_storage") == "false":
        query = query.filter(MVCamera.onboard_storage.is_(False))
    if filters.get("max_fps"):
        query = query.filter(MVCamera.max_fps == int(filters["max_fps"]))

    results = query.all()
    db.close()
    return results, None