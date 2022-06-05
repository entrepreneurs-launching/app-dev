import React from 'react';
import {View, Text, Dimensions} from 'react-native';

import ImagedCarouselCard from 'react-native-imaged-carousel-card';

export default function TripsCard(props) {
  const cardWidth = Dimensions.get('window').width * 0.95;

  return (
    <View style={{paddingTop: 10}}>
      <ImagedCarouselCard
        width={cardWidth}
        height={cardWidth * 0.75}
        text={props.text}
        source={{
          uri: props.uri,
        }}
      />
    </View>
  );
}
