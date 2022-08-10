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

import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';

import {
  SafeAreaProvider, // added in main.js
  useSafeAreaInsets,
  SafeAreaView,
} from 'react-native-safe-area-context';
import {Auth, API, graphqlOperation, Storage} from 'aws-amplify';
import {listTrips, getTrips} from '../../src/graphql/queries';

import AnimatedHeader from './animated-header';
import TripsCard from './screen-trips-card';
import TripsCardHalf from './screen-trips-card-half';
import {shuffleArray} from '../utils/shuffle-array';
import {anyColor, anyHexColor} from '../utils/colors';
import urls from '../strings/urls';
import TitleBar from './titlebar';
import TripDetails from './screen-trip-details';
import styles from '../style/style';

const Stack = createNativeStackNavigator();
const HEADER_HEIGHT = urls.constHeaderHeight;

export default function Trips({navigation}) {
  const offset = useRef(new Animated.Value(0)).current;
  const insets = useSafeAreaInsets();

  const [tripList, setTrips] = useState([]);
  const [refreshing, setRefreshing] = useState(false);

  const fetchTrips = async () => {
    console.log('sup fetchTrips');
    try {
      //    trips = await API.graphql(graphqlOperation(listTrips, {limit: 2}));
      const trips = await API.graphql(graphqlOperation(listTrips));

      if (trips.data.listTrips) {
        console.log('sup: Trips:' + trips.data.listTrips.items.length);
        shuffleArray(trips.data.listTrips.items);
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

  const onSelectTrip = idx => {
    console.log('sup: onPressTrip ' + idx);
    const item = tripList[idx]
    navigation.navigate('Details', {dest: item, id: idx});
  };

  const columns1 = 1;
  const renderItem1 = ({item, index}) => (
    <TripsCard dest={item} id={index} key={index} />
  );
  const columns2 = 2;
  const renderItem2 = ({item, index}) => (
    <TripsCardHalf dest={item} id={index} key={index} onSelect={onSelectTrip} />
  );

  return (
    <>
      <StatusBar
        // hidden
        // backgroundColor="transparent"
        backgroundColor="gainsboro"
        barStyle="dark-content"
        translucent={true}
      />

      <AnimatedHeader animatedValue={offset} />

      <FlatList
        data={tripList}
        // if using renderitem1, use columns1
        // if using renderitem2, use columns2
        renderItem={renderItem2}
        numColumns={columns2}
        // the window
        style={{}}
        // the ladder
        contentContainerStyle={{
          paddingTop: HEADER_HEIGHT * 2 + insets.top + 10,
        }}
        showsVerticalScrollIndicator={false}
        scrollEventThrottle={16}
        onScroll={Animated.event(
          [{nativeEvent: {contentOffset: {y: offset}}}],
          {useNativeDriver: false},
        )}
        refreshControl={
          <RefreshControl refreshing={refreshing} onRefresh={onRefresh} />
        }
      />
    </>
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
