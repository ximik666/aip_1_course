# Проектирование и защита второго проекта
def report_checks(checks):
    return {"passed": sum(checks), "total": len(checks)}

assert report_checks([True, False, True]) == {"passed": 2, "total": 3}
