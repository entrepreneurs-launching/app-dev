/* eslint-disable */
// this is an auto generated file. This will be overwritten

export const createTrips = /* GraphQL */ `
  mutation CreateTrips(
    $input: CreateTripsInput!
    $condition: ModelTripsConditionInput
  ) {
    createTrips(input: $input, condition: $condition) {
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
export const updateTrips = /* GraphQL */ `
  mutation UpdateTrips(
    $input: UpdateTripsInput!
    $condition: ModelTripsConditionInput
  ) {
    updateTrips(input: $input, condition: $condition) {
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
export const deleteTrips = /* GraphQL */ `
  mutation DeleteTrips(
    $input: DeleteTripsInput!
    $condition: ModelTripsConditionInput
  ) {
    deleteTrips(input: $input, condition: $condition) {
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
