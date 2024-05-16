import MyStyles from "../../styles/MyStyles";
import { View, Text } from "react-native"

const Lesson = ({route}) => {
    const courseId = route.param?.courseId;
    return (
        <View style={[MyStyles.container, MyStyles.margin]}>
            <Text style={MyStyles.subject}>DANH MỤC BÀI HỌC {courseId}</Text>
        </View>
    )
}

export default Lesson;