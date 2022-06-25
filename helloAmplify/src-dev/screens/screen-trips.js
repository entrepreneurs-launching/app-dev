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

import {SafeAreaProvider, SafeAreaView} from 'react-native-safe-area-context';
import {Auth, API, graphqlOperation, Storage} from 'aws-amplify';
import {listTrips, getTrips} from '../../src/graphql/queries';

import AnimatedHeader from './animated-header';
import TripsCard from './screen-trips-card';
import {shuffleArray} from '../utils/shuffle-array';
import urls from '../strings/urls';
import TripList from './screen-trips-list';
import TitleBar from './titlebar';
import styles from '../style/style';

const HEADER_HEIGHT = urls.constHeaderHeight;

export default function Trips() {
  const offset = useRef(new Animated.Value(0)).current;

  const [tripList, setTrips] = useState([]);
  const [refreshing, setRefreshing] = useState(false);

  const fetchTrips = async () => {
    console.log('sup fetchTrips');
    try {
      //    trips = await API.graphql(graphqlOperation(listTrips, {limit: 2}));
      const trips = await API.graphql(graphqlOperation(listTrips));

      if (trips.data.listTrips) {
        console.log('sup: Trips:');
        console.log(trips);
        // shuffleArray(trips.data.listTrips.items);
        setTrips(trips.data.listTrips.items);
      }
    } catch (e) {
      console.log('sup: fetchTrips error');
      console.log(e.message);
    }
  };
  useEffect(() => {
    fetchTrips();
  }, []);

  const onRefresh = async () => {
    setRefreshing(true);
    await fetchTrips();
    setRefreshing(false);
  };

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
        )}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
        }>
        {tripList.map((item, index) => (
          <View key={index}>
            <TripsCard dest={item} id={index} key={index} />
          </View>
        ))}
      </ScrollView>
    </SafeAreaProvider>
  );
}

/* 
  const buttonPress = async () => {
    console.log('sup: press');
    try {
      const user = await Auth.currentAuthenticatedUser();

      const response = await API.graphql(
        graphqlOperation(createTrips, {
          input: {
            id: 'abcd02',
            code: 'abcd02',
            place: 'yosemite',
            state: 'california',
          },
        }),
      );
      console.log('sup: response');
      console.log(response);
    } catch (e) {
      console.log('sup:error');
      console.log(e.message);
    }
  };
  
  <Button title="PRESS" onPress={buttonPress}></Button>

  keyExtractor={item => item.id}
        data={tripList}
        renderItem={({item}) => {
          return <TripsCard text={item.name} uri={urls.urlDelhi} />;
        }}

*/
