import React, {useRef, useEffect, useState} from 'react';
import {
  View,
  Text,
  Button,
  Platform,
  ScrollView,
  FlatList,
  Animated,
  RefreshControl,
  StatusBar,
} from 'react-native';

import {RNCarousel} from 'react-native-carousel-cards';

import styles from '../style/style';

export default function TripDetails({route, navigation}) {
  const {dest, id} = route.params;

  const idx = id;
  const item = dest;
  
  const place = item.place;
  const state = item.state;
  const image = item.image.split(',').map(item => item.trim());
  // console.log('sup: array' + item.image);


  return (
    <View>
      <Text style={styles.basicText}>Lets Go To {place}</Text>
    </View>
  );
}
