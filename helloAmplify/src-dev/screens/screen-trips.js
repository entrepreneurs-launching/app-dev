import React, {useEffect, useState, useCallback} from 'react';
import {View, Text, Platform, ScrollView, RefreshControl} from 'react-native';

import TitleBar from './titlebar';
import styles from '../style/style';

export default function Trips() {
  console.info('app: showing trips screen');

  return (
    <>
      <TitleBar text="Trips" color="lightblue" barstyle="light-content" />
      <View>
        <ScrollView
          
          keyboardDismissMode="on-drag"
          showsVerticalScrollIndicator={false}>
              <Text>I AM DONE</Text>
              <Text>I AM DONE</Text>
          
        </ScrollView>
      </View>
    </>
  );
}
