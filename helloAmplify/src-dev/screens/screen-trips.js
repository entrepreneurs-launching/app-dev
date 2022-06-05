import React, {useRef, seEffect, useState, useCallback} from 'react';
import {
  View,
  Text,
  Platform,
  ScrollView,
  Animated,
  RefreshControl,
  Dimensions,
  Button,
  StatusBar,
} from 'react-native';

import {SafeAreaProvider, SafeAreaView} from 'react-native-safe-area-context';

import AnimatedHeader from './animated-header';
import TitleBar from './titlebar';
import TripsCard from './screen-trips-card';
import styles from '../style/style';
import urls from '../strings/urls';

const HEADER_HEIGHT = urls.constHeaderHeight;

export default function Trips() {
  console.info('app: showing trips screen');

  const offset = useRef(new Animated.Value(0)).current;

  return (
    <SafeAreaProvider>
      <StatusBar
        barStyle="dark-content"
        backgroundColor="gainsboro"
        translucent={true}
      />

      <AnimatedHeader animatedValue={offset} />

      <ScrollView
        style={{flex: 1, backgroundColor: 'white'}}
        contentContainerStyle={{
          alignItems: 'center',
          paddingTop: HEADER_HEIGHT * 2 + 50,
        }}
        showsVerticalScrollIndicator={false}
        scrollEventThrottle={16}
        onScroll={Animated.event(
          [{nativeEvent: {contentOffset: {y: offset}}}],
          {useNativeDriver: false},
        )}>
        <TripsCard text="2 day trip to Delhi" uri={urls.urlDelhi}></TripsCard>
        <TripsCard text="3 day trip to Mumbai" uri={urls.urlMumbai}></TripsCard>
        <TripsCard
          text="1 day trip to Bangalore"
          uri={urls.urlBangalore}></TripsCard>
        <TripsCard
          text="2 day trip to Calcutta"
          uri={urls.urlCalcutta}></TripsCard>
        <TripsCard text="2 day trip to Delhi" uri={urls.urlDelhi}></TripsCard>
        <TripsCard text="3 day trip to Mumbai" uri={urls.urlMumbai}></TripsCard>
        <TripsCard
          text="1 day trip to Bangalore"
          uri={urls.urlBangalore}></TripsCard>
        <TripsCard
          text="2 day trip to Calcutta"
          uri={urls.urlCalcutta}></TripsCard>
        <TripsCard text="2 day trip to Delhi" uri={urls.urlDelhi}></TripsCard>
        <TripsCard text="3 day trip to Mumbai" uri={urls.urlMumbai}></TripsCard>
        <TripsCard
          text="1 day trip to Bangalore"
          uri={urls.urlBangalore}></TripsCard>
        <TripsCard
          text="2 day trip to Calcutta"
          uri={urls.urlCalcutta}></TripsCard>
      </ScrollView>
    </SafeAreaProvider>
  );
}
