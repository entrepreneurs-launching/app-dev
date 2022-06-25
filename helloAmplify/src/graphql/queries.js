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
