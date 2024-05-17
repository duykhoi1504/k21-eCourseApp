import axios from "axios";

const BASE_URL='https://thanhduong.pythonanywhere.com/';


// const BASE_URL="http://127.0.0.1:8000/";
export const endpoints={
    'categories':'/categories/',
    'courses': '/courses/',
    'lessons': (courseId) => `/courses/${courseId}/lessons`
};

export default axios.create({
    baseURL:BASE_URL
});