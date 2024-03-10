"use client"

import { PostData } from "@/api";
import { Dispatch, FC, MouseEventHandler, SetStateAction, useRef, useState } from "react";
import toast, { Toaster } from "react-hot-toast";

type Props = {
  setPosts: Dispatch<SetStateAction<PostData[]>>;
}

const AddPost: FC<Props> = ({ setPosts }) => {
  const dialogRef = useRef<HTMLDialogElement>(null);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");

  const addPost: MouseEventHandler<HTMLButtonElement> = (e) => {
    e.preventDefault();

    if (title.trim().length < 5) return toast.error("Title must be at least 5 characters long");
    if (content.trim().length < 10) return toast.error("Content must be at least 10 characters long");

    setPosts((prevPosts) => {
      const newPost: PostData = {
        model: "chat-gp.post",
        pk: prevPosts.length + 1,
        fields: {
          user: 1,
          forum: 1,
          title,
          content,
          time_stamp: new Date().toISOString()
        }

      }

      return [newPost, ...prevPosts]
    })

    setTitle("");
    setContent("");
    dialogRef.current?.close();
  }

  return (
    <>
      { /* MAKE THIS STICKY */}
      <button className="btn w-full sticky top-5 z-50" onClick={() => dialogRef.current?.showModal()}>Add post</button>
      <div className="w-full">
        <dialog ref={dialogRef} className="modal">
          <div className="modal-box">
            <h3 className="font-bold text-lg">Add a post</h3>

            <label className="form-control w-full">
              <div className="label">
                <span className="label-text">Title</span>
              </div>
              <input type="text" placeholder="Your post title..." value={title} onChange={(e) => setTitle(e.target.value)} className="input input-bordered w-full" />
            </label>

            <label className="form-control">
              <div className="label">
                <span className="label-text">Content</span>
              </div>
              <textarea className="textarea textarea-bordered h-24" value={content} onChange={(e) => setContent(e.target.value)} placeholder="Your post content..."></textarea>
            </label>

            <div className="modal-action">
              <form className="space-x-2" method="dialog">
                {/* if there is a button in form, it will close the modal */}
                <button className="btn">Close</button>
                <button onClick={addPost} className="btn btn-success">Add</button>
              </form>
            </div>
          </div>

          <Toaster />
        </dialog>
      </div>
    </>
  )
}

export default AddPost;
