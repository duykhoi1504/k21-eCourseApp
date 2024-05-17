import MyStyles from "../../styles/MyStyles";
import { View, ActivityIndicator } from "react-native"
import React from 'react';
import APIs, { endpoints } from "../../configs/APIs";
import { Card, Text } from "react-native-paper";

const LessonDetails = ({ route }) => {
    const [lesson, setLesson] = React.useState(null);
    const [comments, setComments] = React.useState(null);
    const lessonId = route.param?.lessonId;

    const loadLesson = async () => {
        try {
            let res = await APIs.get(endpoints['lesson-details'](lessonId));
            setLesson(res.data);
        } catch (ex) {
            console.error(ex);
        }
    }

    const loadComments = async () => {
        try {
            let res = await APIs.get(endpoints['comments'](lessonId));
            setComments(res.data);
        } catch (ex) {
            console.error(ex);
        }
    }

    React.useEffect(() => {
        loadLesson();
    }, [lessonId]);

    return (
        <View style={[MyStyles.container, MyStyles.margin]}>
            {lesson === null ? <ActivityIndicator /> : <>
                <Card>
                    <Card.Title title="Card Title" subtitle="Card Subtitle" />
                    <Card.Content>
                        <Text variant="titleLarge">{lesson.subject}</Text>
                        <Text variant="bodyMedium">Card content</Text>
                    </Card.Content>
                    <Card.Cover source={{ uri: lesson.image }} />
                </Card>
            </>}
        </View>
    );
}

export default LessonDetails;