from database import engine, Base
from models.ms import MSSwitch
from models.mr import MRAccessPoint
from models.mv import MVCamera
from models.mx import MXAppliance  # ✅ Fixed import

# ✅ Create all tables defined by the Base metadata
Base.metadata.create_all(bind=engine)