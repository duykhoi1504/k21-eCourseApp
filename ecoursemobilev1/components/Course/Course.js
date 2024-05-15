import React from "react";
import { View,Text,ActivityIndicator,Image, ScrollView } from "react-native"
import MyStyles from "../../styles/MyStyles"
import { useState } from "react"
import APIs, { endpoints } from "../../configs/APIs";
import { Chip, List, Searchbar } from "react-native-paper";
import moment from "moment";
import "moment/locale/vi"

const Course =()=>{
    //nap lan du va duy nhat
    const [categories,setCategories]= React.useState(null);
    const [courses, setCourses]=React.useState([]);
    const [loading, setLoading]=React.useState(false)
    const [q, setQ] = React.useState("");
    const [cateId, setCateId] = React.useState("");

    const loadCates= async () =>{
        try{
            let res=await APIs.get(endpoints['categories'])
            setCategories(res.data);
        }catch(ex){
            console.error(ex);
        }
    }

    const loadCourses= async () =>{
        let url = `${endpoints['courses']}?q=${q}&category_id=${cateId}`;
        try{
            setLoading(true);
            let res=await APIs.get(url)
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
    },[q, cateId]);



    //
    return (
        <View style={[MyStyles.container, MyStyles.margin]}>
            <View style={MyStyles.row}>
            <Chip mode={!cateId?"outlined":"flat"} style={MyStyles.margin} onPress={() => setCateId("")} icon="shape-outline">Tất cả</Chip>
            {categories===null?<ActivityIndicator/>:<>
                {categories.map(c => <Chip mode={cateId===c.id?"outlined":"flat"} onPress={() => setCateId(c.id)} style={MyStyles.margin} key={c.id} icon="shape-outline">{c.name}</Chip>)}</>}
            </View>
            <View>
            <Searchbar placeholder="Tìm khoá học..." value={q} onChangeText={setQ}/>
            </View>
            <ScrollView>
                {courses.map(c => <List.Item style={MyStyles.margin} key={c.id} title={c.subject} description={moment(c.created_date).fromNow()} left={() => <Image style={MyStyles.avatar} source={{uri:c.image}} />}/>)}
                {loading && <ActivityIndicator/>}
            </ScrollView>
        </View>
    )
}

export default Course;