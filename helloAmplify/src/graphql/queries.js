/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const getTrips = /* GraphQL */ `
  query GetTrips($id: ID!) {
    getTrips(id: $id) {
      id
      code
      lat
      lon
      latlon
      place
      state
      image
      months
      category
      mindays
      maxdays
      description
      nearby
      createdAt
      updatedAt
      owner
    }
  }
`;
export const listTrips = /* GraphQL */ `
  query ListTrips(
    $filter: ModelTripsFilterInput
    $limit: Int
    $nextToken: String
  ) {
    listTrips(filter: $filter, limit: $limit, nextToken: $nextToken) {
      items {
        id
        code
        lat
        lon
        latlon
        place
        state
        image
        months
        category
        mindays
        maxdays
        description
        nearby
        createdAt
        updatedAt
        owner
      }
      nextToken
    }
  }
`;
export const getAttractions = /* GraphQL */ `
  query GetAttractions($id: ID!) {
    getAttractions(id: $id) {
      id
      json
      weburl
      lat
      lon
      pluscode
      place
      state
      description
      address
      ranking
      rating
      numrev
      numphoto
      category1
      category2
      category3
      category4
      category5
      category6
      category7
      category8
      category9
      createdAt
      updatedAt
      owner
    }
  }
`;
export const listAttractions = /* GraphQL */ `
  query ListAttractions(
    $filter: ModelAttractionsFilterInput
    $limit: Int
    $nextToken: String
  ) {
    listAttractions(filter: $filter, limit: $limit, nextToken: $nextToken) {
      items {
        id
        json
        weburl
        lat
        lon
        pluscode
        place
        state
        description
        address
        ranking
        rating
        numrev
        numphoto
        category1
        category2
        category3
        category4
        category5
        category6
        category7
        category8
        category9
        createdAt
        updatedAt
        owner
      }
      nextToken
    }
  }
`;
