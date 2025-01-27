import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
try: 
    lang = input("For what language would you like to generate a graph?")
    url = f"https://api.github.com/search/repositories?q=language:{lang}&sort=stars"
    headers = {'Accept': 'application/vnd.github.v3+json'} # defines headers, v3 of this API
    r = requests.get(url, headers=headers) # requests and assigns the response to r

    response_dict = r.json() # converts the json to a dictionary
    repo_dicts = response_dict['items']
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)
        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(60, 100, 150)',
            'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': f"Most-Starred {lang.title()} Projects on GitHub",
        'titlefont': {'size': 28},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
            },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 24},
            'tickfont': {'size': 14},
            },
    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='python_repos.html')

except KeyError:
    print("That language is not available. Please ensure it is spelled correctly.")
