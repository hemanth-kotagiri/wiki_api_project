import wikipedia as wiki

# print(wiki.__version__)

# print(wiki.summary("Wikipedia"))

def ask_user():
    search = input("What do you want me to search today: ").title()

    results = wiki.page(search)
    print(results.title)
    print(results.content)


if __name__ == "__main__":
    ask_user()