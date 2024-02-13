"use client"

import { topics } from '@/constants'
import { usePathname } from 'next/navigation'
import React from 'react'

type PageParams = {
  params: {
    topic: string
  }
}

const TopicPage = ({ params: { topic } }: PageParams) => {
  const pathName = usePathname()
  const topicData = topics.find(x => "/" + x.path === pathName)

  if (!topicData) {
    return (
      <>
        <main className="w-full h-full grid place-items-center">
          <h2 className="text-black font-bold text-3xl mt-10">Topic {topic} not found</h2>
          <a className='pt-3' href='/'>Return to main page</a>
        </main>
      </>
    )
  }

  return (
    <main className="w-full h-full grid place-items-center grid-cols-[4fr,3fr] gap-10 p-10">

      <section>
        <div className="card w-full bg-slate-100 shadow-xl">
          <figure><img src={topicData.image} className='w-full h-64' alt={topicData.name} /></figure>
          <div className="card-body">
            <h2 className="card-title text-black">{topicData.name}</h2>
            <div className="text-sm breadcrumbs">
              <ul>
                <li><a href={"/" + topicData.path.split("/", 1)[0]}>{topicData.parent}</a></li>
                <li>{topicData.name}</li>
              </ul>
            </div>
            <p>Heart disease, or cardiovascular disease, encompasses various conditions affecting the heart and blood vessels, often leading to severe complications. It's a major cause of mortality globally. Types include coronary artery disease, heart failure, arrhythmias, and congenital defects. Risk factors include unhealthy habits like smoking, poor diet, lack of exercise, and underlying conditions such as hypertension, diabetes, and obesity. Symptoms range from chest pain and shortness of breath to fatigue and swelling. Early detection and management, including lifestyle changes, medication, and sometimes surgery, are crucial for better outcomes and quality of life.</p>
          </div>
        </div>
      </section>

      <section className='w-full h-full'>
        <div className='card w-full h-full bg-slate-100 shadow-xl'>
          <div className='card-body'>
            <h2 className='card-title text-black'>Chat</h2>

            <div className="chat chat-start">
              <div className="chat-bubble bg-slate-200 text-black">It's over Anakin, <br />I have the high ground.</div>
            </div>
            <div className="chat chat-end">
              <div className="chat-bubble bg-blue-500 text-white">You underestimate my power!</div>
            </div>

            <div className='mt-auto'></div>
            <input type="text" placeholder="Send a message" className="input bg-white outline-none text-black ring-0 input-bordered w-full" />
          </div>
        </div>
      </section>
    </main>
  )
}

export default TopicPage;
