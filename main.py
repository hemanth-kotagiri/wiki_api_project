import wikipedia as wiki

#Documentation : https://wikipedia.readthedocs.io/en/latest/

# print(wiki.__version__)

# print(wiki.summary("Wikipedia"))

def ask_user():
    search = input("What do you want me to search today(q to quit): ").title()
    if search == 'Q':
        exit()
    results = wiki.page(search)
    print(results.title)
    print(results.content)


if __name__ == "__main__":
    while True:
        ask_user()