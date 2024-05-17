import MyStyles from "../../styles/MyStyles";
import { View, Text, ActivityIndicator } from "react-native"
import APIs, { endpoints } from "../../configs/APIs";
import React from "react";

const Lesson = ({ route }) => {
    const [lessons, setLessons] = React.useState(null);
    const courseId = route.param?.courseId;

    const loadLesson = async () => {
        try {
            let res = await APIs.get(endpoints['lessons'](courseId));
            setLessons(res.data);
        } catch (ex) {
            console.error(ex);
        }
    }

    React.useEffect(() => {
        loadLesson();
    }, [courseId]);

    return (
        <View style={[MyStyles.container, MyStyles.margin]}>
            <Text style={MyStyles.subject}>DANH MỤC BÀI HỌC {courseId}</Text>
            {lessons === null?<ActivityIndicator />:<>
                {lessons.map(l => <TouchableOpacity key={l.id}>
                    <Item instance={l} />
                </TouchableOpacity>)}
            </>}
        </View>
    )
}

export default Lesson;