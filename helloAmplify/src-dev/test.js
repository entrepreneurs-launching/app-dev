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

export default function Test() {
  return (
    <>
      <View style={{flex: 1}}>
        <ScrollView>
          <Text style={{padding: 20, fontSize: 30}}>Sroll 2</Text>
          <Text style={{padding: 20, fontSize: 30}}>Sroll 2</Text>
          <Text style={{padding: 20, fontSize: 30}}>Sroll 2</Text>
          <Text style={{padding: 20, fontSize: 30}}>Sroll 2</Text>
          <Text style={{padding: 20, fontSize: 30}}>Sroll 2</Text>
          <Text style={{padding: 20, fontSize: 30}}>Sroll 2</Text>
          <Text style={{padding: 20, fontSize: 30}}>Sroll 2</Text>
          <Text style={{padding: 20, fontSize: 30}}>Sroll 2</Text>
          

          <View style={{height: 400, borderColor: 'white', borderWidth: 1}}>
            <ScrollView>
              <Text style={{padding: 20, fontSize: 30}}>Sroll B</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll 1</Text>
              <Text style={{padding: 20, fontSize: 30}}>Sroll E</Text>
            </ScrollView>
          </View>
        </ScrollView>
      </View>
    </>
  );
}
