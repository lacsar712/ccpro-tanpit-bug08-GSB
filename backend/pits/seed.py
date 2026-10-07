from pits.models import LiquorSample, Pit, User, Yard


def seed_demo() -> None:
    admin, _ = User.objects.get_or_create(username="admin", defaults={"role": "admin"})
    admin.role = "admin"
    admin.set_password("123456")
    admin.save()
    worker, _ = User.objects.get_or_create(username="worker", defaults={"role": "worker"})
    worker.role = "worker"
    worker.set_password("123456")
    worker.save()
    if Yard.objects.exists():
        return
    yard = Yard.objects.create(name="南冈鞣场", village="青皮村")
    layout = [
        ("东-1", Pit.STATUS_TANNING, 0, 2, 4.2),
        ("东-2", Pit.STATUS_FILL, 0, 10, 5.5),
        ("中-1", Pit.STATUS_DRAINED, 1, 2, 4.6),
        ("中-2", Pit.STATUS_TANNING, 1, 10, 6.1),
        ("西-1", Pit.STATUS_FILL, 2, 2, None),
        ("西-2", Pit.STATUS_DRAINED, 2, 10, 3.8),
    ]
    for code, status, row, col, ph in layout:
        pit = Pit.objects.create(yard=yard, code=code, status=status, row=row, col=col)
        if ph is not None:
            LiquorSample.objects.create(pit=pit, ph=ph, operator="worker")
