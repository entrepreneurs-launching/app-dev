import React, {useRef, useEffect, useState} from 'react';
import {View, Text, ScrollView} from 'react-native';

import TripsCard from './screen-trips-card';
import styles from '../style/style';

export default function TripDetails({route, navigation}) {
  const {dest, id} = route.params;
  const index = id;
  const item = dest;

  return (
    <ScrollView>
      <TripsCard dest={item} id={index} key={index} />
    </ScrollView>
  );
}
