import {FC} from "react";
import { Post } from '../types';
import "../styles/Post.css"
interface PostDetailProps {
    post: Post
}

const PostDetail: FC<PostDetailProps>= ({post})=>{
    const formattedDate = new Date(post.created_at).toLocaleDateString()
    return <div className="post-container">
        <p className="post-title">{post.title}</p>
        <p className="post-content">{post.content}</p>
        <p className="post-date">{formattedDate}</p>
    </div>
}

export default PostDetail