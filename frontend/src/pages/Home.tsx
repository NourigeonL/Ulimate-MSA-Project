import { useState, useEffect } from "react"
import api from "../api"
import PostDetail from "../components/PostDetail"
import { Post } from "../types"
import "../styles/Home.css"
import LoadingIndicator from "../components/LoadingIndicator"
function Home(){
    const [posts, setPosts] = useState<Array<Post>>([])
    const [loading, setLoading] = useState(false);
    useEffect(() => {
        //getPost();
    }, [])
    
    const getPost = () =>{
        setLoading(true);
        api
        .get("/api/blog/posts/")
        .then((res) => res.data)
        .then((data) => {setPosts(data); console.log(data); setLoading(false)})
        .catch((err) => alert(err));

    };

    return <div>
        <h2>Posts</h2>
        {loading && <LoadingIndicator />}
        {posts.map((post) => <PostDetail post={post} key={post.id}/>)}
    </div>
}

export default Home
