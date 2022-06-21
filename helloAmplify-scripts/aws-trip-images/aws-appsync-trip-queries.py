query1="""
query MyQuery ($limit: Int!) {
  listTrips(limit: $limit) {
    items {
      id
      code
      image
      state
      place
      months
    }
    nextToken
  }
}
"""

queryn="""
query MyQuery ($limit: Int!, $nextToken: String!) {
  listTrips(limit: $limit, nextToken: $nextToken) {
    items {
      id
      code
      image
      state
      place
      months
    }
    nextToken
  }
}
"""

query2="""
query MyQuery ($id: ID!) {
  getTrips(id: $id) {
    id
    code
    place
    state
    image
  }
}
"""

query3="""
mutation MyMutation ($id: ID!, $image: String!) {
  updateTrips(input: {id: $id, image: $image}) {
    id
    code
    image
    place
    state
  }
}
"""


