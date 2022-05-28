/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 *
 * @format
 * @flow strict-local
 */

import React from 'react';
import type {Node} from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  useColorScheme,
  Button,
  View,
} from 'react-native';

import {withAuthenticator} from 'aws-amplify-react-native';
import {Auth} from 'aws-amplify';

import Main from './src-dev/main';

const App: () => Node = () => {
  /*
  const signOut = async () => {
    try {
      await Auth.signOut();
    } catch (error) {
      console.log('error signing out: ', error);
    }
  };
  <Button title="Signout" onPress={signOut} />
  */

  return <Main />;
};

/*
 * For Authenticator customizations
 * See https://ui.docs.amplify.aws/react/components/authenticator
 */
export default withAuthenticator(App, {
  signUpConfig: {
    hiddenDefaults: ['phone_number'],
  },
});
