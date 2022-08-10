import React, {useState, useEffect, useReducer} from 'react';
import {
  View,
  Pressable,
  Text,
  Dimensions,
  Image,
  ImageEditor,
} from 'react-native';

import ImagedCarouselCard from 'react-native-imaged-carousel-card';
import {RNCarousel} from 'react-native-carousel-cards';
import {Storage} from 'aws-amplify';

import styles from '../style/style';
import urls from '../strings/urls';

export default function TripsCardHalf(props) {
  const cardWidth = Dimensions.get('window').width * 0.5 * 0.95;
  const cardHeight = cardWidth;

  const idx = props.id;
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

  useEffect(() => {
    hour = todayHour();
    a = (hour % 4) + 0;
    b = (hour % 3) + 4;
    c = (hour % 3) + 4 + 3;
    // console.log('sup: ' + hour + ' ' + a + ' ' + b + ' ' + c);
    getImageA(a);
  }, []);

  const onPressFunction = (idx) => {
    props.onSelect(idx);
  };

  // change Pressable to TouchableOpacity
  return (
    <Pressable onPress={onPressFunction.bind(this, idx)}>
      <View style={{margin: 5}}>
        <ImagedCarouselCard
          width={cardWidth}
          height={cardHeight}
          shadowColor="aliceblue"
          text={randDay() + ' day trip to ' + place}
          source={{
            uri: imageURLA,
          }}
        />
      </View>
    </Pressable>
  );
}
