states = ["Kansas", "Nebraska", "North Dakota", "South Dakota"]

def urlify(string):
    """Converts a string into a URL-friendly string."""
    return string.lower().replace(" ", "-")

#urls: imperative version
def imperatitve_urls(states):
    urls = []
    for state in states:
        urls.append(urlify(state))
    return urls

print(imperatitve_urls(states))

#urls: functional version, list comprehension
def functional_urls(states):
    return [urlify(state) for state in states]

print(functional_urls(states))