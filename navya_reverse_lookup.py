scores={"anita":92,
        "ravi":85,
        "kiran":76,
        "zoya":88}
score=int(input("enter score:"))
zip_data = dict(zip(scores.values(),scores.keys()))
print(zip_data.get(score,"score not found"))