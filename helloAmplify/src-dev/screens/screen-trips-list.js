import React from 'react';
import {View, Text, FlatList, StyleSheet, RefreshControl} from 'react-native';

import TripsCard from './screen-trips-card';
import styles from '../style/style';

const TripList = ({tripList, refreshing, onRefresh}) => {
  return (
    <View style={styles.productsView}>
      {tripList && (
        <FlatList
          refreshControl={
            <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
          }
          keyExtractor={item => item.id}
          data={tripList}
          renderItem={({item}) => {
            return <TripsCard text={item.name} uri={item.image} />;
          }}
        />
      )}
    </View>
  );
};

export default TripList;
