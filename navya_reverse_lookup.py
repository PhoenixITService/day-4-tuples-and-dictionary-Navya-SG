scores={"Anita":92,
        "Ravi":85,
        "Kiran":76,
        "Zoya":88}
print(dict(zip(scores.values(),scores.keys())).get(int(input("Enter score:")),"Not found"))