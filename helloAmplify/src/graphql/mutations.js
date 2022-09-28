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
export const createAttractions = /* GraphQL */ `
  mutation CreateAttractions(
    $input: CreateAttractionsInput!
    $condition: ModelAttractionsConditionInput
  ) {
    createAttractions(input: $input, condition: $condition) {
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
export const updateAttractions = /* GraphQL */ `
  mutation UpdateAttractions(
    $input: UpdateAttractionsInput!
    $condition: ModelAttractionsConditionInput
  ) {
    updateAttractions(input: $input, condition: $condition) {
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
export const deleteAttractions = /* GraphQL */ `
  mutation DeleteAttractions(
    $input: DeleteAttractionsInput!
    $condition: ModelAttractionsConditionInput
  ) {
    deleteAttractions(input: $input, condition: $condition) {
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
