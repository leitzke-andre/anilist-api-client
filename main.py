import requests

# Here we define our query as a multi-line string
def queryById(id):
    query = '''
    query ($id: Int) { # Define which variables will be used in the query (id)
    Media (id: $id, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
        id
        title {
        romaji
        english
        native
        }
        season
        seasonYear
    }
    }
    '''
    variables = {
        'id': id
    }

    url = 'https://graphql.anilist.co'

    response = requests.post(url, json={'query': query, 'variables': variables})

    return response

def queryBySeasonYear(season, year, page, perPage):
    query = '''
    query ($season: MediaSeason, $seasonYear: Int, $page: Int, $perPage: Int) { # Define which variables will be used in the query (id)
        Page (page: $page, perPage: $perPage) {
            pageInfo {
                total
                currentPage
                lastPage
                hasNextPage
                perPage
            }
            media (season: $season, seasonYear: $seasonYear, type: ANIME) { # Insert our variables into the query arguments (id) (type: ANIME is hard-coded in the query)
                id
                title {
                    romaji
                    english
                    native
                }
                season
                seasonYear
            }
        }
    }
    '''
    variables = {
        'season': season,
        'seasonYear': year,
        'page': page,
        'perPage': perPage
    }

    url = 'https://graphql.anilist.co'

    response = requests.post(url, json={'query': query, 'variables': variables})

    return response


# response = queryById(1)
response = queryBySeasonYear('WINTER', 2022, 1, 500)

print(response.status_code)
print(response.text)

