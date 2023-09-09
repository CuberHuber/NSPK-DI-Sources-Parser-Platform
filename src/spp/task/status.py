NONSET = 0
PREPARING = 10
READY = 20
WORKING = 30
SUSPENDED = 40
FINISHED = 50
BROKEN = 60

_statusToName = {
    NONSET: "NONSET",
    PREPARING: "PREPARING",
    WORKING: "WORKING",
    READY: "READY",
    SUSPENDED: "SUSPENDED",
    FINISHED: "FINISHED",
    BROKEN: "BROKEN"
}

_nameToStatus = {
    "NONSET": NONSET,
    "PREPARING": PREPARING,
    "WORKING": WORKING,
    "READY": READY,
    "SUSPENDED": SUSPENDED,
    "FINISHED": FINISHED,
    "BROKEN": BROKEN,
}
