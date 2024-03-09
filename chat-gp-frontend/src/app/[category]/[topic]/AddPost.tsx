"use client"

import { useRef } from "react";

const AddPost = () => {
  "use client"
  const dialogRef = useRef<HTMLDialogElement>(null);

  return (
    <div className="w-full">
      <button className="btn w-full" onClick={() => dialogRef.current?.showModal()}>Add post</button>
      <dialog ref={dialogRef} className="modal">
        <div className="modal-box">
          <h3 className="font-bold text-lg">Add a post</h3>
          <p className="py-4">Post title</p>
          <div className="modal-action">
            <form method="dialog">
              {/* if there is a button in form, it will close the modal */}
              <button className="btn">Close</button>
            </form>
          </div>
        </div>
      </dialog></div>
  )
}

export default AddPost;
