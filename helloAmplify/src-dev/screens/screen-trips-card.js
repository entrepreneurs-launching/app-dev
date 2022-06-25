import React, {useState, useEffect} from 'react';
import {View, Text, Dimensions, Image, ImageEditor} from 'react-native';

import {RNCarousel} from 'react-native-carousel-cards';
import {Storage} from 'aws-amplify';

import styles from '../style/style';
import urls from '../strings/urls';

export default function TripsCard(props) {
  const cardWidth = Dimensions.get('window').width * 0.95;
  const cardHeight = cardWidth * 0.6;

  const item = props.dest;
  const place = item.place;
  const state = item.state;
  const image = item.image.split(',').map(item => item.trim());
  // console.log('sup: array' + item.image);

  const randDay = () => {
    min = 1;
    max = 4;
    return Math.floor(Math.random() * (max - min)) + min;
  };
  const todayHour = () => {
    const now = new Date();
    return now.getHours();
  };

  const [imageURLA, setImageURLA] = useState(null);
  const [imageURLB, setImageURLB] = useState(null);
  const [imageURLC, setImageURLC] = useState(null);

  const getImageA = async i => {
    try {
      const imageurl = await Storage.get(image[i]);
      setImageURLA(imageurl);
      // console.log('sup: ' + imageurl);
    } catch (e) {
      console.log(e);
    }
  };
  const getImageB = async i => {
    try {
      const imageurl = await Storage.get(image[i]);
      setImageURLB(imageurl);
      // console.log('sup: ' + imageurl);
    } catch (e) {
      console.log(e);
    }
  };
  const getImageC = async i => {
    try {
      const imageurl = await Storage.get(image[i]);
      setImageURLC(imageurl);
      // console.log('sup: ' + imageurl);
    } catch (e) {
      console.log(e);
    }
  };
  useEffect(() => {
    hour = todayHour();
    a = (hour % 4) + 0;
    b = (hour % 3) + 4;
    c = (hour % 3) + 4 + 3;
    // console.log('sup: ' + hour + ' ' + a + ' ' + b + ' ' + c);
    getImageA(a);
    getImageB(b);
    getImageC(c);
  }, []);

  return (
    <View style={{paddingTop: 10}} key={props.id}>
      <RNCarousel
        key={props.id}
        showArrows={false}
        loop={true}
        loopInterval={5000 * randDay()}
        height={cardHeight}
        indicatorContainerStyle={{marginBottom: 40}}
        data={[
          {key: imageURLA, url: imageURLA},
          {key: imageURLB, url: imageURLB},
          {key: imageURLC, url: imageURLC},
        ]}
      />
      <View style={styles.newView}>
        <Text style={styles.textStyle}>
          {randDay()} day trip to {place}
        </Text>
        <View style={{marginLeft: 40}}>
          <Text style={styles.textStyleLight}>Drive: 4 hours</Text>
          <Text style={styles.textStyleLight}>Climate: pleasant</Text>
        </View>
      </View>
    </View>
  );
}

/*
<Image source={imageSource} style={styles.imageStyle}/>
 */
