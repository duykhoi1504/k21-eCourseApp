
import React from 'react';
import Course from './components/Course/Course';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import 'react-native-gesture-handler';
import Lesson from './components/Course/Lesson';
import { Title } from 'react-native-paper';

const Stack = createNativeStackNavigator();

const MyStack = () => {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Course" component={Course} options={{title: 'Khoá học'}}/>
      <Stack.Screen name="Lesson" component={Lesson} />
    </Stack.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <MyStack/>
    </NavigationContainer>
  );
}

