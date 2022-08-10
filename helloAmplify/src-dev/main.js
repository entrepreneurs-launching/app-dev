import React from 'react';

import {NavigationContainer} from '@react-navigation/native';
import {createNativeStackNavigator} from '@react-navigation/native-stack';
import {SafeAreaProvider} from 'react-native-safe-area-context';

import Trips from './screens/screen-trips';
import TripDetails from './screens/screen-trip-details';
import Test from './test';

const Stack = createNativeStackNavigator();

export default function Main() {
  var ret = (
    <SafeAreaProvider>
      <NavigationContainer>
        <Stack.Navigator initialRouteName="Trips">
          <Stack.Screen
            name="Trips"
            component={Trips}
            options={{headerShown: false}}
          />
          <Stack.Screen name="Details" component={TripDetails} />
        </Stack.Navigator>
      </NavigationContainer>
    </SafeAreaProvider>
  );
  // ret = <Test/>;

  return ret;
}

/*
      <NavigationContainer>
        <Stack.Navigator>
          <Stack.Screen name="Trips" component={Trips} />
        </Stack.Navigator>
      </NavigationContainer>

 */
