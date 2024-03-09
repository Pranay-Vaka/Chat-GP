import React from 'react'
import { getAllMessages, getAllPosts, getForumByName } from '@/api'
import AddPost from './AddPost'
import ChatSection from './ChatSection'

type PageParams = {
  params: {
    topic: string,
    category: string
  }
}

const TopicPage = async ({ params: { topic, category } }: PageParams) => {
  console.log("topic:", topic, "category:", category);

  const messageData = await getAllMessages(category, topic);
  const postData = await getAllPosts(category, topic);
  const forumData = await getForumByName(category, topic);

  if (!forumData.ok || !messageData.ok || !postData.ok) {
    return (
      <>
        <main className="w-full h-full grid place-items-center">
          <h2 className="text-black font-bold text-3xl mt-10">Topic {topic} not found</h2>
          <a className='pt-3' href='/'>Return to main page</a>
        </main>
      </>
    )
  }

  const messages = messageData.messages;
  const posts = postData.posts;
  const forum = forumData.forums[0];

  return (
    <main className="w-full h-full grid place-items-start grid-cols-[4fr,3fr] gap-5 p-10">

      <section className='w-full h-full flex flex-col gap-5'>

        <div className="card w-full shadow-xl">
          <figure><img src={forum.fields.image} className='w-full h-64' alt={forum.fields.name} /></figure>
          <div className="card-body">
            <h2 className="card-title text-black">{forum.fields.name}</h2>
            <div className="text-sm breadcrumbs">
              <ul>
                <li><a href={`/${category}`}>{category}</a></li>
                <li>{topic.split("%20").join(" ")}</li>
              </ul>
            </div>
            <p>{forum.fields.description}</p>
          </div>
        </div>

        <AddPost />

        {posts.map((post) => (
          <div className="card w-full bg-base-100 shadow-xl">
            <div className="card-body">
              <h2 className="card-title">{post.fields.title}</h2>
              <p>{post.fields.content}</p>
              <div className="card-actions text-right justify-end">
                <p className='text-sm'><span className='font-bold'>salmana</span> at {new Date(post.fields.time_stamp).toLocaleDateString()}</p>
              </div>
            </div>
          </div>
        ))}

      </section>

      <section className='w-full sticky top-10'>
        <ChatSection messagesData={messages} topic={topic} />
      </section>
    </main>
  )
}

export default TopicPage;

