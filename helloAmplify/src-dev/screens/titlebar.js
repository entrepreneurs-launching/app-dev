import React from 'react';
import {StatusBar, SafeAreaView, Text} from 'react-native';

import styles from '../style/style';

export default function TitleBar(props) {
  var textcolor;
  console.debug('app: showing title bar');
  if (props.barstyle == 'dark-content') {
    textcolor = 'black';
  }
  if (props.barstyle == 'light-content') {
    textcolor = 'white';
  }
  return (
    <>
      <StatusBar
        barStyle={props.barstyle}
        backgroundColor={props.color}
        translucent={false}
      />
      <SafeAreaView
        style={[styles.titleBarView, {backgroundColor: props.color}]}>
        <Text style={[styles.titleBarText, {color: textcolor}]}>
          {props.text}
        </Text>
      </SafeAreaView>
    </>
  );
}
