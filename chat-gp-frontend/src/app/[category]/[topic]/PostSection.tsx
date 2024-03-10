"use client"

import React, { FC, useState } from 'react'
import AddPost from './AddPost'
import { PostData } from '@/api'

type Props = {
  postsData: PostData[]
}

const PostSection: FC<Props> = ({ postsData }) => {
  const [posts, setPosts] = useState(postsData)

  return (
    <>
      <AddPost setPosts={setPosts} />

      {
        posts.map((post) => (
          <div key={`${post.fields.content}${post.fields.title}`} className="card w-full bg-base-100 shadow-xl">
            <div className="card-body">
              <h2 className="card-title">{post.fields.title}</h2>
              <p>{post.fields.content}</p>
              <div className="card-actions text-right justify-end">
                <p className='text-sm'><span className='font-bold'>salmana</span> at {new Date(post.fields.time_stamp).toLocaleDateString()}</p>
              </div>
            </div>
          </div>
        ))
      }

    </>
  )
}

export default PostSection
