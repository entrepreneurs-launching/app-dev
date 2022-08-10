import React from 'react';
import {
  Animated,
  ScrollView,
  TouchableOpacity,
  View,
  Text,
  StyleSheet,
  StatusBar,
} from 'react-native';

import {SafeAreaView} from 'react-native-safe-area-context';

import style from '../style/style';
import TitleBar from './titlebar';
import urls from '../strings/urls';

const HEADER_HEIGHT = urls.constHeaderHeight;

const AnimatedHeader = ({animatedValue}) => {

  const headerHeight = animatedValue.interpolate({
    inputRange: [0, HEADER_HEIGHT],
    outputRange: [0, -HEADER_HEIGHT],
    extrapolate: 'clamp',
  });

  return (
    <Animated.View
      style={{
        position: 'absolute',
        top: headerHeight,
        zIndex: 3,
        backgroundColor: 'gainsboro',
      }}>
      <SafeAreaView edges={['top']}>
        <Text style={style.titleBarText}>Trips</Text>
        <ScrollView
          horizontal={true}
          style={{paddingRight: 20, paddingBottom: 10}}>
          <View
            style={{
              flexDirection: 'column',
              flex: 1,
              justifyContent: 'flex-end',
            }}>
            <View style={localstyles.filterButtons}>
              <Text style={style.basicText}>1 Day</Text>
            </View>
          </View>
          <View
            style={{
              flexDirection: 'column',
              flex: 1,
              justifyContent: 'flex-end',
            }}>
            <View style={localstyles.filterButtons}>
              <Text style={style.basicText}>2 Day</Text>
            </View>
          </View>

          <View
            style={{
              flexDirection: 'column',
              flex: 1,
              justifyContent: 'flex-end',
            }}>
            <View style={localstyles.filterButtons}>
              <Text style={style.basicText}>3 Day {'>'}</Text>
            </View>
          </View>

          <View
            style={{
              flexDirection: 'column',
              flex: 1,
              justifyContent: 'flex-end',
            }}>
            <View style={localstyles.filterButtons}>
              <Text style={style.basicText}>Romantic</Text>
            </View>
          </View>

          <View
            style={{
              flexDirection: 'column',
              flex: 1,
              justifyContent: 'flex-end',
            }}>
            <View style={[localstyles.filterButtons, {marginRight: 10}]}>
              <Text style={style.basicText}>Adventure</Text>
            </View>
          </View>
        </ScrollView>
      </SafeAreaView>
    </Animated.View>
  );
};

export default AnimatedHeader;

const localstyles = StyleSheet.create({
  filterButtons: {
    borderColor: 'grey',
    borderWidth: 2,
    borderRadius: 15,
    marginLeft: 10,
    padding: 10,
    paddingLeft: 20,
    paddingRight: 20,
    justifyContent: 'center',
    backgroundColor: 'lightgray',
  },
});
