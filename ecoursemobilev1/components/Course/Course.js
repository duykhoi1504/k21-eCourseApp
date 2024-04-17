import React from "react";
import { View,Text,ActivityIndicator,Image, ScrollView } from "react-native"
import MyStyles from "../../styles/MyStyles"
import { useState } from "react"
import APIs, { endpoints } from "../../configs/APIs";
import { Chip, List } from "react-native-paper";
import moment from "moment";
import "moment/locale/vi"
const Course =()=>{
    //nap lan du va duy nhat
    const [categories,setCategories]= React.useState(null);
    const [courses, setCourses]=React.useState([]);
    const [loading, setLoading]=React.useState(false)

    const loadCates= async () =>{
        try{
            let res=await APIs.get(endpoints['categories'])
            setCategories(res.data);
        }catch(ex){
            console.error(ex);
        }
    }

    const loadCourses= async () =>{
        try{
            setLoading(true);
            let res=await APIs.get(endpoints['courses'])
            //có result vì có phan trang
            setCourses(res.data.results);
        }catch(ex){
            console.error(ex);
        }finally{
            setLoading(false)
        }
    }

    React.useEffect(()=>{
        loadCates();
    },[]);

    React.useEffect(()=>{
        loadCourses();
    },[]);



    //
    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.subject}>DANH MUC KHOA HOC</Text>
            <View style={MyStyles.row}>
            {categories===null?<ActivityIndicator/>:<>
                {categories.map(c => <Chip style={MyStyles.margin} key={c.id} icon="text-long">{c.name}</Chip>)}</>}
            </View>
            <ScrollView>
                {courses.map(c => <List.Item style={MyStyles.margin} key={c.id} title={c.subject} description={moment(c.created_date).fromNow()} left={() => <Image style={MyStyles.avatar} source={{uri:c.image}} />}/>)}
                {loading && <ActivityIndicator/>}
            </ScrollView>
        </View>
    )
}

export default Course;